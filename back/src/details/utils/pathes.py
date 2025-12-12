import os


def get_out_dir():
    return os.environ.get("OUT_DIR", '/tmp/vacancy-data')