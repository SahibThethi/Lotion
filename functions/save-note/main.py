import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("lotion-30117033")

def lambda_handler (event, context):
    body = json.loads(event ["body"])
    try:
        table.put_item(Item=body)
        return {
            "statusCode": 201,
            "body": "success"
        }
    except Exception as exp:
        print (exp)
        return {
            "statusCode": 500,
            "body": json. dumps(
            {
                "message":str(exp)
            }
        )
    
    }