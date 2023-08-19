from __future__ import annotations

from dataclasses import dataclass
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from glosstools.typings import FileDescriptorOrPath


@dataclass(slots=True)
class GlossReader:
    file_path: FileDescriptorOrPath
    encoding: str = "utf-8"

    def __enter__(self) -> list[str]:
        self.__file = open(self.file_path, encoding=self.encoding)
        content = self.__file.readlines()
        content_without_newlines = map(self._strip_line, content)
        return self.renumber(list(content_without_newlines))

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def _strip_line(self, value: str):
        return value.strip()

    def renumber(self, content_lines: list) -> list[str]:
        count = 1
        for index, value in enumerate(content_lines):
            if re.match(r"^(\d+\.|\d+)\s*$", value):
                content_lines[index] = f"{count}."
                count += 1
        return content_lines
