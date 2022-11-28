import sys, os
sys.path.append('/mnt/app/aws_layer')
sys.path.append('/mnt/app/aws_layer/python')
from dotenv import load_dotenv
import click

load_dotenv()
import os

@click.command()
def export_lambda_layer():
    """
        todo
        think think think.
        we're creating a good working layer in the dockerfile build.
        what's the best way to get it out?
    """
    pass

if __name__=='__main__':
    from app import lambda_handler
    event = {}
    lambda_handler(event)

