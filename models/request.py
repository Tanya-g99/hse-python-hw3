from pydantic import BaseModel, Field, field_validator, model_validator
from typing_extensions import Self

class Request(BaseModel):
    numbers: list[float] = Field(min_length=1)
    delays: list[float] = Field(min_length=1)

    @model_validator(mode='after')
    def validate_numbers_and_delays_length(self) -> Self:
        if len(self.numbers) != len(self.delays):
            raise ValueError("Numbers and delays must have the same length")
        return self
    
    @field_validator('delays', mode='after')
    def validate_delays_non_negative(cls, delays: list[float]) -> list[float]:
        for delay in delays:
            if delay < 0:
                raise ValueError("Delays must be non-negative")
        return delays