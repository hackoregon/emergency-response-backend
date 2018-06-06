#!/bin/bash
export PATH=$PATH:~/.local/bin


set -e
echo "Collect static files"
python -Wall manage.py collectstatic --noinput


# ./manage.py test --keepdb --noinput
pytest
