import openai
import asyncio
from openai import OpenAI

# 设置 OpenAI API 密钥

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# # 定义项目的内容


# 发送请求给 OpenAI 的 mini 4o 模型，指定返回 JSON 格式
async def new_project(Content):
    try:
        content = "Please estimate the time needed for the following project and return the output as a JSON object with three keys: 'estimated_time', 'deadline', and 'project_summary'. The Summary of the Project is:"
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": content},
                {
                    "role": "user",
                    "content": Content
                },

            ],
            response_format={"type": "json_object"},
        )

        # 解析 AI 的 JSON 响应
        ai_response=completion.choices[0].message

        # 打印并处理返回的 JSON 数据

        return ai_response

    except Exception as e:
        print(f"Error occurred: {str(e)}")