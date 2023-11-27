from fastapi import FastAPI
from fastapi import Header
from fastapi import Body
from fastapi import Response

from model.tag import TagIn, Tag, TagOut
import service.tag as service

app = FastAPI()

## basic ops ##
@app.get("/hi")
def greet(who):
    return f"query param {who}?"

@app.get("/hi")
def greet():
    return "Hello? World?"

@app.get("/hi/{who}")
def greet(who):
    return f"path {who}?"

@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Body {who}?"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body"

@app.post("/agent")
def get_agent(user_agent:str = Header(), a:str = Header()):
    return f"{user_agent} + {a}"

@app.get("/happy", status_code=302)
def happy():
    return ":)"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", host="0.0.0.0",port=80, reload=True)