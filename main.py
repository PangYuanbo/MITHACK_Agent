import FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Teacher_end import New_project
app = FastAPI()
@app.post("/Newproject/")
def Newproject(
        Content: str
):
    project = New_project(Content)
    return {"AI Return": project}