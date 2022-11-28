import sys, os
if os.environ.get('IN_DOCKER'):
    sys.path.append('/mnt/app/aws_layer')
    sys.path.append('/mnt/app/aws_layer/python')

import click
from dotenv import load_dotenv
load_dotenv()
import os

# @click.command()
# def export_lambda_layer():
#     """
#         todo. This is going to be insecure and very gnarly. Just sayin'
#         DON'T DO AS I DO, AND DON'T RUN THIS ANYWHERE IMPORTANT
#     """
#     pass

if __name__=='__main__':
    from app import lambda_handler
    event = {}
    lambda_handler(event)

