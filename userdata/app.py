import boto3
import os, json

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('USERS_TABLE', 'users')
table = dynamodb.Table(table_name)


def lambda_handler(event, context):

    body = event.get("body")
    print(f"Request body: {body}")
    # If it's a JSON string, parse it:
    if body:
        data = json.loads(body)
    else:
        data = event
    print(f"data : {data}")

    required_fields = ['first_name', 'last_name', 'email']

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    item = {
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name']
    }

    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': 'User saved successfully.'
    }