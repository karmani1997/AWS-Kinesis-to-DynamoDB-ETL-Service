import base64
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lot-numbers')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the payload of the Kinesis record
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        lot_number = data['lot_number']
        
        response = table.get_item(
            Key={
                'lot_number': lot_number
            }
        )
    
        if 'Item' not in response:
            table.put_item(
                Item={
                    'lot_number': lot_number,
                    'count': 1
                }
            )
        else:
            table.update_item(
                Key={
                    'lot_number': lot_number
                },
                UpdateExpression='SET #count = #count + :val',
                ExpressionAttributeNames={
                    '#count': 'count'
                },
                ExpressionAttributeValues={
                    ':val': 1
                }
            )
            
    return {
        'statusCode': 200,
        'body': json.dumps('Product counts processed successfully')
    }

