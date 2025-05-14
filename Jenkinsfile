pipeline {
    agent any

    tools {
        allure 'allure'  // Назва, яку вказав у Global Tool Configuration
    }

    stages {
        stage('Setup Docker') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y docker.io docker-compose lsof
                    docker --version
                    docker-compose --version
                '''
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    def cleanupStatus = sh(script: './scripts/cleanup.sh', returnStatus: true)
                    if (cleanupStatus != 0) {
                        echo "Clean up script returned non-zero status ${cleanupStatus}, но продолжаем pipeline."
                    }
                }
            }
        }

        stage('Build Containers') {
            steps {
                sh 'docker-compose -p pytest_app up -d --build'
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh '''
                        docker-compose run --rm app pytest /app/lesson_29 --alluredir=/app/allure-results
                    '''
                }
            }
        }

        stage('Collect Allure Results') {
            steps {
                sh 'docker cp $(docker-compose -p pytest_app ps -q app):/app/allure-results ./allure-results'
            }
        }
    }


    post {
        always {
            allure([
              results: [[path: 'allure-results']],
              reportBuildPolicy: 'ALWAYS'
            ])
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            sh 'docker-compose -p pytest_app down -v --remove-orphans || true'
        }
    }
}
