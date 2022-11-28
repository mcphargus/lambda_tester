cache=$1
docker build . -t lambda_demo -f Dockerfile $cache
cid=$(docker create lambda_demo)
docker cp $cid:/layer.zip layer.zip
docker run --env-file .env lambda_demo
