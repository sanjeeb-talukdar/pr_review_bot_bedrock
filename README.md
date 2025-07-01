# GitHub PR Review Bot using Amazon Bedrock & S3 Guidelines

## 🔍 Overview
A serverless Python bot that reviews GitHub pull requests using coding guidelines stored in Amazon S3 and AI models from Amazon Bedrock.

## 🚀 Features
- Fetches PR diffs from GitHub
- Loads review rules from S3 (exported from Confluence)
- Uses Claude (via Bedrock) for intelligent review
- Posts comments back on GitHub PR

## 🛠️ Deployment
1. Deploy with [Serverless Framework](https://www.serverless.com/)
2. Ensure IAM permissions for:
   - S3: `s3:GetObject`
   - Bedrock: `bedrock:InvokeModel`
   - GitHub Token access via Secrets Manager or Env vars

## 🧪 Test Locally
```bash
pytest tests/
```

## 📂 Folder Structure
```
pr_review_bot/
├── lambda/handler.py
├── utils/github.py, s3_loader.py, prompt_builder.py
├── bedrock_client.py
├── prompts/
├── sample_guidelines/
├── sample_events/
├── tests/
├── Dockerfile
├── serverless.yml
├── requirements.txt
├── README.md
```

## 📬 Author
**Sanjib Talukdar**  
[GitHub](https://github.com/sanjeeb-talukdar) | [LinkedIn](https://www.linkedin.com/in/sanjeeb-talukdar/)
