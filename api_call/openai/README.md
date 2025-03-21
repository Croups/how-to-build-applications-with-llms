# Getting Started with OpenAI API

## Overview

In this video, I am going to show you how to get an OpenAI API and how to get started with the OpenAI API. The tutorial covers:

1. How to create an OpenAI account
2. How to create a project on OpenAI
3. How to get an API key
4. How to set the API key in your environment
5. How to make your first API call to OpenAI
6. How to write a function for OpenAI calls
7. What are the system roles for OpenAI calls

## Installation

```bash
git clone https://github.com/Croups/how-to-build-applications-with-llms
cd api_call/openai
pip install -r requirements.txt
```

## Setup

1. Go to https://platform.openai.com/
2. Create a project and get your API key
3. Set your environment variable:
   ```
   OPENAI_API_KEY = "your_api_key"
   ```
## Example Code for First API Call

```python
from openai import OpenAI

# Initialize the client with your API key
client = OpenAI(api_key="your-api-key-here")  # Better to use environment variable

# Make a simple completion request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"}
    ]
)

print(response.choices[0].message.content)
```

## Important Notes

- **Security**: Never share your API key publicly or commit it to version control
- **Costs**: Be aware that API usage incurs charges based on token consumption
- **Rate Limits**: There are rate limits for different API tiers
- **Models**: Different models have different capabilities and pricing

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Community Forums](https://community.openai.com/)
- [Pricing Information](https://openai.com/pricing)

---
