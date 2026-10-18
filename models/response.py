from pydantic import BaseModel, Field

class Result(BaseModel):
    number: float
    square: float
    delay: float
    time: float

class Response(BaseModel):
    results: list[Result]
    total_time: float
    parallel_faster_than_sequential: bool