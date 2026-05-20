def appname = "hello-newapp"
def repo = "MosheBittan"  // Replace with your DockerHub username
def appimage = "docker.io/${repo}/${appname}"
def apptag = "${env.BUILD_NUMBER}"
def repoName = repo.toLowerCase()

podTemplate(cloud: 'kubernetes', containers: [
    containerTemplate(
        name: 'jnlp', 
        image: 'jenkins/inbound-agent:latest'
    ),
     containerTemplate(
        name: 'docker', 
        image: 'docker:26-dind', // Use the latest stable DinD image
        privileged: true,      // Essential for Docker daemon to run
        args: '--storage-driver=vfs' // VFS is safest for K8s, though slower
    ),
    containerTemplate(
        name: 'deployer', 
        image: 'elevy99927/k8s-deployer:latest', 
        command: 'cat', 
        ttyEnabled: true
    )
    ], 
  volumes: [
    emptyDirVolume(mountPath: '/var/lib/docker', memory: false) // Q: Why do we need this volume?
  ]) {
    node(POD_LABEL) {
        stage('chackout') {
            container('jnlp') {
            sh '/usr/bin/git config --global http.sslVerify false'
	    checkout scm
          }
        } // end chackout

        stage('Build') {
            container('docker') {
              echo "Building docker image..."
              sh "docker build -t $repoName:$apptag ."
              sh "echo docker push $appimage:$apptag"
              //sh "sleep 180"
            }
        } //end hello
        
        stage('Push') {
            container('docker') {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds', 
                        usernameVariable: 'DH_USER', 
                        passwordVariable: 'DH_PASS'
                    )
                ]){
              echo "Pushing docker image to DockerHUB..."
              sh "docker push MosheBittan/$appname:$apptag"
              //sh "sleep 180"
                }
            }
        } //end hello
    }
}
