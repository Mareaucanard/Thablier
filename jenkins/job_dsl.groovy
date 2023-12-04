folder('Whanos base images') {
    description('Folder for Whanos base images.')
}
folder('Projects') {
    description('Folder for Whanos projects.')
}

job('Whanos base images/whanos-c') {
    steps {
        shell('gcc --version | grep "13.2" > /dev/null')
        shell('test -f Makefile')
        shell('make')
        shell('./<compiled_binary>')
    }
    wrappers {
        preBuildCleanup()
    }
}

// job('Whanos base images/whanos-java') {
// }

// job('Whanos base images/whanos-javascript') {
// }

// job('Whanos base images/whanos-python') {
// }

// job('Whanos base images/whanos-befunge') {
// }