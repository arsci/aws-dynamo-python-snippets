import boto3, uuid, json, decimal

dynamoTableName = 'TABLE_NAME_HERE'

## Setup DynamoDB params
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table(dynamoTableName)

## The item to add to dynamo
obj = {
  "id": str(uuid.uuid4()), ## Always use a UUID as the key
  "att1": "key1", ## String attribute
  "att2": decimal.Decimal(1126.564854) ## Decimal attribute
}

## Put the item
response = table.put_item(Item=obj)

## Response
print(response)

## Dynamo Class for converting numbers to dynamo decimal data type
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
