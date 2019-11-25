import json
import boto3

from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CS321-User-Table')

def my_try(event):
    print('MY TRY')
    table_response = table.scan()
    print(table_response)
    for item in table_response['Items']:
        if item['user'] == json.loads(event['body'])['name']:
            if item['password'] == json.loads(event['body'])['password']:
                return True
    return False
    

def lambda_handler(event, context):

    if my_try(event):
        return {
            'statusCode': '200',
            'body': json.dumps('Login Successful'),
            'headers': {
                "Content-Type" : "application/json",
                "Access-Control-Allow-Origin" : "*",
                "Allow" : "GET, OPTIONS, POST",
                "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
                "Access-Control-Allow-Headers" : "*"
            }
        }  
    else:
        return {
            'statusCode': '0',
            'body': json.dumps('Login Unsuccessful'),
            'headers': {
                "Content-Type" : "application/json",
                "Access-Control-Allow-Origin" : "*",
                "Allow" : "GET, OPTIONS, POST",
                "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
                "Access-Control-Allow-Headers" : "*"
            }
        }
    
    
    statusCode = 0;
    response = table.scan(
        FilterExpression= Attr('password').eq(event['Password'])
    )
    
    
    print('response len:', len(response)); 
    print('response:', response); 
    print('response: ', response.get('Items')); 
    
   
    return {
    'statusCode': statusCode, #"200",
    'body': json.dumps('Thomas R'),
    'headers': {
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Allow" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Headers" : "*"
    }
}