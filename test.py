from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.2,
    num_predict=200
)

promt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "{user_input}")
    ]
)
chain = promt | llm
resp = chain.invoke(
    {
        "user_input":"i have 4 mango and 6 apple. what i will eat first?"
    }
    )
print(resp.content)