import uvicorn
from fastapi import FastAPI
from server.api import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
