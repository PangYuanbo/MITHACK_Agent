from uagents import Agent, Bureau, Context, Model
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()




class Message(Model):
    message: str

def Send_message(content:str):

    agent_1 = Agent(name="agent_1", seed="agent_1 recovery phrase", port=8001, endpoint="http://localhost:8001/submit")

    ALICE_ADDRESS = os.getenv("Student1_address")

    @agent_1.on_interval
    async def send_message(ctx: Context):
        await ctx.send(ALICE_ADDRESS, Message(message=content))
        ctx.unregister(send_message)

    agent_2 = Agent(name="agent_2", seed="agent_2 recovery phrase", port=8001, endpoint="http://localhost:8001/submit")

    ALICE_ADDRESS = os.getenv("Student2_address")

    @agent_2.on_interval
    async def send_message(ctx: Context):
        await ctx.send(ALICE_ADDRESS, Message(message=content))
        ctx.unregister(send_message)


    agent_3 = Agent(name="agent_3", seed="agent_3 recovery phrase", port=8001, endpoint="http://localhost:8001/submit")

    ALICE_ADDRESS = os.getenv("Student3_address")

    @agent_3.on_interval
    async def send_message(ctx: Context):
        await ctx.send(ALICE_ADDRESS, Message(message=content))
        ctx.unregister(send_message)

    agent_1.run()
    agent_2.run()
    agent_3.run()
