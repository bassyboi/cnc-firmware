#!/usr/bin/env python3
"""Split a raw text file into categorized files.

The script scans each line of the input and sorts it into different
categories. By default files named ``menu.txt`` ``paths.txt`` ``errors.txt``
``numbers.txt`` and ``other.txt`` are produced in the working directory.  An
output directory can be specified with ``-o``.
"""
import argparse
import re
from pathlib import Path


def sort_lines(source_path: str, output_dir: Path):
    """Stream ``source_path`` and write categorized output files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        'menu': open(output_dir / 'menu.txt', 'w', encoding='utf-8'),
        'paths': open(output_dir / 'paths.txt', 'w', encoding='utf-8'),
        'errors': open(output_dir / 'errors.txt', 'w', encoding='utf-8'),
        'numbers': open(output_dir / 'numbers.txt', 'w', encoding='utf-8'),
        'other': open(output_dir / 'other.txt', 'w', encoding='utf-8'),
    }

    menu_re = re.compile(r'#menu\d+', re.IGNORECASE)
    path_re = re.compile(r'/flash/|\\LAN', re.IGNORECASE)
    error_re = re.compile(r'error|exception', re.IGNORECASE)
    number_re = re.compile(r'^\d+$')

    with open(source_path, 'r', errors='ignore') as fh:
        for raw in fh:
            line = raw.rstrip('\n')
            if not line:
                continue
            if menu_re.search(line):
                target = 'menu'
            elif path_re.search(line):
                target = 'paths'
            elif error_re.search(line):
                target = 'errors'
            elif number_re.match(line.strip()):
                target = 'numbers'
            else:
                target = 'other'
            print(line, file=files[target])

    for f in files.values():
        f.close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Categorize lines in a text file.'
    )
    parser.add_argument('src', help='input text file')
    parser.add_argument('-o', '--output', default='.',
                        help='directory for result files')
    args = parser.parse_args()

    sort_lines(args.src, Path(args.output))


if __name__ == '__main__':
    main()
