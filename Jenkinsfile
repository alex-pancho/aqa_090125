pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout code') {
            steps {
                git branch: 'lesson_31', url: 'https://github.com/Kseniia-Karnaukh/aqa_090125'
            }
        }

        stage('Set up Python and install dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest lesson_31/test_homework_29.py --junitxml=test-results.xml
                '''
            }
        }

        stage('Publish test results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/test-results.xml', allowEmptyArchive: true
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
