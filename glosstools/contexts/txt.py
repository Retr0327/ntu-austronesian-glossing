from __future__ import annotations

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Iterable,
)

from .base import (
    GlossReader,
    GlossWriter,
)

if TYPE_CHECKING:
    from pathlib import Path

    from glosstools.typings import FileDescriptorOrPath


@dataclass
class TxtGlossReader(GlossReader):
    file_path: FileDescriptorOrPath
    encoding: str = "utf-8"

    def __enter__(self):
        self.__file = open(self.file_path, encoding=self.encoding)
        self.__content = self.__file.readlines()
        return self

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def read(self) -> list[str]:
        content_without_newlines = map(self._strip_line, self.__content)
        return self._renumber(list(content_without_newlines))


@dataclass
class TxtGlossWriter(GlossWriter):
    file_path: Path
    data: Iterable[str]
    encoding: str = "utf-8"

    def __enter__(self):
        has_path = self.file_path.exists()
        if not has_path:
            self._mkdir(self.file_path)

        self.__file = open(self.file_path, mode="w", encoding=self.encoding)
        return self

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def write(self):
        return self.__file.writelines("\n".join(self.data))
