import json
import boto3
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CS321-User-Table')


def lambda_handler(event, context):
    print(event)
    data = json.loads(event['body'])
    status_code = 200
    found = False
    msg = ''
    # Take a username, and put the data in the table.
    table_response = table.scan()
    print(table_response)
    for item in table_response['Items']:
        name1 = item['name'].rstrip()
        name2 = data['user'].rstrip()
        if name1 == name2:
            print('USER FOUND')
            response_item = table.get_item(Key={'user': str(item['user'])})
            print(response_item)
            res = response_item['Item']
            
            res['data'].append(data['events'])
            table.put_item(Item=res)
            status_code = 200
            msg = 'User Found'
            found = True

    
    
    if found == False:
        status_code = '0'
        msg = 'User Not Found'
        
    print(msg)
    # TODO implement
    return {
    'statusCode': str(status_code),
    'body': json.dumps(msg),
    'headers': {
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Allow" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
        "Access-Control-Allow-Headers" : "*"
    }
}