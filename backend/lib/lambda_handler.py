# lambda_handler.py
import json

def handler(event, context):
    """
    Lambda function handler.
    Responds with a greeting including the name from the input event.
    """
    name = event.get('name', 'World')
    message = f"Hello, {name}!"
    print(message)

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }