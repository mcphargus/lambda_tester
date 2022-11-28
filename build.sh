buildopts=$1
docker build . -t lambda_demo -f Dockerfile $buildopts && \
    docker run --env-file .env lambda_demo