from pathlib import Path
from vacancy.utils.pathes import get_out_dir


def init_directories():
    output_path = get_out_dir()
    Path(output_path).mkdir(parents=True, exist_ok=True)
