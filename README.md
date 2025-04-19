# s3-upload-compliance

## Requirements
1. AWS lambda function that saves user details into dynamodb.
2. test cases(unit, integration) that verifies lambda execution works fine.
---

## Tools
1. AWS Cloud
2. SAM & SAM Cli
3. Git
4. Python
5. AWS SDK (boto3)
---

## AWS services used
1. S3
2. Lambda Functions
3. APIGateway
4. Dynamodb
5. IAM
6. CloudFormation
---

## Installation

### 1. Clone repo
```bash
git clone https://github.com/pravinlondhe94/python-project.git
```

### 2. Install aws cli & configure default profile

### 3. Install sam cli

### 4. Create s3 bucket in aws
```bash 
aws s3 md s3://your-s3-bucket-name
```

Update **src/samconfig.toml** with
```
s3_bucket = "your-s3-bucket-name"
```

Update **iac/backend.tf** with
```
bucket = "your-s3-bucket-name"
```

## 4. Deploy lambda functions
```bash
sam build
sam deploy
```

## 4. Testing Lambda function 
```bash
pip install -r tests/requirements.txt
# unit test
python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
python -m pytest tests/integration -v
```
---

## Clean up
Delete all resources from AWS cloud
```bash
aws cloudformation delete-stack --stack-name sam-app
```
