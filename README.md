# AWS-S3-triggering-using-AWS-Lambda
     AWS Services used here,
     1.AWS S3 Bucket
     2.AWS Lambda
     3.AWS Cloudwatch
     4.AWS IAM
     5.AWS SNS
     
 *****************************************************************************************************************************************************************************    
     
     Process:
     
     1.A S3 Bucket has been created using python code instead of GUI.
     2.A file has been uploaded in the bucket.
     3.AWS IAM is used to provide access to other user type.
     4.A Lambda function has been created and python code has been written to trigger an event ie mail has to be sent when a file is uploaded. For that python is chosen and            (all) option is selected to handle any type of requests.
     5.Python code is written inside AWS Lambda for notification purpose.
     6.Here AWS SNS is created to sent e-mail. For that Email protocol is selected.
     7.Also AWS Cloudwatch is used to monitor the process.
