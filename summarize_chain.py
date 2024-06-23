from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
langchain_llm = ChatGoogleGenerativeAI(model="gemini-pro")

prompt_template = """Write a concise summary of the following:
        "{string}"
        CONCISE SUMMARY:"""

prompt = PromptTemplate(
        input_variables=["string"],
        template=prompt_template,
)

chain = LLMChain(llm = langchain_llm, prompt = prompt)

if __name__ =="__main__":
    print(chain.run("ice cream"))