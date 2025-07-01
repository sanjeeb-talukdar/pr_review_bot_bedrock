from utils.github import fetch_diff, post_comments
from utils.s3_loader import load_guidelines
from utils.prompt_builder import build_prompt
from bedrock_client import invoke_model, parse_response

def handler(event, context):
    pr_number = event['pull_request_number']
    repo = event['repository']
    github_token = event['github_token']

    guidelines = load_guidelines(
        bucket='my-review-guidelines-bucket',
        key='guidelines/latest-guidelines.md'
    )
    diff = fetch_diff(repo, pr_number, github_token)
    prompt = build_prompt(guidelines, diff)
    response_text = invoke_model(prompt)
    comments = parse_response(response_text)
    for comment in comments:
        post_comments(repo, pr_number, comment, github_token)
