FROM amazonlinux:latest
# RUN yum update -y
RUN yum install  zip -y
RUN amazon-linux-extras install python3.8
RUN mkdir -p /mnt/app
ADD . /mnt/app
WORKDIR /mnt/app
RUN python3.8 -m pip install --upgrade pip --user
RUN python3.8 -m pip install -r requirements.txt -t aws_layer/python
RUN cp -r /mnt/app/aws_layer/python /
RUN zip -r /layer.zip /python
CMD python3.8 script.py