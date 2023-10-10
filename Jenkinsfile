pipeline {
  agent any

  stages {
    stage('Build & Test') {
      agent {
        docker {
          image 'python:3.10-alpine'
        }
      }
      environment {
        HOME = "${env.WORKSPACE}"
      }
      stages {
        stage('Get Code') {
          steps {
            git 'https://github.com/dimsidelnikov/otus_final_project/'
          }
        }
        stage('Build') {
          steps {
            sh 'pip install -U pip'
            sh 'pip install -r requirements.txt'
          }
        }
        stage('Test') {
          steps {
            sh 'python3 -m pytest --executor ${IP_SELENOID} \
            --url ${URL_OPENCART} -n ${NUM_THREADS} \
            --browser ${BROWSER} --bv ${BROWSER_VERSION}'
            stash name: 'allure-results', includes: 'allure-results/*'
          }
        }
      }
    }
  }
  post {
    always {
      unstash 'allure-results'
      script {
        allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'allure-results']]
      ])
      }
    }
  }
}