import re
from dataclasses import dataclass
from .util import GlossReader, GlossSaver
from typing import Generator, List, TextIO


@dataclass
class GlossAdder:
    """
    The GlossAdder object adds another interlinear gloss (i.e. gloss preamble) in a txt file.
    """

    file_name: str
    file_encoding: str = "utf-8-sig"
    clitic_sep: bool = True

    @property
    def content(self) -> List[str]:
        """The content property set the txt data based on the `file_name` and `file_encoding`.

        Returns:
            a list
        """
        with GlossReader(self.file_name, self.file_encoding) as file:
            return file

    def get_gla_index(self, content: list) -> Generator[int, None, None]:
        """The get_gla_index gets the index of the original orthography (i.e. gla).

        Args:
            content (list): the content from the txt file.

        Returns:
            a generator
        """
        return (
            index + 1
            for index, value in enumerate(content)
            if re.findall("\d\.\s*$", value)
        )

    def modify_gla(self, gla: str) -> str:
        """The modify_gla method modifies the original orthography.

        Args:
            gla (str): the original orthography

        Returns:
            a str
        """
        if self.clitic_sep:
            gla_without_space = re.sub(r"([\^\<\>]|(L[\d@].)|\-\b|[\[\]]|)", "", gla)
            gla_with_space = re.sub(
                r"(?<=a)\.\b|[\s]|(\b\=\b)+", " ", gla_without_space
            )
            return gla_with_space

        gla_without_space = re.sub(
            r"([\^\<\>]|(L[\d@].)|(\b\=\b)|\-\b|[\[\]]|)", "", gla
        )
        gla_with_space = re.sub(r"(?<=a)\.\b|[\s]+", " ", gla_without_space)
        return gla_with_space

    def search_item(self, gla_index: list, content: list) -> List[str]:
        """The search_item method searches the index of the original orthography (i.e. gla), and modifies 
           it by calling the method `modify_gla()`.

        Args:
            gla_index (list): the index of the original orthography
            content (list): the content from the txt file.

        Returns:
            a list
        """
        count = 0
        for index_value in gla_index:
            gla = content[index_value + count]
            content.insert(index_value + count, self.modify_gla(gla))
            count += 1
        return "\n".join(content)

    def add(self) -> TextIO:
        """The add method adds another interlinear gloss (i.e. gloss preamble) to the txt file.

        Returns:
            a txt file
        """ 
        gla_index = list(self.get_gla_index(self.content))
        data = self.search_item(gla_index, self.content)
        return GlossSaver(
            file_name=self.file_name, data=data, folder_name="gloss_added"
        ).save()
