config = {
    "base_url": 'https://api.chatfire.cn/v1',
    "api_key": 'sk-zO8exlBicZh7nJeZn5GuC5X9SPuVrZzXoGyOW0i9BFvN62ON'
}

from pydantic import BaseModel
import agents
from typing import List


class UserStory(BaseModel):
    role: str
    goal: str
    value: str

class StoryCollection(BaseModel):
    items: List[UserStory]

agent = agents.Agent(
    name="User Story Generator",
    instructions="You are a project manager for a supermarket management system, and you need to analyze and generate standard user stories based on actual scenarios.",
    output_type=StoryCollection,
    model="gpt-4o",
)

async def main():
    result = await agents.Runner.run(
        starting_agent=agent,
        input="generate many user storys",
    )
    print(result.final_output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # 使用正确的asyncio运行方式