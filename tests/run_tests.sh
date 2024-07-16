#!/bin/bash


if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

source myenv/bin/activate


pip install --upgrade pip
pip install -r requirements.txt


if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

pytest test.py

deactivate
