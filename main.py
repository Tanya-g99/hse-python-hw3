import asyncio
import time

from fastapi import FastAPI
from models.request import Request
from models.response import Response, Result

app = FastAPI()


async def calculate_square(number: float, delay: float) -> tuple[Result, float]:
    start = time.perf_counter()
    await asyncio.sleep(delay)
    end = time.perf_counter()
    elapsed = end - start
    return Result(
        number=number,
        square=number ** 2,
        delay=delay,
        time=elapsed,
    )


@app.post("/calculate/")
async def calculate(body: Request) -> Response:
    start = time.perf_counter()
    results = await asyncio.gather(
        *(
            calculate_square(number, delay)
            for number, delay in zip(body.numbers, body.delays)
        )
    )
    end = time.perf_counter()
    total_time = end - start
    sequential_time = sum(result.time for result in results)

    return Response(
        results=results,
        total_time=total_time,
        parallel_faster_than_sequential=total_time < sequential_time,
    )