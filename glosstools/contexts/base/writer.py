from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class GlossWriter(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args, **kwargs):
        pass

    def _mkdir(self, file_path: Path):
        folder = file_path.parent
        folder.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def write(self):
        pass
