import boto3

def lambda_handler(event, context):
   dynamodb_resource = boto3.resource("dynamodb")
   table = dynamodb_resource.Table("portfolio-db")
   response = table.put_item(
       Item={
 
          "contactEmail": event["contactEmail"],
          "contactMessage": event["contactMessage"],
          "contactName": event["contactName"],
          "contactSubject": event["contactSubject"],

       }
   )