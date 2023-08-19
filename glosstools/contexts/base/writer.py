from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class GlossWriter(ABC):
    file_path: str | Path
    data: Iterable[str]
    encoding: str = "utf-8"

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args, **kwargs):
        pass

    def get_file_path(self) -> Path:
        if isinstance(self.file_path, str):
            return Path(self.file_path)
        return self.file_path

    def _mkdir(self, file_path: Path):
        folder = file_path.parent
        folder.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def write(self):
        pass
