from __future__ import annotations

from dataclasses import dataclass
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from re import Pattern

    from .contexts.base import (
        GlossReader,
        GlossWriter,
    )


@dataclass
class GlossSubstituter:
    file_path: str
    new_file_path: Path
    reader: GlossReader
    writer: GlossWriter

    @property
    def file_data(self) -> list[str]:
        with self.reader(file_path=self.file_path) as file:
            return file.read()

    def _sub(
        self,
        old: str | Pattern[str],
        new: str | Pattern[str],
        line_number: int | None = None,
    ):
        result = []
        line_count = -1
        for line in self.file_data:
            if line.strip().endswith(".") and line.strip().split(".")[0].isdigit():
                line_count = 0
            else:
                if line_count != -1:
                    if line_number is None or line_count == line_number:
                        line = re.sub(old, new, line)  # noqa: PLW2901
                    line_count += 1
                    if line_count > 2:
                        line_count = -1

            result.append(line)
        return result

    def sub(
        self,
        old: str | Pattern[str],
        new: str | Pattern[str],
        line_number: int | None = None,
    ):
        subbed = self._sub(old=old, new=new, line_number=line_number)
        with self.writer(file_path=self.new_file_path, data=subbed) as file:
            file.write()
