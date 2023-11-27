from fastapi import FastAPI, Depends, Query

app = FastAPI()

# the dependency function:
def user_dep(name: str = Query, password: str = Query):
    return {"name": name, "valid": True}

def check_dep(name: str = Query, password: str = Query):
    print(name)
    if not name:
        raise

# the path function / web endpoint:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

@app.get("/user1")
def get_user(user1):
    return user1

# the path function / web endpoint:
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True