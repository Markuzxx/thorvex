from __future__ import annotations

from .diagnostic import DiagnosticSeverity, Diagnostic, ThorvexError, ThorvexWarning


class DiagnosticManager:

    def __init__(self,
                 source_code: str,
                 severity: DiagnosticSeverity = DiagnosticSeverity.ERROR) -> None:

        self.source_code = source_code
        self.severity = severity

        self.errors: list[ThorvexError] = []
        self.warnings: list[ThorvexWarning] = []

    def report(self,
               diagnostic: Diagnostic) -> None:

        if isinstance(diagnostic, ThorvexError): self.errors.append(diagnostic)
        elif isinstance(diagnostic, ThorvexWarning): self.warnings.append(diagnostic)

    def has_errors(self) -> bool:

        return len(self.errors) > 0

    def dump(self) -> None:

        for error in self.errors: print(error)

        if self.severity >= DiagnosticSeverity.WARNING:
            for warning in self.warnings: print(warning)
