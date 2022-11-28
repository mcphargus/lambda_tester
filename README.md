# Lambda Docker Workflow

This thing is rad!

Borrowed heavily from https://adamnovotny.com/blog/serving-dynamic-web-pages-using-python-and-aws-lambda.html
Adam, you rawk dude! Thanks for the helpful post!

# usage

put credentials in your env, build and run. Easy peasy.

```sh
docker build . -t lambda_demo -f Dockerfile && \
    docker run \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    lambda_demo
```

# todo

- add asciinema demo to README
- stop getting distracted
- add lambda layer exporter
  - see https://gist.github.com/mcphargus/bf78f28a4c22e42e6a2f72d813fe3c38 for inspiration
- ~~start using gitflow~~
- find a yum proxy because this takes _way_ too long to build
- ~~fix this stupid soft_unicode markupsafe issue~~ updated requirements.txt to not have versions

  `ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/mnt/app/aws_layer/python/markupsafe/__init__.py)`
