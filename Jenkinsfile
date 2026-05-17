// flask-aws-monitor
@Library('my-shared-library') _
// include library function

pipeline {
    any agent

    stages{
        stage ('Checkout Code') {
            steps {
                script {
                    checkout scm
                    // This automatically clones the repo based on the SCM configuration in the UI
                }
            }
        }
        stage ('Docker Build') {
            steps {
                script {
                    sh "docker build -t flask-aws-monitor:latest ."
                    // This automatically clones the repo based on the SCM configuration in the UI
                }
            }
        }  
        stage ('SonarQube Scan')
            steps {
                script {
                    codeQuality.sonarCreateProject("testScan")
                    codeQuality.sonarLocalScan()
                    // sonarqube
                }
            }  
    }   
}
