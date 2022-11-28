# Lambda Docker Workflow

This thing is rad!

Borrowed heavily from https://adamnovotny.com/blog/serving-dynamic-web-pages-using-python-and-aws-lambda.html
Adam, you rawk dude! Thanks for the helpful post!

# usage

put credentials in your env, build and run. Easy peasy.

```sh
docker build . -t lambda_demo -f Dockerfile && \
    docker run --env-file creds.env lambda_demo
```

# configuration
  todo

# exporting lambda layers

From [this gist](https://gist.github.com/mcphargus/bf78f28a4c22e42e6a2f72d813fe3c38)

```sh
# bogarted from https://stackoverflow.com/questions/58504350/install-a-package-in-aws-lambda
pipenv --python 3.6
pipenv shell
. /home/clintwn/.local/share/virtualenvs/clintwn-UrrUtgNN/bin/activate
pipenv install jinja2
PY_DIR='build/python/lib/python3.9/site-packages'
mkdir -p $PY_DIR
pipenv lock -r > requirements.txt
pip install -r requirements.txt --no-deps -t $PY_DIR
cd build/
zip -r ../jinja2_layer.zip .
cd ..
rm -r build/
# now upload that sucker to the aws console under Lambda / Layers

```

# todo

- ~~add asciinema demo to README~~
  - https://asciinema.org/a/19ZWv7Y8DFv9mIBJmFJSik24i?startAt=30s
- stop getting distracted
- add lambda layer exporter
  - see https://gist.github.com/mcphargus/bf78f28a4c22e42e6a2f72d813fe3c38 for inspiration
- ~~start using github issues~~
- ~~start using gitflow~~
- find a yum proxy because this takes _way_ too long to build
- ~~fix this stupid soft_unicode markupsafe issue~~ updated requirements.txt to not have versions

  `ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/mnt/app/aws_layer/python/markupsafe/__init__.py)`
