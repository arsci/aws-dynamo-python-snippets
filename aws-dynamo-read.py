import boto3, uuid, json, decimal

dynamoTableName = 'TABLE_NAME_HERE'
itemKeyToQuery = 'ITEM_KEY_TO_QUERY_HERE'

## Setup DynamoDB params
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table(dynamoTableName)

## Query params
obj = {
  "id": itemKeyToQuery
}

## Run the query
response = table.get_item(Key=obj)

## Response
print(response)