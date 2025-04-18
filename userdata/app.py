import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('USERS_TABLE', 'users')
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    required_fields = ['first_name', 'last_name', 'email']

    for field in required_fields:
        if field not in event:
            raise ValueError(f"Missing required field: {field}")

    item = {
        'email': event['email'],
        'first_name': event['first_name'],
        'last_name': event['last_name']
    }

    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': 'User saved successfully.'
    }