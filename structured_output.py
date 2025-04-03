import os
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
# from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',  # Windows path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Write a letter in Google Docs to my Papa, thanking him for good health, and save the document as a PDF",
        llm=llm,
        browser=browser,
    )
    result = await agent.run()
    print(result.extracted_content())  # Print the extracted content from the result
    await browser.close()  # Close the browser after use

asyncio.run(main())