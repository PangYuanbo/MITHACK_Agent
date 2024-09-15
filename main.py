
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from Teacher_end import new_project
from mail_box import Send_message
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 定义请求体模型
@app.post("/Newproject/")
async def Newproject(request: Request):
    data = await request.json()  # 直接从请求体中解析 JSON 数据
    content = data.get("Content")
    project = await new_project(content)
    print(project)
    return {"project": project}
@app.post("/Newproject/")
async def Newproject(
        Content: str
):
    project =await new_project(Content)
    print (project)
    return {"project": project}

@app.post("/UploadToMailbox/")
def UploadToMailbox(
        Content: str
):
    Send_message(Content)
    return {"Message sent to all students"}
