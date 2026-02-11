
import argparse
import os
import requests
import json
import base64

# --- Argument Parsing ---
ap = argparse.ArgumentParser(description="Generate an image via ZenMux API.")
ap.add_argument("--prompt", required=True, help="Text prompt for the image.")
ap.add_argument("--model", default="google/gemini-2.5-flash-image", help="The model to use for generation.")
ap.add_argument("--output", default="generated_image.png", help="Output file name for the image.")
args = ap.parse_args()

# --- API Configuration ---
api_key = os.environ.get("ZENMUX_API_KEY")
base_url = "https://zenmux.ai/api/vertex-ai"

if not api_key:
    print("Error: ZENMUX_API_KEY environment variable is not set.")
    exit(1)

# --- Image Generation Logic ---
try:
    print(f"Starting image generation with model: {args.model}")
    url = f"{base_url}/v1/models/{args.model}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": args.prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"]
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    print(f"Request sent. Response status code: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        if "candidates" in result and result["candidates"]:
            for candidate in result["candidates"]:
                if "content" in candidate and "parts" in candidate["content"]:
                    for part in candidate["content"]["parts"]:
                        if "inlineData" in part and "data" in part["inlineData"]:
                            print("Image data found in response.")
                            image_data = base64.b64decode(part['inlineData']['data'])
                            with open(args.output, "wb") as f:
                                f.write(image_data)
                            print(f"Success! Image saved to: {args.output}")
                            exit(0) # Success
        print("Error: Image data not found in the successful response.")
    else:
        print(f"Error: API returned status {response.status_code}")
        print(f"Response body: {response.text}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# If we reach here, it means something went wrong
exit(1)
