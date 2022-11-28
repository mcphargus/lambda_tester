FROM amazonlinux:latest as build-stage
RUN yum install zip -y
RUN amazon-linux-extras install python3.8
RUN mkdir -p /mnt/app
ADD script.py app.py README.md requirements.txt __init__.py /mnt/app/
WORKDIR /mnt/app
RUN python3.8 -m pip install --upgrade pip --user
RUN python3.8 -m pip install -r requirements.txt -t aws_layer/python
RUN cp -r /mnt/app/aws_layer/python /
RUN zip -r /layer.zip /python
CMD python3.8 script.py