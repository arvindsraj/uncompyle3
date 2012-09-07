from uncompyle3.utils.spark import GenericASTBuilder

from .astnode import ASTNode


class Parser(GenericASTBuilder):

    def __init__(self):
        GenericASTBuilder.__init__(self, ASTNode, "stmts")

    def p_grammar(self, args):
        """
        stmts ::= stmts sstmt
        stmts ::= sstmt
        sstmt ::= stmt
        stmt ::= call_stmt
        call_stmt ::= expr POP_TOP
        designator ::= STORE_NAME
        """

    def p_expr(self, args):
        """
        expr ::= call_function
        expr ::= LOAD_NAME
        expr ::= LOAD_CONST
        expr ::= binary_expr
        binary_expr ::= expr expr binary_op
        binary_op ::= BINARY_POWER
        binary_op ::= BINARY_MULTIPLY
        binary_op ::= BINARY_DIVIDE
        binary_op ::= BINARY_FLOOR_DIVIDE
        binary_op ::= BINARY_TRUE_DIVIDE
        binary_op ::= BINARY_MODULO
        binary_op ::= BINARY_ADD
        binary_op ::= BINARY_SUBTRACT
        binary_op ::= BINARY_SUBSCR
        binary_op ::= BINARY_LSHIFT
        binary_op ::= BINARY_RSHIFT
        binary_op ::= BINARY_AND
        binary_op ::= BINARY_XOR
        binary_op ::= BINARY_OR
        """

    def p_assign(self, args):
        '''
        stmt ::= assign
        assign ::= expr designator
        '''

#    def p_custom(self, args):
#        """
#        call_function ::= expr CALL_FUNCTION
#        """
