import boto3

def lambda_handler(event, context):
   dynamodb_resource = boto3.resource("portfolio-db")
   table = dynamodb_resource.Table("table")
   response = table.put_item(
       Item={
           "contactName": event["contactName"],
           "contactEmail": event["contactEmail"],
           "contactSubject": event["contactSubject"],
           "contactMessage": event["contactMessage"],
       }
   )

#html
#var desc = $("#description-input").val();