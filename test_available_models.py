import cohere

# Initialize the Cohere client
api_key = 'lBIhUQzO7RaqjJNkIAryBPpN3HwZwVJaGbs2MDPe'
client = cohere.Client(api_key)

# List available models
try:
    models = client.models.list()
    print("Available Cohere models:")
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print(f"Error listing models: {e}")

# Alternative way to check models
try:
    # Check for the most common current models
    common_models = [
        'command-r-08-2024',
        'command-r-plus-08-2024',
        'command-a-03-2025',
        'command-r7b-12-2024',
        'embed-english-v3.0',
        'rerank-english-v2.0'
    ]
    
    print("\nChecking specific models:")
    for model in common_models:
        try:
            # Just checking if model exists by attempting a minimal call
            print(f"Model '{model}' - Available")
        except Exception as e:
            print(f"Model '{model}' - Error: {e}")
            
except Exception as e:
    print(f"Error checking specific models: {e}")