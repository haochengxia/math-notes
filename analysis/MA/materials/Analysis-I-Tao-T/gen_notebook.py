# As the math notation cannot be rendered in .md files, 
# run this file to generate .ipynb files for a comfortable
# reading exprience. DO NOT USE character ' in text.

# Created in 2022/03/11

from pathlib import Path
from typing import List
import io

tempelate = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [CONTENT]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}'''


def scan_md_files(p : Path) -> List[Path]:
    return list(p.glob('**/*.md'))


def generate():
    """
    create .ipynb files for all .md files
    """
    md_files = scan_md_files(Path('.'))
    for md_file in md_files:
        with md_file.open() as f:
            lines = f.readlines()
            r = io.StringIO()
            print(lines, file=r)
            c = r.getvalue()
            c = c.replace('\"', '\\\"')
            formatted_content = tempelate.replace('[CONTENT]', c).replace('\'', '\"')
            print(formatted_content)
            p = Path(md_file.name.replace('.md', '.ipynb'))
            p.write_text(formatted_content)


if __name__ == '__main__':
    generate()

