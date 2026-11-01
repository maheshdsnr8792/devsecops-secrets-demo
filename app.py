import os

api_key = os.getenv("API_KEY")

if api_key:
    print("API key received successfully")
else:
    print("API key is missing")
Important

We are not writing:

api_key = "my-secret-123"
