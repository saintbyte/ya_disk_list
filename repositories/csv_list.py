class CsvImageListRepository:
    def __init__(self, settings):
        self._settings = settings

    def save_image_list(self, data: list):
        if self._settings["DEBUG"]:
            print(f"data len:{len(data)}")
        fh = open(self._settings["OUTPUT_CSV_FILENAME"], "w")
        for file in data:
            s = f"{file['path']};{file['name']};{file['size']};{file['sha256']};\n"
            fh.write(s)
        fh.close()

    def get_list(self, offset=0, limit=100):
        fh = open(self._settings["OUTPUT_CSV_FILENAME"], "w")