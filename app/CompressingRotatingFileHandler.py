import os
from gzip import open as gzip_open
from logging.handlers import RotatingFileHandler

class CompressingRotatingFileHandler(RotatingFileHandler):
    def rotation_filename(self, default_name: str) -> str:
        return default_name + ".gz"

    def rotate(self, source: str, dest: str) -> None:
        with open(source, 'rb') as f_in, gzip_open(dest, 'wb') as f_out:
            f_out.writelines(f_in)
        os.remove(source)