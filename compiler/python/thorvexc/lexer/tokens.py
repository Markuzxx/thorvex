from __future__ import annotations

from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):

    # Punctuation / Grouping
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    DOT_DOT = auto()
    SEMICOLON = auto()
    COLON = auto()
    NEWLINE = auto()

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


SINGLE_CHAR_TOKENS: dict[str, TokenType] = {

    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ',': TokenType.COMMA,
    '.': TokenType.DOT,
    ';': TokenType.SEMICOLON,
    ':': TokenType.COLON,
    '+': TokenType.PLUS,
    '-': TokenType.MINUS,
    '*': TokenType.STAR,
    '/': TokenType.SLASH,
    '%': TokenType.PERCENT,
    '=': TokenType.ASSIGN,
    '<': TokenType.LESS,
    '>': TokenType.GREATER

}


@dataclass()
class Token:

    type: TokenType
    lexeme: str
    line: int
    start_column: int
    end_column: int
    value: object | None = None

    @staticmethod
    def simple(type_: TokenType,
               lexeme: str,
               line: int,
               start_column: int,
               end_column: int) -> Token:

        return Token(type_, lexeme, line, start_column, end_column)

    @staticmethod
    def literal(type_: TokenType,
                lexeme: str,
                line: int,
                start_column: int,
                end_column: int,
                value: object) -> Token:

        return Token(type_, lexeme, line, start_column, end_column, value)

    @staticmethod
    def eof(line: int,
            column: int) -> Token:

        return Token(TokenType.EOF, "\0", line, column, column)
