from typing import List

from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from .models import Voting
from .schemas import VotingInputSchema, VotingResultSchema
from .services.voting import VotingService

router = Router()

@router.post("/voting/", response=VotingResultSchema)
def create_voting(request: HttpRequest, payload: VotingInputSchema):
    try:
        voting = Voting.objects.create(
            total_votes=payload.total_votes,
            valid_votes=payload.valid_votes,
            blank_votes=payload.blank_votes,
            null_votes=payload.null_votes
        )
        
        service = VotingService(voting)
        
        if not service.validate_vote_totals():
            voting.delete()
            raise HttpError(400, "Invalid voting data: vote totals exceed total voters")
        
        return {
            "total_votes": voting.total_votes,
            "valid_percent": round(service.get_percent_valid_votes(), 2),
            "blank_percent": round(service.get_percent_blank_votes(), 2),
            "null_percent": round(service.get_percent_null_votes(), 2),
        }
        
    except Exception as e:
        raise HttpError(500, f"Error creating voting: {str(e)}")

@router.post("/voting/calculate/", response=VotingResultSchema)
def calculate_voting(request: HttpRequest, payload: VotingInputSchema):
    try:
        voting = Voting(
            total_votes=payload.total_votes,
            valid_votes=payload.valid_votes,
            blank_votes=payload.blank_votes,
            null_votes=payload.null_votes
        )
        
        service = VotingService(voting)
        
        if not service.validate_vote_totals():
            raise HttpError(400, "Invalid voting data: vote totals exceed total voters")
        
        return {
            "total_votes": voting.total_votes,
            "valid_percent": round(service.get_percent_valid_votes(), 2),
            "blank_percent": round(service.get_percent_blank_votes(), 2),
            "null_percent": round(service.get_percent_null_votes(), 2),
        }
        
    except Exception as e:
        raise HttpError(500, f"Error calculating voting results: {str(e)}")

@router.get("/voting/{voting_id}", response=VotingResultSchema)
def get_voting_results(request: HttpRequest, voting_id: int):
    try:
        voting = Voting.objects.get(id=voting_id)
    except Voting.DoesNotExist:
        raise HttpError(404, "Voting not found")

    service = VotingService(voting)
    
    if not service.validate_vote_totals():
        raise HttpError(400, "Invalid voting data: vote totals exceed total voters")

    return {
        "total_votes": voting.total_votes,
        "valid_percent": round(service.get_percent_valid_votes(), 2),
        "blank_percent": round(service.get_percent_blank_votes(), 2),
        "null_percent": round(service.get_percent_null_votes(), 2),
    }