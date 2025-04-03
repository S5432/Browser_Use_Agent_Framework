import os
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig,Controller
# from browser_use import Agent
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
load_dotenv()

import asyncio



# class Post(BaseModel):
#     caption: str
#     url: str


# class Posts(BaseModel):
#     posts: List[Post]

class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int

class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)


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

# link : https://docs.browser-use.com/customize/agent-settings
initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
# 	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
# 	{'scroll_down': {'amount': 1000}},
 ]

async def main():
	task = 'Go to hackernews show hn and give me the first  5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller,browser=browser, initial_actions=initial_actions)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')


if __name__ == '__main__':
	asyncio.run(main())


