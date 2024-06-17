from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import processing

tabs = {}
class Item(BaseModel):
    url: str
    title: str
    body: str
    tabID: int



app = FastAPI()
@app.post("/")
async def root():
    return {"https://www.reddit.com/r/samharris/comments/15v58oi/eliezer_yudkowsky_worth_taking_serious_yes_or_no/": tabs["https://www.reddit.com/r/samharris/comments/15v58oi/eliezer_yudkowsky_worth_taking_serious_yes_or_no/"]}

#takes ina json object and stores it as a key value in a dictionary
@app.post("/store")
async def store(item: Item):
    tabs[item.tabID] = item
    return item

#procceses the dict and returns the values

@app.get("/process")
async def process():
    proccessed = processing.run_model(tabs)
    return proccessed

#deletes everything in the dictionary
@app.get("/delete")
async def delete():
    tabs.clear()
    return tabs
    
    
