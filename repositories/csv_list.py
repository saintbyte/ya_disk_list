from typing import IO


class CsvImageListRepository:
    fields = [   "path",        "name",        "size",        "sha256",    ]

    def __init__(self, settings):
        self._settings = settings

    @staticmethod
    def openfile(filename: str, mode: str) -> IO:
        return open(filename, mode)

    @staticmethod
    def normailize_line(line: str) -> str:
        line = line.strip()
        return line

    @staticmethod
    def parse_line(line: str) -> dict:
        arr = line.split(";")
        return dict(zip(CsvImageListRepository.fields,  arr))

    def save_image_list(self, data: list):
        if self._settings["DEBUG"]:
            print(f"data len:{len(data)}")
        fh = CsvImageListRepository.openfile(self._settings["OUTPUT_CSV_FILENAME"], "w")
        for file in data:
            s = f"{file['path']};{file['name']};{file['size']};{file['sha256']};\n"
            fh.write(s)
        fh.close()

    def get_list(self, offset=0, limit=100):
        fh = CsvImageListRepository.openfile(self._settings["OUTPUT_CSV_FILENAME"], "r")
        read_cnt = 0
        output_cnt = 0
        result = []
        for line in fh:
            read_cnt = read_cnt + 1
            if read_cnt < offset:
                continue
            output_cnt = output_cnt + 1
            line = CsvImageListRepository.normailize_line(line)
            result.append(CsvImageListRepository.parse_line(line))
            if output_cnt >= limit:
                break
        fh.close()
        return result
