# add your get-notes function here
import boto3
from boto3.dynamodb.conditions import Key
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")
 
def handler(event, context):
    email = event["queryStringParameters"]["email"]

    try:
        res = table.query(KeyConditionExpress=Key("email").eq(email))
        return {
            "statusCode": 200,
            "body": json.dumps(res["Items"])
        }
    except Exception as exp:
        print(exp)
        return{
            "status": 500,
            "body": json.dumps({
                "message": str(exp)
            })
        }