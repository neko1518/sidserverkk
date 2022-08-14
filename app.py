import json
import urllib.request
from fastapi import FastAPI, Request
import json
from fastapi.responses import JSONResponse
import uvicorn
import sidserver

app="ccip"
key="967e107a-b0cf-45fe-8dbe-886a0fb0d6a2"

client=sidserver.Client(app_name=app,key=key)        
app = FastAPI()

@app.get('/')
async def get_webpage():
    return "Sid server"
    
@app.get('/reset')
async def ress():
    return "restarted"



@app.post("/{comId}/send-active-obj/{sid}")
async def submit_report(request: Request):
    body = await request.json()
    data=body["data"]
    client.login_sid(sid)
    server=client.sendActive(comId,data)
    return server
