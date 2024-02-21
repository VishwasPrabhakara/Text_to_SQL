from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX,_mysql_prompt
from langchain.prompts.prompt import PromptTemplate
import os

from few_shots import few_shots

from dotenv import load_dotenv
load_dotenv()

def get_few_shot_db_chain():

    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)

    db_user = "root"
    db_password = "Vishwas%401403"
    db_host = "localhost"
    db_port = 3306  # Replace with the correct port number
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", sample_rows_in_table_info=3)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


    vectorize = [f"{example['Question']} {example['SQLQuery']} {example['SQLResult']}" for example in few_shots]
    vectorstore = Chroma.from_texts(vectorize, embedding=embeddings, metadatas=few_shots) #Generate  a vector store , job is to takke input question convert into emebeddings annd pull up similar few shots
    example_selector =SemanticSimilarityExampleSelector(
    vectorstore= vectorstore,
    k=2)

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer"],
    template="\nQestion : {Question}\nSQL Query : {SQLQuery}\nSQL Result : {SQLResult}\nAnswer : {Answer}")

    few_shots_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prompt_suffix=PROMPT_SUFFIX,
        input_variables=["input","table_info","top_k"],)

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt = few_shots_prompt) 
    return chain

if __name__ =="__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("How many total t shirts are left in total in stock")) 


