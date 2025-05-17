pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/alex-pancho/aqa_090125', branch: 'main'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -s -v --junitxml=$WORKSPACE/report.xml
                '''
                junit '**/report.xml'
            }
        }
    }
}