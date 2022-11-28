FROM amazonlinux:latest
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
RUN yum update -y
RUN yum install gcc gcc-c++ findutils zip -y
RUN amazon-linux-extras install python3.8
RUN mkdir -p /mnt/app
ADD . /mnt/app
WORKDIR /mnt/app
RUN python3.8 -m pip install --upgrade pip --user
RUN python3.8 -m pip install -r requirements.txt -t aws_layer/python
CMD python3.8 script.py