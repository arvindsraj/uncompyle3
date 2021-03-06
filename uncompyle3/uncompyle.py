from .scanner.scanner import Scanner
from .scanner.token import Token
from .parser.parser import Parser
from .walker.walker import Walker
from .utils.debug import debug


class Uncompyle:

    def __init__(self):
        self._scanner = Scanner()
        self._parser = Parser()
        self._walker = Walker()

    def run(self, file_bytes):
        ### File format check stage ###
        # python version magic = file_bytes[:4]
        # source file timestamp = file_bytes[4:8]
        # source file size = file_bytes[8:12]
        bytecode = file_bytes[12:]

        ### Scanner stage ###
        tokens = self._scanner.run(bytecode)
        debug('---Tokens debug output---\n#: offset linestart type attr pattr')
        k = 1
        for i in tokens:
            debug('op {}:'.format(k), i.offset, i.linestart, i.type, i.attr, i.pattr)
            k+=1

        ### Parser stage ###
        debug('\n\n---Parser stage debug---')
        if len(tokens) > 2 and tokens[-1] == Token(type_='RETURN_VALUE') and tokens[-2] == Token(type_='LOAD_CONST'):
            del tokens[-2:]

        ast = self._parser.parse(tokens)
        debug(ast)

        ### Walker stage ###
        debug('\n\n---Walker stage debug---')
        return self._walker.gen_source(ast)
