import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CS321-User-Table')

def lambda_handler(event, context):
    
    print('Getting all Schedules')
    
    response_table = table.scan()
    print(response_table)
    
    schedules_list =[]
    for item in response_table['Items']:
        schedules_list.append(item['name'])
        
    print(schedules_list)
    return {
    'statusCode': '200',
    'body': json.dumps(schedules_list),
    'headers': {
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Allow" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Headers" : "*"
    }
}