from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import korea_engine

load_dotenv()

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

print(population_df.head())

popluation_query_engine = PandasQueryEngine(df=population_df, 
                                            verbose=True,
                                            instruction_str=instruction_str)
# verbose = True : detailed output
popluation_query_engine.update_prompts({"pandas_prompt": new_prompt})
# popluation_query_engine.query("what is the population of South Korea")

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=popluation_query_engine,
        metadata=ToolMetadata(
        name="population_data",
        description="this gives information about the world popluation and demographics"
        ),
    ),
    QueryEngineTool(
        query_engine=korea_engine,
        metadata=ToolMetadata(
        name="korea_data",
        description="this gives detailed info about korea"
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q": # python 3.9
    result = agent.query(prompt)
    print(result)
