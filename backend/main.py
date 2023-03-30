from fastapi import FastAPI
from routers import gpt
import uvicorn


app =  FastAPI()

@app.on_event("startup")
async def startup():
    app.include_router(gpt.router)


@app.get('/')
def index():
    return 'Success! APIs are working!'
    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
