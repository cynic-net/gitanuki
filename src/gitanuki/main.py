import  argparse
from    pathlib  import Path


def main() -> None:
    p = argparse.ArgumentParser(
        prog='tanuki',
        description='Collection and rendering of Git repositories',
    )
    p.add_argument('dir', type=Path,
        help='configuration/data/output directory')
    args = p.parse_args()
