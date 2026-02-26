import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_APIKEY")
)

try:

    response = client.responses.create(
    model="gpt-5.2",
    input="what is biggest river in this world?",
    store=True,
    temperature=0.3,
    max_output_tokens=100
    )
    print(response)
# print(response.output_text)
except Exception as e:
    print(e)
