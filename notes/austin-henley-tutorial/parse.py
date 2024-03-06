import sys
from lex import *

# Parser object keeps track of current token and checks if the code matches the grammar.
# The parser object will control the lexer and request a new token as needed. So next, we have to implement the parser object.
class Parser:
    def __init__(self, lexer):
        pass

    # Return true if the current token matches.
    # Accessing methods on the Token Class
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    # Accessing methods on the Token Class
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        pass

    # Advances the current token.
    def nextToken(self):
        pass

    def abort(self, message):
        sys.exit("Error. " + message)