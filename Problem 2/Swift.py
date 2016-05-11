#------------------------------------------------------------
# HMM tokenizer
# ------------------------------------------------------------


# List of token names.
tokens = [
             'AND_OP', 'OR_OP', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY', \
             'SEMI', 'EQ_OP', 'NE_OP', 'LE_OP', 'GE_OP', 'ELEM', 'PIPE', 'EQUALS', \
             'LT_OP', 'GT_OP', 'PLUS', 'MINUS', 'MULT', 'DIV', 'PRCNT', 'BANG', \
             'COMMA', 'SQUOTE', 'LAMBDA', 'MAP_TO', 'DQUOTE', 'COLON', 'BACKSLASH'\
             #'DOT', \
             'INTEGER', 'IDENTIFIER', 'CLFLOAT', 'CLSTRING' \
             ] + list(reserved.keys())

# Regular expression rules for simple tokens




def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        # print "In t_IDENTIFIER, saw: ", t.value
        t.type = t.value.upper()
    return t

def t_CLSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,]*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

# BNF Parsing rules

def p_program(p):
    '''program : declarations
               | functions
               | declarations functions'''
    print "Saw: ", p[1]

def p_functions(p):
    '''functions : function
                 | functions function'''

def p_funciton(p):
    '''function : type IDENTIFIER LPAREN RPAREN LCURLY RCURLY
                | type IDENTIFIER LPAREN RPAREN LCURLY declarations RCURLY
                | type IDENTIFIER LPAREN RPAREN LCURLY declarations statements RCURLY'''

def p_declarations(p):
    '''declarations : type idList SEMI
               | declarations type idList SEMI
               | type idList EQUALS expression SEMI
               | declarations type idList EQUALS expression SEMI'''
    if len(p)   == 4 : p[0] = p[2]
    elif len(p) == 5 : p[0] = p[3]
    elif len(p) == 6 : p[0] = p[2] + " = " + p[4]
    elif len(p) == 7 : p[0] = p[3] + " = " + p[5]
    print p[0]

def p_idList(p):
    '''idList : IDENTIFIER
              | IDENTIFIER COMMA idList'''
    if len(p) == 2: p[0] = p[1]
    else: p[0] = p[1] + ", " + p[3]

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | LIST
            | TUPLE
            | OBJECT
            | STRING
            | FUNC'''

def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : expression SEMI
                 | assignment SEMI
                 | whileStatement'''
    print "Saw a statement", p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''
    p[0] = "Assignment"

def p_while(p):
    '''whileStatement : WHILE LPAREN expression RPAREN LCURLY statements RCURLY'''
    p[0] = "While"

def p_expression(p):
    '''expression : conjunction
                  | conjunction OR_OP expression'''
    p[0] = "Expression: ", p[1]

def p_conjunction(p):
    '''conjunction : equality
                   | AND_OP equality'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_equality(p):
    '''equality : relation
                | relation equOp equality'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_equOp(p):
    '''equOp : EQ_OP
             | NE_OP'''
    p[0] = p[1]

def p_relation(p):
    '''relation : addition
                | addition relOp relation'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = str(p[1])

def p_relOp(p):
    '''relOp : LT_OP
             | LE_OP
             | GT_OP
             | GE_OP'''
    p[0] = p[1]

def p_addition(p):
    '''addition : term
                | term addOP addition'''
    from java.lang import Math
    import Addition
    if len(p) == 4 and isinstance( p[1], int ) and isinstance( p[3], int ):
        print "Calling java Math: ", Math.max(p[1], p[3])
        print "Calling java Addition.add: ", Addition.add(p[1], p[3])
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = p[1]

def p_addOP(p):
    '''addOP : PLUS
             | MINUS'''
    p[0] = p[1]

def p_term(p):
    '''term : factor
            | factor mulOP term'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = p[1]

def p_mulOP(p):
    '''mulOP : MULT
             | DIV
             | PRCNT'''
    p[0] = p[1]

def p_factor(p):
    '''factor : primary
              | primary unaryOP factor'''
    if len(p) == 4: p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else : p[0] = p[1]

def p_unaryOp(p):
    '''unaryOP : MINUS
               | BANG'''
    p[0] = p[1]

def p_primary(p):
    '''primary : literal'''
    p[0] = p[1]

def p_literal(p):
    '''literal : INTEGER
               | IDENTIFIER
               | TRUE
               | FALSE
               | CLFLOAT
               | CLSTRING'''
    p[0] = p[1]

def emptyline(self):
    """Do nothing on empty input line"""
    pass# Error handling rule

def p_error(p):
    print "At line: ", p.lexer.lineno,
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

with open('swiftCode.txt', 'r') as content_file:
    content = content_file.read()
yacc.parse(content)
