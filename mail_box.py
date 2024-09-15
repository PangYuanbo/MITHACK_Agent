import asyncio

from uagents import Agent, Bureau, Context, Model
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


class Message(Model):
    message: str


def Send_message(content: str,port:int):
    endpoint = f"http://localhost:{port}/submit"
    agent_1 = Agent(name="agent_1", seed="agent_1 recovery phrase", port=port, endpoint=endpoint)
    ALICE_ADDRESS = os.getenv("Student1_address")

    @agent_1.on_event("startup")
    async def send_message(ctx: Context):
        await ctx.send(ALICE_ADDRESS, Message(message=content))


    # agent_2 = Agent(name="agent_2", seed="agent_2 recovery phrase", port=8002, endpoint="http://localhost:8002/submit")
    #
    # ALICE_ADDRESS = os.getenv("Student2_address")

    # @agent_2.on_interval
    # async def send_message(ctx: Context):
    #     await ctx.send(ALICE_ADDRESS, Message(message=content))
    #     ctx.unregister(send_message)
    #
    # agent_3 = Agent(name="agent_3", seed="agent_3 recovery phrase", port=8003, endpoint="http://localhost:8003/submit")
    #
    # ALICE_ADDRESS = os.getenv("Student3_address")
    #
    # @agent_3.on_interval
    # async def send_message(ctx: Context):
    #     await ctx.send(ALICE_ADDRESS, Message(message=content))
    #     ctx.unregister(send_message)

    agent_1.run()
    loop = asyncio.get_event_loop()
    loop.create_task(agent_1.run_async())
    # agent_2.run()
    # agent_3.run()


# Send_message('''
# {
#     "project": {
#         "content": "{\n  \"estimated_time\": \"2 hours\",\n  \"deadline\": \"2024-09-18T23:59:00\",\n  \"project_summary\": \"This project involves learning how to use Canvas, focusing on its features and functionalities to successfully complete the assignment by the given deadline.\"\n}",
#         "role": "assistant",
#         "function_call": null,
#         "tool_calls": null,
#         "refusal": null
#     }
# }''')
