#####################https://www.youtube.com/watch?v=zGkVKix_CRU#######################
import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Provide me the top 5 posts from Hacker News",
        llm=llm,
        use_vision=False,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())