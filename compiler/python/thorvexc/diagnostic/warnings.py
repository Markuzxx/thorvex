from __future__ import annotations

from .diagnostic import Diagnostic, DiagnosticSeverity, DiagnosticCode


class ThorvexWarning(Diagnostic):

    def __init__(self,
                 code: DiagnosticCode,
                 message: str,
                 source: str,
                 line: int,
                 start_column: int,
                 end_column: int) -> None:

        super().__init__(DiagnosticSeverity.ERROR, code, message, source, line, start_column, end_column)
