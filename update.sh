!/usr/bin/bash
git pull
python3.10 -m pip uninstall ihack -y
python3.10 -m pip uninstall ihackit -y
python3.10 -m pip install -r requirements.txt
python3.10 -m pip install --upgrade ihackit
python3.10 -m pip install .
rm -rf dist build *.egg-info
