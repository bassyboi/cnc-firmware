# CNC Firmware Utilities

This repository now includes a simple Python script to organize
large raw text dumps into categorized files.

## Usage

1. Place your raw text file (e.g., `raw.txt`) in this directory.
2. Run `./sort_into_files.py raw.txt` (optionally add `-o output_dir` to
   place results in a separate folder).
3. The script will produce several files in the chosen output directory:
   - `menu.txt` for lines containing `#menu`
   - `paths.txt` for lines with `/flash/` paths or language files
   - `errors.txt` for lines mentioning errors or exceptions
   - `numbers.txt` for purely numeric lines
   - `other.txt` for all remaining lines

These output files can then be examined or processed separately.
