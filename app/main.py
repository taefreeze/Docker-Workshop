from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Home():
    return {"Hello" : "API"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80, debug=True)