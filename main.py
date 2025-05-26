import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = os.getenv("GEMINI_API_KEY"),
    temperature = 0.7 )

# response = llm.invoke("explain the quantum computing in 5 lines")
# print(response.content)

# template = """
# you are an assistant. Answer the question clearly and precisely 
# Question = {question}
# Answer: 
# 
# """
# prompt = PromptTemplate(

#     input_variables=["question"],
#     template= template 
#)

# formatted_prompt = prompt.format(question = "what is quantum physics")

# response = llm.invoke(formatted_prompt)
# print(response.content)



advance_template = """
    you are a {Role} expert.
    Context: {Context}
    Task: {Task}
    Please provide a {Style} response
    Input:{Input}         
    """

advance_prompt = PromptTemplate(
    input_variables=["Role","Context","Task","Style","Input"] ,
    template=advance_template 
)

# using the chain we need to change the code in order to use the chain method

#  advance_format = advance_prompt.format(
#     Role = "Python Programming",
#     Context = "Teaching a beginner",
#     Task = "Explain the concept",
#     Style = "Friendly and Understanding",
#     Input = "What are functions?"
# )

# response = llm.invoke(advance_format)
# print(response.content)


chain = LLMChain(llm = llm, prompt = advance_prompt)
response  = chain.run(
   Role = "Python Programming",
    Context = "Teaching a beginner",
    Task = "Explain the concept",
    Style = "Friendly and Understanding",
    Input = "What are functions?" 
)
print(response)
