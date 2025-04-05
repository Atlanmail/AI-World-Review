from langchain_google_genai import ChatGoogleGenerativeAI

'''
    LLM to use
'''

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)