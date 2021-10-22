import re  
from typing import List, TextIO
from dataclasses import dataclass
from .util import GlossReader, GlossSaver


@dataclass
class GlossReplacer:
    """
    The GlossReplacer object replaces a specified phrase with another specified phrase in a txt file.
    """

    file_name: str
    file_encoding: str = "utf-8-sig"

    @property
    def content(self) -> List[str]:
        """The content property set the txt data based on the `file_name` and `file_encoding`.

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
        result = (re.sub(old, new, value) for value in self.content)
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
        return GlossSaver(
            file_name=self.file_name, data=data, folder_name="gloss_replaced"
        ).save()

