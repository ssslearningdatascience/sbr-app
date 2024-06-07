from fastapi import FastAPI
from fastapi.responses import JSONResponse
from cfenv import AppEnv

app = FastAPI(
    title="Sample FastAPI Project",
    description= "This is a simple FastAPI routers creation",
    version="0.01",
    docs_url="/",
    )
env = AppEnv()

@app.get("/health")
async def root():
    return JSONResponse({"message": "Welcome to the FastAPI"}, status_code=200)

@app.get("/{name}")
async def get_name(name):
    return JSONResponse({"name": name}, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app', host="192.168.0.124", port=8082,reload=True)