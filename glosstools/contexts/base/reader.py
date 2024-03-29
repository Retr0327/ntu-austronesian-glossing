from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from glosstools.typings import FileDescriptorOrPath


@dataclass
class GlossReader(ABC):
    file_path: FileDescriptorOrPath
    encoding: str = "utf-8"

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args, **kwargs):
        pass

    def _strip_line(self, value: str):
        return value.strip()

    def _renumber(self, content_lines: list) -> list[str]:
        count = 1
        for index, value in enumerate(content_lines):
            if re.match(r"^(\d+\.|\d+)\s*$", value):
                content_lines[index] = f"{count}."
                count += 1
        return content_lines

    @abstractmethod
    def read(self) -> list[str]:
        return
