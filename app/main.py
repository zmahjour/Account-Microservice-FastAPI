from fastapi import FastAPI
import uvicorn
from api.api_v1.api import router as account_router


app = FastAPI()
app.include_router(account_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
