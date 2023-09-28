from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os


os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)


def generate_small_business_name_and_services(small_business):

    # Chain 1: Small Business Name
    prompt_template_name = PromptTemplate(
        input_variables=['small_business'],
        template="I want to open a {small_business}. Suggest 5 fancy names for this and please use one word or comma separated name for each busines ."
    )

    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="Business_name")

    # Chain 2: Define prompt template for services/items
    prompt_template_items = PromptTemplate(
        input_variables=['Business_name'],
        template="""Suggest 5 itemize services for {Business_name} and if food services, menu items, otherwise retail items. Names need to be single or comma-separated"""
    )

    # Define chain for services/items
    services_chain = LLMChain(
        llm=llm, prompt=prompt_template_items, output_key="Itemize_Services")

    # Define Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, services_chain],
        input_variables=['small_business'],
        output_variables=['Business_name', "Itemize_Services"]
    )

    # Run the chain
    response = chain({'small_business': small_business})
    return response


if __name__ == "__main__":
    response = generate_small_business_name_and_services("Boutique")
    print(response)
