import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = os.getenv("GEMINI_API_KEY"),
    temperature = "0.7"
)

response = llm.invoke("explain the quantum computing in 5 lines")
print(response.text)
