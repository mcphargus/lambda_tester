docker build . -t lambda_demo -f Dockerfile && \
    docker run --env-file creds.env lambda_demo