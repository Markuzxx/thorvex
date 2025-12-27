from __future__ import annotations

from .diagnostic import Diagnostic, DiagnosticSeverity, DiagnosticCode


class ThorvexError(Diagnostic):

    def __init__(self,
                 code: DiagnosticCode,
                 message: str,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int) -> None:

        super().__init__(DiagnosticSeverity.ERROR, code, message, snippet, source, line, column_start, column_end)


########################################################################################################################
# Lexer errors (1XXX)

class LexerError(ThorvexError):

    def __init__(self,
                 message: str,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int,
                 code: DiagnosticCode = DiagnosticCode.E1000) -> None:

        super().__init__(code, message, snippet, source, line, column_start, column_end)


class UnexpectedCharacterError(LexerError):

    def __init__(self,
                 character: str,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int) -> None:

        super().__init__(f"Unexpected character: '{character}'.", snippet, source, line, column_start, column_end,
                         code=DiagnosticCode.E1001)


class UnterminatedCharacterLiteralError(LexerError):

    def __init__(self,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int) -> None:

        super().__init__("Unterminated character literal", snippet, source, line, column_start, column_end,
                         code=DiagnosticCode.E1002)


class UnterminatedStringLiteralError(LexerError):

    def __init__(self,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int) -> None:

        super().__init__("Unterminated string literal.", snippet, source, line, column_start, column_end,
                         code=DiagnosticCode.E1003)


class InvalidEscapeSequenceError(LexerError):

    def __init__(self,
                 escape_sequence: str,
                 snippet: str,
                 source: str,
                 line: int,
                 column_start: int,
                 column_end: int) -> None:

        super().__init__(f"Invalid escape sequence: '{escape_sequence}'.", snippet, source, line, column_start,
                         column_end, code=DiagnosticCode.E1004)
