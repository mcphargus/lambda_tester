
import click
from dotenv import load_dotenv
load_dotenv()
import os


from app import lambda_handler

event = {}

lambda_handler(event)