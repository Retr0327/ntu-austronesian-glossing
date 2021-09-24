import re
from .util import GlossReader
from typing import List, TextIO
from dataclasses import dataclass


@dataclass
class GlossReplacer:
    """
    The GlossReplacer object replaces a specified phrase with another specified phrase in a txt file.
    """

    file_name: str
    file_encoding: str = "utf-8-sig"

    def download_content(self) -> List[str]:
        """The download_content method downloads the content from the txt file.

        Returns:
            a list
        """
        with GlossReader(self.file_name, self.file_encoding) as file:
            return file

    def search_item(self, old, new) -> str:
        """The search_item method finds the old substring, and replaces it with the new one.

        Args:
            old (str): the old substring
            new (str): the new substring

        Returns:
            a str
        """
        content = self.download_content()
        result = (re.sub(old, new, value) for value in content)
        return "\n".join(result)

    def replace_item(self, __old: str, __new: str) -> TextIO:
        """The replace_item method returns a copy of the string where the old substring is replaced with the new substring.

        Args:
            __old (str): the old substring
            __new (str): the new substring

        Returns:
            a txt file
        """
        data = self.search_item(__old, __new)
        with open(self.file_name, "w", encoding="utf-8") as f:
            f.writelines(data)
