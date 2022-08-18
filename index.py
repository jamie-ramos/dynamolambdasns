import boto3
import os


topic_arn = os.environ["TOPIC_ARN"]
    
def lambda_handler(event, context):    
    client = boto3.client('sns')
    message = "This is a test notification for SNS triggered by Lambda triggered by DynamoDB."
    
    response = client.publish(
        TopicArn = topic_arn,
        Message = message ,
        Subject='Hello, something has been added to DynamoDB.'
    )