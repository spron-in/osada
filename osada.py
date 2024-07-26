import os
import sys
import sqlalchemy

from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

import chainlit as cl

### get env variables
### set GOOGLE_API_KEY to use google models
### set OPENAI_API_KEY to use openai models
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "gemini")
LLM_CHOICE = os.environ.get("LLM_CHOICE", "")
LLM_TEMPERATURE = os.environ.get("LLM_TEMPERATURE", 0)

DB_TYPE = os.environ.get("DB_TYPE", "postgresql")
DB_USERNAME = os.environ.get("DB_USERNAME", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "localhost")
DB_NAME = os.environ.get("DB_NAME", "")
DB_PORT = os.environ.get("DB_PORT", "5432")


# Conditional LLM Initialization
if LLM_PROVIDER.lower() == "gemini":
    if "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("Using gemini, please set GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model=LLM_CHOICE)
elif LLM_PROVIDER.lower() == "openai":
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("Using openai, please set OPENAI_API_KEY")
    llm = ChatOpenAI(model=LLM_CHOICE,temperature=LLM_TEMPERATURE)
else:
    raise ValueError("Invalid LLM_CHOICE. Use 'gemini' or 'openai'.")

db_uri = f"{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(db_uri)
db = SQLDatabase(engine)

@cl.on_chat_start
async def on_chat_start():

    msg = []
    msg.append("Welcome to OSADA - Open Source AI Database Agent")
    try:
        with engine.connect() as connection:
            connection.execute(sqlalchemy.text("SELECT 1"))
            msg.append(f"Connected to the database {DB_TYPE}://MASKED:MASKED@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}")
            await cl.Message(
                content="""
                
                """.join(msg)
            ).send()    
    except sqlalchemy.exc.OperationalError as e:
        msg.append(f"Connection to database failed: {e}")
        await cl.Message(
            content="""
                
            """.join(msg)
        ).send()

@cl.step(type="db_agent")
async def db_agent(prompt):
    agent_executor = create_sql_agent(llm, db=db, verbose=True)    
    response = agent_executor.invoke({"input": prompt})
    if 'output' in response:
        return response['output']
    else:
        return "Something went wrong"

@cl.on_message
async def on_message(message: cl.Message):
    final_answer = await cl.Message(content="").send()
    final_answer.content = await db_agent(message.content)

    await final_answer.update()