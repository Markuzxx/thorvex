from __future__ import annotations

from enum import IntEnum, StrEnum
from dataclasses import dataclass


class DiagnosticSeverity(IntEnum):

    ERROR = 20
    WARNING = 10


class DiagnosticCode(StrEnum):

    # Internal errors (0XXX)
    E0000 = "E0000"
    ...

    # Lexer errors (1XXX)
    E1000 = "E1000"
    E1001 = "E1001"
    E1002 = "E1002"
    E1003 = "E1003"
    E1004 = "E1004"
    ...

    # Warnings
    ...


@dataclass()
class Diagnostic:

    severity: DiagnosticSeverity
    code: DiagnosticCode
    message: str
    snippet: str
    source: str
    line: int
    start_column: int
    end_column: int

    def __str__(self) -> str:

        # Colors
        severity_colors: dict[DiagnosticSeverity, str] = {
            DiagnosticSeverity.ERROR: "\033[31m",   # Red
            DiagnosticSeverity.WARNING: "\033[33m", # Yellow
        }
        color = severity_colors.get(self.severity, "\033[0m")
        reset = "\033[0m"
        gutter_color = "\033[90m" # Gray

        # Gutter
        line_gutter = f"  {self.line} | "
        empty_gutter = ' ' * len(line_gutter[:-2]) + "| "

        # Split snippet
        snippet_prefix = self.snippet[:(self.start_column - 1)]
        snippet_highlight = self.snippet[(self.start_column - 1):self.end_column]
        snippet_suffix = self.snippet[self.end_column:]

        # Caret
        caret_padding = ' ' * (self.start_column - 1)
        caret = '^' * (self.end_column - self.start_column + 1)

        return (f"{color}{self.severity.name.lower()}[{self.code}]: {self.message}\n"
                f"{gutter_color}  --> {self.source}:{self.line}:{self.start_column}\n"
                f"{empty_gutter}\n"
                f"{line_gutter}{reset}{snippet_prefix}{color}{snippet_highlight}{reset}{snippet_suffix}\n"
                f"{gutter_color}{empty_gutter}{caret_padding}{color}{caret}{reset}\n")
