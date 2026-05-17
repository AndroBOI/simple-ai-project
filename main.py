from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents="Explain how machine learning works. Write a detailed, comprehensive explanation.",
)
for chunk in response:
    print(chunk.text, end="")
