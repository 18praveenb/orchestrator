#!/usr/bin/env zsh

python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# Get GeneralUserGS
wget "https://www.dropbox.com/s/4x27l49kxcwamp5/GeneralUser_GS_1.471.zip?dl=1"
unzip "GeneralUser_GS_1.471.zip?dl=1"
cp GeneralUser\ GS\ 1.471/GeneralUser\ GS\ v1.471.sf2 GeneralUserGS.sf2
