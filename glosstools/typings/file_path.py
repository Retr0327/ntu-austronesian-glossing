from __future__ import annotations

from os import PathLike
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]  # stable
FileDescriptorOrPath: TypeAlias = int | StrOrBytesPath
