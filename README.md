# Please find task 1 code under `task1` folder and task 2 pdf attached under `task2`.


## TASK 1 - Kinesis-to-DynamoDB Lambda Function
This Lambda function is designed to process Kinesis data and update a DynamoDB table with product counts. The function is triggered by a Kinesis stream, and it expects the data in the stream to be in JSON format, with a lot_number field representing the product.

## Requirements
* Serverless framework
* AWS account
* Kinesis stream with data in JSON format
* DynamoDB table with a partition key of lot_number
* IAM role with permissions to access Kinesis and DynamoDB

## Install dependencies
Install necessary npm packages to run sls deployment commands in next section.

``` 
cd task1
npm install
```

## Deployment
To deploy the lambda function on aws using the following command.

``` 
sls deploy
```


## Testing
We can trigger aws kinesis via an api but for the sake of demonstration, I will be using below given command in the next step of feedback call.

```
aws kinesis put-record --stream-name myStream --data '{"lot_number": "62211540"}' --partition-key 1 --region us-east-1
```

