import boto3
import os

# Create an SQS client
sqs = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL'] # Supplied by Function service-discovery wire

def handler(message, context):

  # Send a new message/job to the specified SQS Queue
  response = sqs.send_message(
      QueueUrl=queue_url,
      MessageBody='this is a second job'
  )
  return response