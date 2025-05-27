from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from main import llm
from langchain.chains import SequentialChain

# Chain 1: Generate a recipe name
recipe_template = """Suggest a detailed recipe for {dish} suitable for {cuisine} cuisine."""
recipe_prompt = PromptTemplate(input_variables=["dish", "cuisine"], template=recipe_template)
recipe_chain = LLMChain(llm=llm, prompt=recipe_prompt, output_key="recipe")

# Chain 2: Generate cooking instructions
instructions_template = """Convert this recipe into step-by-step cooking instructions: {recipe}"""
instructions_prompt = PromptTemplate(input_variables=["recipe"], template=instructions_template)
instructions_chain = LLMChain(llm=llm, prompt=instructions_prompt, output_key="instructions")

# Chain 3: Estimate preparation time
time_template = """Estimate the total preparation and cooking time needed for these instructions: {instructions}"""
time_prompt = PromptTemplate(input_variables=["instructions"], template=time_template)
time_chain = LLMChain(llm=llm, prompt=time_prompt, output_key="time_estimate")

# Combine all chains
overall_chain = SequentialChain(
    chains=[recipe_chain, instructions_chain, time_chain],
    input_variables=["dish", "cuisine"],
    output_variables=["recipe", "instructions", "time_estimate"],
    verbose=True
)

# Run the chain
result = overall_chain({"dish": "pasta", "cuisine": "Italian"})
print(result)