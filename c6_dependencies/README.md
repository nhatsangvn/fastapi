Two ways:
- @app.get("/user", dependencies=[Depends(user_dep)])
- def get_user(user: dict = Depends(user_dep)) -> dict:

```
def user_dep(name: str = Query, password: str = Query):
    return {"name": name, "valid": True}
```


Dependency like a helper, that STORE the return of function to an Argument, to return