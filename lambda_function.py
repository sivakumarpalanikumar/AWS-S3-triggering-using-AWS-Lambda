import boto3

def lambda_handler (event, context):
    s3_user=boto3.client('s3')
    file=s3_user.list_objects (Bucket='')['Contents'][0]['Key']
    print(file) 
    sns_user=boto3.client('sns')
    response=sns_user.publish(
    TopicArn='arn:aws:sns:us-east-1:128959570200:email-notify', 
    Message="Processing of "+ file+" is completed",
    Subject='53 Alert !!!',)
    return
