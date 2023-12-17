folder('Whanos base images') {
    description('Folder for Whanos base images.')
}
folder('Projects') {
    description('Folder for Whanos projects.')
}

job('Whanos base images/whanos-c') {
    steps {
        shell('docker build -t whanos-c .')
        shell('docker run --rm whanos-c')
    }
    wrappers {
        preBuildCleanup()
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