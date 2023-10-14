from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv


load_dotenv()

def generate_pet_name(pet_type, pet_color):
    llm = OpenAI(temperature=0.7)
    prompt = PromptTemplate(
        input_variables=["pet_type", "pet_color"],
        template="Give me 5 cool names for my pet dog {pet_type} which is of color {pet_color}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt, output_key="pet_names")
    response = chain.run(pet_type=pet_type, pet_color=pet_color)
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.9)

    tools = load_tools(["wikipedia"], llm=llm)

    agent = initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run("What is the average age of a dog? Multiply the result by 3")

    print(result)


langchain_agent()