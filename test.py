import json
import time
import boto3
from botocore.exceptions import ClientError
from flask import jsonify

def send():
    user_id = '3220daa3-9d01-48e3-bf83-75087f07761f'
    job_id = '38b236bf-b692-4965-922f-f6ddfb2fd230'

    data = { "job_id": str(job_id), 
                "user_id": str(user_id),
                "complete_time": int(time.time()),
            }
    sns_topic = 'arn:aws:sns:us-east-1:127134666975:chakradhar_a12_job_results'
    # todo error handling
    sns = boto3.resource('sns',region_name='us-east-1')
    topic = sns.Topic(sns_topic)
    try:
        response = topic.publish(Message=str(data))
    except ClientError as err:
        print("hello")

    print(response)
    #   app.logger.error(f'Unable to send a notification to SNS queue {err}')
    #   return abort(500)



def send_email_ses(recipients=None, sender=None, subject=None, body=None):

    ses = boto3.client('ses', region_name='us-east-1')

    try:
        response = ses.send_email(
            Destination = {
            'ToAddresses': (recipients if type(recipients) == "list" else [recipients])
            },
            Message={
            'Body': {'Text': {'Charset': "UTF-8", 'Data': body}},
            'Subject': {'Charset': "UTF-8", 'Data': subject},
            },
            Source=(sender or 'chakradhar@ucmpcs.org'))
    except ClientError as e:
        raise e

    return response



sqs_url = "https://sqs.us-east-1.amazonaws.com/127134666975/chakradhar_a12_job_results"
def start_polling():
    sqs = boto3.client('sqs',region_name='us-east-1')
    
        # todo error handling
    response = sqs.receive_message(QueueUrl=sqs_url
                ,MaxNumberOfMessages=1
                ,MessageAttributeNames=['All']
                ,WaitTimeSeconds=20)


    if 'Messages' in response.keys():
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        params = message['Body']
        print(params)
        params = json.loads(json.loads(params)['Message'].replace("'", '"'))
        job_id = params['job_id']
        base_url = "http://localhost:5000/job/"
        url = base_url + 'annotations/' + str(job_id)
        complete_time = params['complete_time']
        print("procssing request")
        sub = "Results available for job " + str(job_id)
        email_body =  "Your annotation job completed at " + str(complete_time) +". Click here to view job details and results: " +str(url) 
        send_email_ses(subject=sub, body=email_body,recipients='chakradhar@uchicago.edu')
        # todo error handling
        # sqs.delete_message(QueueUrl=sqs_url,ReceiptHandle=receipt_handle)
        

send()
start_polling()