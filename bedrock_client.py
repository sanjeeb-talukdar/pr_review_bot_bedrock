import boto3
import json

def invoke_model(prompt):
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    body = {
        "prompt": prompt,
        "max_tokens_to_sample": 1000,
        "temperature": 0.5
    }
    response = client.invoke_model(
        modelId='anthropic.claude-3-sonnet-20240229',
        body=json.dumps(body)
    )
    return response['body'].read().decode('utf-8')

def parse_response(response_text):
    return response_text.split('\n\n')
