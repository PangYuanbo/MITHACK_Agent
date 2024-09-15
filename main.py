
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Teacher_end import New_project
from mail_box import Send_message
app = FastAPI()
@app.post("/Newproject/")
def Newproject(
        Content: str
):
    project = New_project(Content)
    return { project}

@app.post("/UploadToMailbox/")
def UploadToMailbox(
        Content: str
):
    Send_message(Content)
    return {"Message sent to all students"}
