from pathlib import Path 
from dataclasses import dataclass


@dataclass
class GlossSaver:
    """
    The GlossSaver object saves the data to a txt file on the desktop.
    """

    file_name: str
    data: str
    folder_name: str

    def __post_init__(self):
        self.desktop = Path.home() / "Desktop"

    def create_folder(self) -> Path:
        """The create_folder method creates the `gloss_replaced` folder.

        Returns:
            a folder path
        """
        dir_name = self.folder_name
        new_dir = Path(self.desktop, dir_name)
        new_dir.mkdir(parents=True, exist_ok=True)
        return new_dir

    def write_txt(self, path: Path):
        """The write_txt method writes the data to a txt file

        Args:
            path (Path): the file path
        """
        with open(path / self.file_name, "w", encoding="utf-8") as f:
            f.writelines(self.data)

    def save(self):
        """The save method saves the data to the desktop."""
        save_folder = self.desktop / self.folder_name
        is_exist = save_folder.exists()

        if is_exist is False:
            new_dir = self.create_folder()
            self.write_txt(new_dir)

        self.write_txt(save_folder)
