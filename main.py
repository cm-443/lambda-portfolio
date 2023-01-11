import datetime

def lambda_handler(event, context):
    print(datetime.datetime.utcnow() + datetime.timedelta(minutes=30))
    print("text")