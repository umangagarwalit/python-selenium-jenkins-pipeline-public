pipeline {
    agent any
    
    stages {
	
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/umangagarwalit/python-selenium-jenkins-pipeline-public.git', branch: 'main'
            }
        }

        stage('Install Python & Dependencies') {
            steps {
				bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
				bat 'pytest -s -v test_script.py --html=reports/report.html --self-contained-html --capture=tee-sys'
            }
		}
		
		stage('Publish Test Reports') {
            steps {
                publishHTML([
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }	
        }
    }
}
