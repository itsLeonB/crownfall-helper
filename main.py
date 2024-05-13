import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = pd.read_csv("data.csv")


class Token(BaseModel):
    tokens: List[str]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/heroes")
def return_heroes(token: Token):
    result = data[
        data[["token1", "token2", "token3"]].isin(token.tokens).sum(axis=1) >= 2
    ]
    return result["name"].tolist()
