python3 -m venv venv
. $WORKSPACE/venv/bin/activate

pip install -r requirements.txt
pytest $FOLDER -v --junitxml=$WORKSPACE/report.xml