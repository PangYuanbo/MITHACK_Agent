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
        #content = "Please estimate the time needed for the following project and return the output as a JSON object with three keys: 'estimated_time', 'deadline', and 'project_summary'. The Summary of the Project is:"
        
        content = """
        The current date is 2024-09-15,
        
        Please provide an accurate estimate for an experienced professor with all prerquisite materials, documentation and formulas to complete the following assignment in a very rushed and informal way without any planning, testing, validation, verification or quality assurance. Assume the professor needs no time for brainstorming, sketching, prototyping, setup or preparation, and can work continuously without breaks. Assume the assignment comes with a step by step guide to the problem. 
        
        Your response should be a JSON object with three keys: 
        1. 'estimated_time' (the estimated duration to complete the assignment in terms of continuous work time, e.g., "1030" hours or "24 hours" or "1 second"; cannot be after the deadline),
        2. 'deadline' (the proposed deadline for the assignment, e.g., "2024-10-01"),
        3. 'estimation explanation' (justify in depth why the estimate is correct).
        """
        
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