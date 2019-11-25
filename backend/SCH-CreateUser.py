import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CS321-User-Table')
    
def lambda_handler(event, context):
    msg = ''
    status_code = 200
    print(event)
    new_user_data = json.loads(event['body'])
    print(new_user_data['name'])
    
    response = table.scan()
    for item in response['Items']:
        if new_user_data['email'] == item['user']:
            status_code = 0
            msg = 'email already in use'
    
    
    if status_code == 200:
        table.put_item(
            Item={
                'user': new_user_data['email'],
                'password': new_user_data['password'],
                'data': [],
                'name': new_user_data['name']
            }
        )
        msg = 'User Created Successfully'
    
    return {
    'statusCode': status_code,
    'body': json.dumps(msg),
    'headers': {
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Allow" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Headers" : "*"
    }
}
