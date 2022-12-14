import jinja2
import boto3
from rich.console import Console
from rich.table import Table
console = Console()

c = boto3.client('s3')

def lambda_handler(event,context={}):
    console.log('grabbing file list from s3://rowdy-videos')
    files = c.list_objects(Bucket='rowdy-videos')
    console.log('now we can make a table')
    table = Table(title='files n shiz')
    table.add_column("Key")
    table.add_column("LastModified")
    table.add_column("ETag")
    table.add_column("Size")
    for f in files['Contents']:
        k = f['Key']
        mdt = f['LastModified']
        et = f['ETag']
        size = f['Size']
        table.add_row(k,mdt.isoformat(),et,str(size))
    console.log(table)
    console.log("^^ there's your table")
    return {
        'statusCode':200,
        'body': 'done'
    }
