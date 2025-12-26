from __future__ import annotations

from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):

    # Punctuation / Grouping
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    DOT = auto()
    DOT_DOT = auto()
    SEMICOLON = auto()
    COLON = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()

    # Literals
    INT_LIT = auto()
    FLOAT_LIT = auto()
    STR_LIT = auto()

    # Keywords
    ...

    # Special
    EOF = auto()


@dataclass()
class Token:

    type: TokenType
    lexeme: str
    line: int
    column: int
    value: object | None = None

    @staticmethod
    def simple(type_: TokenType,
               lexeme: str,
               line: int,
               column: int) -> Token:

        return Token(type_, lexeme, line, column)

    @staticmethod
    def literal(type_: TokenType,
                lexeme: str,
                line: int,
                column: int,
                value: object) -> Token:

        return Token(type_, lexeme, line, column, value)

    @staticmethod
    def eof(line: int,
            column: int) -> Token:

        return Token(TokenType.EOF, "\0", line, column)
