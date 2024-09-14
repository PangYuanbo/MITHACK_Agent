from uagents import Agent, Context, Model


class Prompt(Model):
    context: str
    text: str


class Response(Model):
    text: str

def New_project(Content):
    agent = Agent(
        name="user",
        endpoint="http://localhost:8000/submit",
    )


    AI_AGENT_ADDRESS = "agent1qvyrg0578tm2ekua44gnyqmgf99wemp4q8mamatvkg5kvgepsh2fz3e24xk"




    prompt = Prompt(
        type="json_object",
        context="Please estimate the time need for the the following Project: and The Summary of the Project is: ",
        text=Content,
    )


    @agent.on_event("startup")
    async def send_message(ctx: Context):
        await ctx.send(AI_AGENT_ADDRESS, prompt)


    @agent.on_message(Response)
    async def handle_response(ctx: Context, sender: str, msg: Response):
        ctx.logger.info(f"Received response from {sender}: {msg.text}")


