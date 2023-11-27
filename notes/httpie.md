pip install fastapi
pip install uvicorn
pip install httpie

### Basic web
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", port=80, reload=True)
```


```
$ http localhost/hi
HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Fri, 22 Sep 2023 17:59:47 GMT
server: uvicorn

"Hello? World?"
```
note: **We will change only the @app**
httpie note:
```
http HOST who==sang => curl HOST?who=sang
http HOST who=sang  => curl -d '{ "who": "sang" }' HOST
http HOST who:sang  => curl -H 'who: sang' HOST
```

### Path: The URL
```
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"
```
Test
```
$ http -v localhost/hi/sang
GET /hi/sang HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Fri, 22 Sep 2023 18:17:03 GMT
server: uvicorn

"Hello? sang?"
```

### Query: The query parameters (after the ? at the end of the URL)
```
@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"
```
Test
```
$ http -v localhost/hi who==sang 
GET /hi?who=sang HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Fri, 22 Sep 2023 18:15:44 GMT
server: uvicorn

"Hello? sang?"
```

### Body: The HTTP body
```
from fastapi import FastAPI, Body
...
@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}?"
```
Test
```
$ http -v localhost/hi who=sang 
POST /hi HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 15
Content-Type: application/json
Host: localhost
User-Agent: HTTPie/3.2.2

{
    "who": "sang"
}


HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Fri, 22 Sep 2023 18:14:57 GMT
server: uvicorn

"Hello? sang?"
```

### Header: The HTTP headers
**Basic header**
```
from fastapi import FastAPI, Header
...
@app.get("/hi")
def greet(who:str = Header()):
    return f"Hello? {who}?"
```
Test
```
$ http -v localhost/hi who:sang
GET /hi HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost
User-Agent: HTTPie/3.2.2
who: sang



HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Fri, 22 Sep 2023 18:18:34 GMT
server: uvicorn

"Hello? sang?"
```
**Get header**
```
from fastapi import FastAPI, Header
...
@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent
```
Test
```
$ http -v POST localhost/agent
POST /agent HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 0
Host: localhost
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Fri, 22 Sep 2023 18:22:57 GMT
server: uvicorn

"HTTPie/3.2.2"
```