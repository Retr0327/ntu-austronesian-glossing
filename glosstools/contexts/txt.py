from dataclasses import dataclass

from .base import (
    GlossReader,
    GlossWriter,
)


@dataclass
class TxtGlossReader(GlossReader):
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
    def __enter__(self):
        file_path = self.get_file_path()
        has_path = file_path.exists()
        if not has_path:
            self._mkdir(file_path)

        self.__file = open(file_path, mode="w", encoding=self.encoding)
        return self

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def write(self):
        return self.__file.writelines("\n".join(self.data))
