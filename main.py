from fastapi import FastAPI
from pydantic import BaseModel
import random


class Fact(BaseModel):
    id: int
    fact: str


facts_db = [
    Fact(id=1,
         fact="The term ‘psychology‘ has been derived from the Greek word ‘psyche’ translating as ‘breath, spirit, soul’ and ‘logia’ corresponding to ‘study of’."),
    Fact(id=2, fact="It takes about 66 days for an average individual to make something a daily habit."),
    Fact(id=3,
         fact="Studies say that individuals who could instinctively use sarcasm to tackle a frivolous question have healthy minds."),
    Fact(id=4,
         fact="Individuals who have a deep sense of guilt are better at identifying the emotions and concerns of the people around them."),
    Fact(id=5,
         fact="We can udnretsnad any msseed up stnecene as lnog as the lsat and frsit lteerts of wdros are in crrcoet palecs. Suhc as tihs stnecene."),
    Fact(id=6,
         fact="The way an individual treats the employees at an establishment tells immensely about their character. ")
]

app = FastAPI()


@app.get("/")
async def get_all():
    return facts_db


@app.get("/fact")
async def get_random_fact():
    return random.choice(facts_db)


@app.get("/fact?id={id}")
async def get_fact_by_id_v1(id:str | None = None):
    return next((f for f in facts_db if f.id == int(id)), None)


@app.get("/fact/{id}")
async def get_fact_by_id_v2(id):
    return next((f for f in facts_db if f.id == int(id)), None)


@app.post("/add")
async def add_fact(fact: Fact):
    facts_db.append(fact)
    return fact
