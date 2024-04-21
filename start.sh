#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python3 -m venv env
source ./env/bin/activate

cd $DIR
set -o pipefail; pip3 install -r requirements.txt | { grep -v "already satisfied" || :; }

python3 fredagainbot.py