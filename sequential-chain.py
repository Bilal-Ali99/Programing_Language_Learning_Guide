
# # Chain 1: Generate A road map of learning python
# roadmap_template = """Create a Short road map {Input} for {Role} Programing."""
# roadmap_prompt = PromptTemplate(input_variables=["Input", "Role"], template=roadmap_template)
# print("ROAD MAP PROMPT: ",roadmap_prompt)
# roadmap_chain = LLMChain(llm=llm, prompt=roadmap_prompt, output_key="roadmap")

# # Chain 2: Generate a plan to follow the roadmap
# plan_template = """Create a plan for following the roadmap: {roadmap}"""
# plan_prompt = PromptTemplate(input_variables=["roadmap"], template=plan_template)
# print("PLAN PROMT: ",plan_prompt)
# plan_chain = LLMChain(llm=llm, prompt=plan_prompt, output_key="plan")

# # Chain 3: Estimate preparation time
# time_template = """Estimate the total time it will take to complete: {plan}"""
# time_prompt = PromptTemplate(input_variables=["instructions"], template=time_template)
# print("TIME PROMT: ",time_prompt)
# time_chain = LLMChain(llm=llm, prompt=time_prompt, output_key="time_estimate")

# # Combine all chains
# overall_chain = SequentialChain(
#     chains=[roadmap_chain, plan_chain, time_chain],
#     input_variables=["Input", "Role"],
#     output_variables=["roadmap", "plan", "time_estimate"],
#     verbose=True
# )

# # Run the chain
# result = overall_chain({"Input": "Roadmap", "Role": "Python"})
# print(result)


