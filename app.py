from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from cfenv import AppEnv

class NameRequest(BaseModel):
    name: str

app = FastAPI(
    title="Sample FastAPI Project",
    description= "This is a simple FastAPI routers creation",
    version="0.01",
    docs_url="/",
    )
env = AppEnv()

@app.get("/health")
async def root():
    return JSONResponse({"message": "Welcome to the FastAPI Application"}, status_code=200)

@app.post("/factorial/{n}")
async def factorial(n: int):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    print("factorial of {n} is",fact)
    return JSONResponse({"result":fact})
        

@app.get("/{name}")
async def get_name(name):
    return JSONResponse({"name": name}, status_code=200)



@app.post("/name")
async def post_name(request: NameRequest):
    print("chandana")
    return JSONResponse({"name": request.name}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app', port=8082, reload=True)