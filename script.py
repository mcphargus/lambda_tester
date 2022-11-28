import sys, os
if os.environ.get('IN_DOCKER'):
    sys.path.append('/mnt/app/aws_layer')
    sys.path.append('/mnt/app/aws_layer/python')

import click
from dotenv import load_dotenv
load_dotenv()
import os


from app import lambda_handler

event = {}

lambda_handler(event)