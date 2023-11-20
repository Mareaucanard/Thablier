function build {
    docker build -t "whanos-$1-base" - < images/$1/Dockerfile.base
}

PIDS=""

build c & PIDS="$PIDS $!"
build java & PIDS="$PIDS $!"
build javascript & PIDS="$PIDS $!"
build python & PIDS="$PIDS $!"
build befunge & PIDS="$PIDS $!"


FAIL=0
for job in $PIDS
do
    wait $job || let "FAIL+=1"
done

if [ "$FAIL" == "0" ];
then
    echo "All docker succeeded"
else
    echo "$FAIL fails"
    exit 1
fi
