
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/ALT ENT ESC FIM FOLD FUNC MAP SE and commentMult commentOne condicional false interpolacao2 not number numberF or string true variavelprograma : instrucoesinstrucoes : instrucao ';'     \n                      | instrucoes instrucao ';'instrucao : escrita\n                     | atribuicao\n                     | definicaoF\n                     | chamarF\n                     | condicional escrita : ESC '(' expressao ')' atribuicao : variavel '=' expressaodefinicaoF : FUNC variavel '(' parametros ')' ',' ':' expressao ';'\n                      | FUNC variavel '(' parametros ')' ':' instrucoes FIMchamarF : variavel '(' parametros  ')' conditional : SE expressao ':' instrucoes FIMexpressao : termo\n                     | expressao '+' termo\n                     | expressao '-' termo\n                     | interpolacaointerpolacao : expressao '#' '{' variavel '}' termo : fator\n                 | termo '*' fator        \n                 | termo '/'  fator fator : number\n                 | numberF\n                 | variavel\n                 | '(' expressao ')'\n                 | string  \n                 | aleatorio\n                 | lista\n                 | entrada\n                 | chamarFexpressao : expressao '<' '>' expressaoaleatorio : ALT '(' number ')'\n            lista : '[' elementos ']' \n                 | '[' ']' entrada : ENT '(' ')'  elementos : expressao\n                      | elementos ',' expressao  parametros : variavel\n                      | parametros ',' variavel argumentos : expressao\n                      | argumentos ',' expressao"
    
_lr_action_items = {'condicional':([0,2,13,18,73,76,],[8,8,-2,-3,8,8,]),'ESC':([0,2,13,18,73,76,],[9,9,-2,-3,9,9,]),'variavel':([0,2,11,13,14,15,16,18,19,33,38,41,42,45,46,53,58,59,64,73,75,76,],[10,10,17,-2,24,24,36,-3,24,24,36,24,24,24,24,66,24,69,24,10,24,10,]),'FUNC':([0,2,13,18,73,76,],[11,11,-2,-3,11,11,]),'$end':([1,2,13,18,],[0,-1,-2,-3,]),';':([3,4,5,6,7,8,12,21,22,23,24,25,26,27,28,29,30,31,35,40,49,52,55,56,57,60,61,63,65,68,70,74,77,78,79,],[13,-4,-5,-6,-7,-8,18,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,-10,-9,-35,-13,-26,-16,-17,-21,-22,-34,-36,-32,-33,-19,79,-12,-11,]),'(':([9,10,14,15,17,19,24,32,33,34,41,42,45,46,58,64,75,],[14,16,19,19,38,19,16,47,19,51,19,19,19,19,19,19,19,]),'=':([10,],[15,]),'FIM':([13,18,76,],[-2,-3,78,]),'number':([14,15,19,33,41,42,45,46,47,58,64,75,],[25,25,25,25,25,25,25,25,62,25,25,25,]),'numberF':([14,15,19,33,41,42,45,46,58,64,75,],[26,26,26,26,26,26,26,26,26,26,26,]),'string':([14,15,19,33,41,42,45,46,58,64,75,],[27,27,27,27,27,27,27,27,27,27,27,]),'ALT':([14,15,19,33,41,42,45,46,58,64,75,],[32,32,32,32,32,32,32,32,32,32,32,]),'[':([14,15,19,33,41,42,45,46,58,64,75,],[33,33,33,33,33,33,33,33,33,33,33,]),'ENT':([14,15,19,33,41,42,45,46,58,64,75,],[34,34,34,34,34,34,34,34,34,34,34,]),')':([20,21,22,23,24,25,26,27,28,29,30,31,36,37,39,49,51,52,54,55,56,57,60,61,62,63,65,66,68,70,74,],[40,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,-39,52,55,-35,65,-13,67,-26,-16,-17,-21,-22,70,-34,-36,-40,-32,-33,-19,]),'+':([20,21,22,23,24,25,26,27,28,29,30,31,35,39,49,50,52,55,56,57,60,61,63,65,68,70,71,74,77,],[41,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,41,41,-35,41,-13,-26,-16,-17,-21,-22,-34,-36,41,-33,41,-19,41,]),'-':([20,21,22,23,24,25,26,27,28,29,30,31,35,39,49,50,52,55,56,57,60,61,63,65,68,70,71,74,77,],[42,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,42,42,-35,42,-13,-26,-16,-17,-21,-22,-34,-36,42,-33,42,-19,42,]),'<':([20,21,22,23,24,25,26,27,28,29,30,31,35,39,49,50,52,55,56,57,60,61,63,65,68,70,71,74,77,],[43,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,43,43,-35,43,-13,-26,-16,-17,-21,-22,-34,-36,43,-33,43,-19,43,]),'#':([20,21,22,23,24,25,26,27,28,29,30,31,35,39,49,50,52,55,56,57,60,61,63,65,68,70,71,74,77,],[44,-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,44,44,-35,44,-13,-26,-16,-17,-21,-22,-34,-36,44,-33,44,-19,44,]),']':([21,22,23,24,25,26,27,28,29,30,31,33,48,49,50,52,55,56,57,60,61,63,65,68,70,71,74,],[-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,49,63,-35,-37,-13,-26,-16,-17,-21,-22,-34,-36,-32,-33,-38,-19,]),',':([21,22,23,24,25,26,27,28,29,30,31,36,37,48,49,50,52,54,55,56,57,60,61,63,65,66,67,68,70,71,74,],[-15,-18,-20,-25,-23,-24,-27,-28,-29,-30,-31,-39,53,64,-35,-37,-13,53,-26,-16,-17,-21,-22,-34,-36,-40,72,-32,-33,-38,-19,]),'*':([21,23,24,25,26,27,28,29,30,31,49,52,55,56,57,60,61,63,65,70,],[45,-20,-25,-23,-24,-27,-28,-29,-30,-31,-35,-13,-26,45,45,-21,-22,-34,-36,-33,]),'/':([21,23,24,25,26,27,28,29,30,31,49,52,55,56,57,60,61,63,65,70,],[46,-20,-25,-23,-24,-27,-28,-29,-30,-31,-35,-13,-26,46,46,-21,-22,-34,-36,-33,]),'>':([43,],[58,]),'{':([44,],[59,]),':':([67,72,],[73,75,]),'}':([69,],[74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'instrucoes':([0,73,],[2,76,]),'instrucao':([0,2,73,76,],[3,12,3,12,]),'escrita':([0,2,73,76,],[4,4,4,4,]),'atribuicao':([0,2,73,76,],[5,5,5,5,]),'definicaoF':([0,2,73,76,],[6,6,6,6,]),'chamarF':([0,2,14,15,19,33,41,42,45,46,58,64,73,75,76,],[7,7,31,31,31,31,31,31,31,31,31,31,7,31,7,]),'expressao':([14,15,19,33,58,64,75,],[20,35,39,50,68,71,77,]),'termo':([14,15,19,33,41,42,58,64,75,],[21,21,21,21,56,57,21,21,21,]),'interpolacao':([14,15,19,33,58,64,75,],[22,22,22,22,22,22,22,]),'fator':([14,15,19,33,41,42,45,46,58,64,75,],[23,23,23,23,23,23,60,61,23,23,23,]),'aleatorio':([14,15,19,33,41,42,45,46,58,64,75,],[28,28,28,28,28,28,28,28,28,28,28,]),'lista':([14,15,19,33,41,42,45,46,58,64,75,],[29,29,29,29,29,29,29,29,29,29,29,]),'entrada':([14,15,19,33,41,42,45,46,58,64,75,],[30,30,30,30,30,30,30,30,30,30,30,]),'parametros':([16,38,],[37,54,]),'elementos':([33,],[48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> instrucoes','programa',1,'p_program','grammar.py',33),
  ('instrucoes -> instrucao ;','instrucoes',2,'p_instrucoes','grammar.py',37),
  ('instrucoes -> instrucoes instrucao ;','instrucoes',3,'p_instrucoes','grammar.py',38),
  ('instrucao -> escrita','instrucao',1,'p_instrucao','grammar.py',46),
  ('instrucao -> atribuicao','instrucao',1,'p_instrucao','grammar.py',47),
  ('instrucao -> definicaoF','instrucao',1,'p_instrucao','grammar.py',48),
  ('instrucao -> chamarF','instrucao',1,'p_instrucao','grammar.py',49),
  ('instrucao -> condicional','instrucao',1,'p_instrucao','grammar.py',50),
  ('escrita -> ESC ( expressao )','escrita',4,'p_escrita','grammar.py',55),
  ('atribuicao -> variavel = expressao','atribuicao',3,'p_atribuicao','grammar.py',59),
  ('definicaoF -> FUNC variavel ( parametros ) , : expressao ;','definicaoF',9,'p_definicaoF','grammar.py',63),
  ('definicaoF -> FUNC variavel ( parametros ) : instrucoes FIM','definicaoF',8,'p_definicaoF','grammar.py',64),
  ('chamarF -> variavel ( parametros )','chamarF',4,'p_chamarF','grammar.py',71),
  ('conditional -> SE expressao : instrucoes FIM','conditional',5,'p_condicional','grammar.py',75),
  ('expressao -> termo','expressao',1,'p_expressao','grammar.py',79),
  ('expressao -> expressao + termo','expressao',3,'p_expressao','grammar.py',80),
  ('expressao -> expressao - termo','expressao',3,'p_expressao','grammar.py',81),
  ('expressao -> interpolacao','expressao',1,'p_expressao','grammar.py',82),
  ('interpolacao -> expressao # { variavel }','interpolacao',5,'p_interpolacao','grammar.py',91),
  ('termo -> fator','termo',1,'p_termo','grammar.py',95),
  ('termo -> termo * fator','termo',3,'p_termo','grammar.py',96),
  ('termo -> termo / fator','termo',3,'p_termo','grammar.py',97),
  ('fator -> number','fator',1,'p_fator','grammar.py',106),
  ('fator -> numberF','fator',1,'p_fator','grammar.py',107),
  ('fator -> variavel','fator',1,'p_fator','grammar.py',108),
  ('fator -> ( expressao )','fator',3,'p_fator','grammar.py',109),
  ('fator -> string','fator',1,'p_fator','grammar.py',110),
  ('fator -> aleatorio','fator',1,'p_fator','grammar.py',111),
  ('fator -> lista','fator',1,'p_fator','grammar.py',112),
  ('fator -> entrada','fator',1,'p_fator','grammar.py',113),
  ('fator -> chamarF','fator',1,'p_fator','grammar.py',114),
  ('expressao -> expressao < > expressao','expressao',4,'p_concatenacao','grammar.py',122),
  ('aleatorio -> ALT ( number )','aleatorio',4,'p_aleatorio','grammar.py',126),
  ('lista -> [ elementos ]','lista',3,'p_lista','grammar.py',131),
  ('lista -> [ ]','lista',2,'p_lista','grammar.py',132),
  ('entrada -> ENT ( )','entrada',3,'p_entrada','grammar.py',139),
  ('elementos -> expressao','elementos',1,'p_elementos','grammar.py',143),
  ('elementos -> elementos , expressao','elementos',3,'p_elementos','grammar.py',144),
  ('parametros -> variavel','parametros',1,'p_parametros','grammar.py',151),
  ('parametros -> parametros , variavel','parametros',3,'p_parametros','grammar.py',152),
  ('argumentos -> expressao','argumentos',1,'p_argumentos','grammar.py',159),
  ('argumentos -> argumentos , expressao','argumentos',3,'p_argumentos','grammar.py',160),
]
