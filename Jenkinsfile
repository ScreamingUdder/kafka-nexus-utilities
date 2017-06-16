node('fedora && python3') {
    // Use a virtualenv to prevent polluting the build server
    def installed = fileExists 'bin/activate'
    if (!installed) {
        stage("Install Python Virtual Enviroment") {
            sh 'virtualenv -p python3 --no-site-packages nexus_venv'
        }
    }

    // Get the latest version of the code
    // The 'checkout scm' command will automatically pull down the code from the appropriate branch that triggered this build.
    stage ("Get Latest Code") {
        checkout scm
    }

    // Install dependencies in the virtualenv using pip
    stage ("Install Application Dependencies") {
        sh '''
            source nexus_venv/bin/activate
            pip3 install -r requirements.txt
            deactivate
           '''
    }

    // After all of the dependencies are installed, you can start to run your tests.
    // The code below assumes that you're using the django-jenkins python libary to run the test but you can
    // also use the built in django test runner, nose or tox
    stage ("Run Unit/Integration Tests") {
        def testsError = null
        try {
            sh '''
                source nexus_venv/bin/activate
                pytest
                deactivate
               '''
        }
        catch(err) {
            testsError = err
            currentBuild.result = 'FAILURE'
        }
        finally {
            junit 'reports/junit.xml'

            if (testsError) {
                throw testsError
            }
        }
    }
}