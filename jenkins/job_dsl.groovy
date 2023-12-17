folder('Whanos base images') {
    description('Folder for Whanos base images.')
}
folder('Projects') {
    description('Folder for Whanos projects.')
}

job('Whanos base images/whanos-c') {
    steps {
        shell('kubectl apply -f /kubeyml/c.yml') // ADD YAML FILE
        shell('kubectl wait --for=condition=complete job/whanos-c')
        shell('kubectl logs job/whanos-c')
    }
}

job('Whanos base images/whanos-java') {
    steps {
        shell('docker build -t whanos-java .')
        shell('docker run --rm whanos-java')
    }
}

job('Whanos base images/whanos-javascript') {
    steps {
        shell('docker build -t whanos-javascript .')
        shell('docker run --rm whanos-javascript')
    }
}

job('Whanos base images/whanos-python') {
    steps {
        shell('docker build -t whanos-python .')
        shell('docker run --rm whanos-python')
    }

}

job('Whanos base images/whanos-befunge') {
    steps {
        shell('docker build -t whanos-befunge .')
        shell('docker run --rm whanos-befunge')
    }
}