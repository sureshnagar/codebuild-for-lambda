import 'json'

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode: 200, 
        'body: JSON.dumps('Hello from Lambda. Modified version..........!')
    }
