from huggingface_hub import InferenceClient

def generate_recommendations(skin_issues):
    client = InferenceClient(token="YOUR_HF_TOKEN")
    
    prompt = f"""Act as an expert dermatologist. Given these skin concerns: {skin_issues}, 
    create a skincare routine with products available in India under ₹1000. Follow this format:
    
    Morning:
    1. Cleaner: [Product Name] (₹price) - [Brief Benefit]
    2. Moisturizer: ...
    
    Evening:
    1. ...
    
    Products must be from Nykaa/Amazon/Pharmeasy. Include direct purchase links."""
    
    response = client.text_generation(
        prompt,
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        max_new_tokens=400
    )
    
    return response