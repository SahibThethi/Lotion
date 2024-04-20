# add your delete-note function here
import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")

def lambda_handler(event, context):
    email = event["queryStringParameters"]["email"]
    id = event["queryStringParameters"]["id"]

    try:
        table.delete_item(Key={
            "email": email,
            "id": id,
        })

        return {
            "statusCode": 200,
            "body": "succes"
        }
    except Exception as exp:
        print(exp)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(exp)
            })
        }
    