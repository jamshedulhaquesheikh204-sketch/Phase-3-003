import cohere
import os

# Use the API key from environment or the provided one
api_key = os.getenv("COHERE_API_KEY", "lvtEngtl7zyrJnydMS3G48k5636PFO6ShfeRSiAV")

try:
    client = cohere.Client(api_key)
    print("Client created successfully")

    response = client.chat(
        model='command-r-08-2024',  # Updated to use current model as command-r was removed
        message='Hello, how are you?',
    )
    print('Response received')
    print('Text:', response.text)

except Exception as e:
    print('Error occurred:', str(e))
    import traceback
    traceback.print_exc()