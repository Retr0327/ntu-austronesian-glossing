from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(slots=True)
class GlossWriter:
    file_path: Path
    data: Iterable[str]
    encoding: str = "utf-8"

    def __enter__(self) -> list[str]:
        self.__file = open(self.file_path, mode="w", encoding=self.encoding)
        has_path = self.file_path.exists()
        if has_path:
            self._mkdir(self.file_path)
        self.__file.writelines(self.data)

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def _mkdir(self, file_path: Path):
        new_dir = Path(file_path)
        new_dir.mkdir(parents=True, exist_ok=True)
