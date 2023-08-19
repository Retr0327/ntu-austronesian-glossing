import re
from typing import List


class GlossReader:
    """
    The GlossReader object is a context manager that reads the glossing txt file.
    """

    def __init__(self, file_name: str, file_encoding: str) -> None:
        self.__file_name = file_name
        self.__file_encoding = file_encoding

    def __enter__(self) -> List[str]:
        self.__file = open(self.__file_name, encoding=self.__file_encoding)
        content = self.__file.readlines()
        content_without_newlines = map(self.remove_newline, content)
        return self.renumber(list(content_without_newlines))

    def __exit__(self, *args, **kwargs):
        return self.__file.close()

    def remove_newline(self, content_value: str):
        """The remove_newline method removes the newline `\n` in a string.

        Args:
            content_value (str): the value in content

        Returns:
            a list
        """
        return content_value.strip()

    def renumber(self, content: list) -> List[str]:
        """The renumber method renumbers the numbering in the file.

        Args:
            content (list): the file content

        Returns:
            a list
        """
        count = 1
        for index, value in enumerate(content):
            if re.match(r"^(\d+\.|\d+)\s*$", value):
                content[index] = f"{count}."
                count += 1
        return content
