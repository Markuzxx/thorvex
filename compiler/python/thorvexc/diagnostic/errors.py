from __future__ import annotations

from .diagnostic import Diagnostic, DiagnosticSeverity, DiagnosticCode


class ThorvexError(Diagnostic):

    def __init__(self,
                 code: DiagnosticCode,
                 message: str,
                 snippet: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int) -> None:

        super().__init__(DiagnosticSeverity.ERROR, code, message, snippet, source, line, start_column, end_column)


########################################################################################################################
# Lexer errors (1XXX)

class LexerError(ThorvexError):

    def __init__(self,
                 message: str,
                 snippet: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int,
                 code: DiagnosticCode = DiagnosticCode.E1000) -> None:

        super().__init__(code, message, snippet, source, line, start_column, end_column)


class UnexpectedCharacterError(LexerError):

    def __init__(self,
                 character: str,
                 snippet: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int) -> None:

        super().__init__(f"Unexpected character: '{character}'.", snippet, source, line, start_column, end_column,
                         code=DiagnosticCode.E1001)


class UnterminatedCharacterLiteralError(LexerError):

    def __init__(self,
                 snippet: str,
                 source: str,
                 line: int,
                 column: int) -> None:

        super().__init__("Unterminated character literal", snippet, source, line, column, column,
                         code=DiagnosticCode.E1002)


class UnterminatedStringLiteralError(LexerError):

    def __init__(self,
                 snippet: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int) -> None:

        super().__init__("Unterminated string literal.", snippet, source, line, start_column, end_column,
                         code=DiagnosticCode.E1003)


class InvalidEscapeSequenceError(LexerError):

    def __init__(self,
                 escape_sequence: str,
                 snippet: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int) -> None:

        super().__init__(f"Invalid escape sequence: '{escape_sequence}'.", snippet, source, line, start_column,
                         end_column, code=DiagnosticCode.E1004)
