import json
import urllib.request
from fastapi import FastAPI, Request
import json
from fastapi.responses import JSONResponse
import uvicorn
import sidserver

app=""
key=""

client=sidserver.Client(app_name=app,key=key)        
app = FastAPI()

@app.get('/')
async def get_webpage():
    return "Sid server"
    
@app.get('/reset')
async def ress():
    return "restarted"



@app.post("/{comId}/send-active-obj/{sid}")
async def submit_report(request: Request,comId:int,sid:str):
    body = await request.json()
    client.login_sid(sid)
    server=client.sendActive(comId)
    return server
