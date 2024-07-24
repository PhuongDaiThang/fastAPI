from fastapi import FastAPI #import FastAPI

app = FastAPI() #create a FastAPI "instance"

@app.get("/") #create a path operation
def read_root(): #define the path operation function
    return {"Hello": "Thang"} # return the content
# uvicorn main1_1:app --reload