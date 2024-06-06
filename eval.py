import random
from lexer import Lexer
from grammar import Grammar
import sys
import os

class Evaluator:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.c_code = ""
        self.lists = {}
        self.types = {}

    def evaluate(self, tree):
        if not tree:
            return
        if isinstance(tree, list):
            for node in tree:
                self.evaluate(node)
        else:
            node_type = tree[0]
            if node_type == 'escrita':
                self.evaluate_escrita(tree)
            elif node_type == 'atribuicao':
                self.evaluate_atribuicao(tree)
            elif node_type == 'definicaoFunc':
                self.evaluate_definicaoFunc(tree)
            elif node_type == 'definicaoFuncMult':
                self.evaluate_definicaoFuncMult(tree)
            elif node_type == 'chamar':
                return self.evaluate_chamar(tree)
            elif node_type == 'if':
                self.evaluate_condicional(tree)
            elif node_type == 'entrada':
                return self.evaluate_entrada(tree)
            elif node_type == 'aleatorio':
                return self.evaluate_aleatorio(tree)

    def evaluate_escrita(self, tree):
        _, expr = tree
        value = self.evaluate_expression(expr)
        print(value)
        if isinstance(value, list):
            if len(value) > 0:
                self.c_code += '    printf("{'
                for i, v in enumerate(value):
                    self.c_code += f'{self.convert_expression_to_c(v)}'
                    if i < len(value) - 1:
                        self.c_code += ', '
                self.c_code += '}\\n");\n'
        elif isinstance(value, str):
            self.c_code += f'    printf("%s\\n", {self.convert_expression_to_c(expr)});\n'
        else:
            self.c_code += f'    printf("%d\\n", {self.convert_expression_to_c(expr)});\n'

    def evaluate_atribuicao(self, tree):
        _, var, expr = tree
        value = self.evaluate_expression(expr)
        self.variables[var] = value
        if isinstance(value, list):
            if len(value) > 0:
                self.lists[var] = value
                size = len(value)
                self.types[var] = 'list'
                self.c_code += f'    int {var}[{size}] = {self.convert_expression_to_c(expr)};\n'
        elif isinstance(value, str):
            self.types[var] = 'string'
            self.c_code += f'    char {var}[{len(value) + 1}] = "{value}";\n'
        else:
            self.types[var] = 'int'
            self.c_code += f'    int {var} = {self.convert_expression_to_c(expr)};\n'

    def evaluate_definicaoFunc(self, tree):
        _, name, params, expr = tree
        self.functions[name] = (params, expr)
        params_str = ', '.join([f'int {p}' for p in params])
        self.c_code += f'int {name}({params_str}) {{\n    return {self.convert_expression_to_c(expr)};\n}}\n'

    def evaluate_definicaoFuncMult(self, tree):
        _, name, params, instrs = tree
        self.functions[name] = (params, instrs)
        params_str = ', '.join([f'int {p}' for p in params])
        self.c_code += f'int {name}({params_str}) {{\n'
        for instr in instrs:
            self.evaluate(instr)
        self.c_code += '}\n'

    def evaluate_chamar(self, tree):
        _, name, args = tree
        if name in self.functions:
            params, body = self.functions[name]
            local_vars = self.variables.copy()
            for param, arg in zip(params, args):
                local_vars[param] = self.evaluate_expression(arg)
            return self.evaluate_function_body(body, local_vars)
        else:
            raise ValueError(f"Function {name} not defined")

    def evaluate_condicional(self, tree):
        _, condition, instructions = tree
        if self.evaluate_expression(condition):
            self.evaluate(instructions)
        self.c_code += f'if ({self.convert_expression_to_c(condition)}) {{\n'
        for instr in instructions:
            self.evaluate(instr)
        self.c_code += '}\n'

    def evaluate_concatenacao(self, expr):
        _, left, right = expr
        return str(self.evaluate_expression(left)) + str(self.evaluate_expression(right))

    def evaluate_expression(self, expr):
        if isinstance(expr, tuple):
            if expr[0] == '+':
                left = self.evaluate_expression(expr[1])
                right = self.evaluate_expression(expr[2])
                return self._convert_to_same_type(left, right, '+')
            elif expr[0] == '-':
                left = self.evaluate_expression(expr[1])
                right = self.evaluate_expression(expr[2])
                return self._convert_to_same_type(left, right, '-')
            elif expr[0] == '*':
                return self.evaluate_expression(expr[1]) * self.evaluate_expression(expr[2])
            elif expr[0] == '/':
                return self.evaluate_expression(expr[1]) // self.evaluate_expression(expr[2])
            elif expr[0] == 'interpolar':
                return self.evaluate_interpolation(expr)
            elif expr[0] == 'concatenacao':
                return self.evaluate_concatenacao(expr)
            elif expr[0] == 'entrada':
                return self.evaluate_entrada(expr)
            elif expr[0] == 'aleatorio':
                return self.evaluate_aleatorio(expr)
        elif isinstance(expr, list):
            return expr
        elif isinstance(expr, str):
            if expr in self.variables:
                return self.variables[expr]
            else:
                return expr
        else:
            return expr

    def _convert_to_same_type(self, left, right, operator):
        if isinstance(left, str) and isinstance(right, (int, float)):
            right = str(right)
        elif isinstance(right, str) and isinstance(left, (int, float)):
            left = str(left)
        elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
        return left + right  # For concatenation of strings

    def evaluate_interpolation(self, expr):
        _, before, var = expr
        return str(self.evaluate_expression(before)) + str(self.variables.get(var, ''))

    def evaluate_function_body(self, body, local_vars):
        old_vars = self.variables.copy()
        self.variables.update(local_vars)
        result = None
        if isinstance(body, list):
            for instruction in body:
                result = self.evaluate(instruction)
        else:
            result = self.evaluate_expression(body)
        self.variables = old_vars
        return result

    def evaluate_entrada(self, tree):
        user_input = input("Entrada: ")
        # Try to convert to int, if fails return as string
        try:
            return int(user_input)
        except ValueError:
            return user_input

    def evaluate_aleatorio(self, tree):
        _, max_value = tree
        return random.randint(0, max_value)

    def convert_expression_to_c(self, expr):
        if isinstance(expr, tuple):
            if expr[0] == '+':
                return f'({self.convert_expression_to_c(expr[1])} + {self.convert_expression_to_c(expr[2])})'
            elif expr[0] == '-':
                return f'({self.convert_expression_to_c(expr[1])} - {self.convert_expression_to_c(expr[2])})'
            elif expr[0] == '*':
                return f'({self.convert_expression_to_c(expr[1])} * {self.convert_expression_to_c(expr[2])})'
            elif expr[0] == '/':
                return f'({self.convert_expression_to_c(expr[1])} / {self.convert_expression_to_c(expr[2])})'
        elif isinstance(expr, list):
            if len(expr) > 0:
                return '{' + ', '.join([self.convert_expression_to_c(e) for e in expr]) + '}'
            else:
                return '{}'
        elif isinstance(expr, str):
            return expr
        else:
            return str(expr)
    
    def generate_c_code(self, filename):
        with open(filename, 'w') as f:
            f.write("#include <stdio.h>\n#include <stdlib.h>\n\n")
            f.write("int main() {\n")
            f.write(self.c_code)
            f.write("    return 0;\n")
            f.write("}\n")
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file = sys.argv[1]
        path = "fca/"

        #criar o caminho para o ficheiro fca
        caminho = os.path.join(path,file)
        with open(caminho, 'r') as file:
            data = file.read()
    else:
        print("Enter code (type 'exit' or 'EOF' to finish):")
        lines = []
        while True:
            line = input()
            if line.lower() == 'exit' or line == 'EOF':
                break
            lines.append(line)
        data = '\n'.join(lines)

    lexer = Lexer()
    lexer.build()
    parser = Grammar()
    parser.build()

    tree = parser.parse(data)
    evaluator = Evaluator()
    evaluator.evaluate(tree)
    evaluator.generate_c_code('output.c')