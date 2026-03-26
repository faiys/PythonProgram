# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate
# from pydantic import BaseModel

# class UserInfo(BaseModel):
#     name:str
#     email:str

# SYSTEMPROMT = """"
# You are an intelligent AI assistant designed to help users with general questions, technical problems, and guidance.

# Your goals:
# - Be helpful, accurate, and concise.
# - Prefer practical, actionable answers.
# - For programming questions, provide correct and runnable code.
# - For ambiguous questions, ask a brief clarifying question.
# - If you do not know the answer, clearly say so.

# Response style:
# - Friendly but professional tone.
# - Structured when helpful (steps, bullets, code blocks).
# - Avoid unnecessary verbosity.
# - Use the conversation history to maintain context.

# Safety:
# - Never invent facts.
# - Avoid unsafe or harmful instructions.
# """

# llm = ChatOllama(
#     model="qwen2.5:7b",
#     temperature=0.2,
#     streaming=True,
#     num_predict=200
# )

# promt = ChatPromptTemplate.from_messages(
#     [
#         ("system", SYSTEMPROMT),
#         ("human", "{user_input}")
#     ]
# )

# structure_list = llm.with_structured_output(UserInfo)
# chain = promt | structure_list
# resp = chain.invoke(
#     {
#         "user_input":"My name is Faiyas and email is faiyas@test.com"
#     }
# )
# print(resp)
# # for chunk in chain.stream("User name is test@gmail.com. The ID is 123. I want ti json format"):
# #     print(chunk,end="", flush=True)


API_KEY = "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"
from openai import OpenAI
 
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
 
response = client.chat.completions.create(
    model="anthropic/claude-3.7-sonnet",
    messages=[
        {"role": "user", "content": "Are you Fool?"}
    ],
    temperature=0.3,
    max_tokens="500"
)
 
print(response.choices[0].message.content)