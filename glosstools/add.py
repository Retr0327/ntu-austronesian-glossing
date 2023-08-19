from __future__ import annotations

from dataclasses import dataclass
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from .contexts.base import (
        GlossReader,
        GlossWriter,
    )


@dataclass
class GlossFirstLineAdder:
    file_path: str
    new_file_path: Path
    reader: GlossReader
    writer: GlossWriter

    @property
    def file_data(self) -> list[str]:
        with self.reader(file_path=self.file_path) as file:
            return file.read()

    def get_first_line_index(self, content: list[str]):
        return (
            index + 1
            for index, value in enumerate(content)
            if re.findall(r"\d\.\s*$", value)
        )

    def _modify_new_line(self, new_line: str, clitic_sep: bool = True):
        if clitic_sep:
            gla_without_space = re.sub(
                r"([\^\<\>]|(L[\d@].)|\-\b|[\[\]]|)", "", new_line
            )
            gla_with_space = re.sub(
                r"(?<=a)\.\b|[\s]|(\b\=\b)+", " ", gla_without_space
            )
            return gla_with_space

        gla_without_space = re.sub(
            r"([\^\<\>]|(L[\d@].)|(\b\=\b)|\-\b|[\[\]]|)", "", new_line
        )
        gla_with_space = re.sub(r"(?<=a)\.\b|[\s]+", " ", gla_without_space)
        return gla_with_space

    def _add(
        self, line_indexes: list[int], file_data: list[str], clitic_sep: bool = True
    ):
        count = 0
        for index in line_indexes:
            gla = file_data[index + count]
            file_data.insert(index + count, self._modify_new_line(gla, clitic_sep))
            count += 1
        return file_data

    def add(self, clitic_sep: bool = True):
        firt_line_index = list(self.get_first_line_index(self.file_data))
        data = self._add(firt_line_index, self.file_data, clitic_sep)
        with self.writer(file_path=self.new_file_path, data=data) as file:
            file.write()
