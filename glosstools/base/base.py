from abc import ABC, abstractmethod


class GlossTool:
    @abstractmethod
    def download_content(self):
        pass

    @abstractmethod
    def search_item(self):
        pass

    @abstractmethod
    def write_txt(self, data):
        pass
