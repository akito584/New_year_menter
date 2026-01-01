
import google.generativeai as genai
import os
import sys

# Add /app to sys.path if needed, though we are just running a script
# Get key from env
api_key = os.environ.get("GEMINI_API_KEY")
print(f"Checking API Key: {api_key[:5]}...{api_key[-5:] if api_key else 'None'}")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    sys.exit(1)

genai.configure(api_key=api_key)

try:
    print("Attempting to connect to Gemini API...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hello, can you hear me?")
    print("Success! Gemini response:")
    print(response.text)
except Exception as e:
    print("\n---------- ERROR DETAILS ----------")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("-----------------------------------")
    import traceback
    traceback.print_exc()
