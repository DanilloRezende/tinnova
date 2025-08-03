from typing import Optional

from pydantic import BaseModel


class VotingInputSchema(BaseModel):
    total_votes: int
    valid_votes: int
    blank_votes: int
    null_votes: int

class VotingResultSchema(BaseModel):
    total_votes: int
    valid_percent: float
    blank_percent: float
    null_percent: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "total_votes": 1000,
                "valid_percent": 80.0,
                "blank_percent": 15.0,
                "null_percent": 5.0
            }
        }