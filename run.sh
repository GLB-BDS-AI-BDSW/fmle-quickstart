#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python ${script_dir}/quickstart.py >> /out/output.txt