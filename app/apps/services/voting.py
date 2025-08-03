class VotingService:
    def __init__(self, voting):
        self.voting = voting

    def _safe_divide(self, numerator, denominator):
        if denominator == 0:
            return 0.0
        return (numerator / denominator) * 100

    def get_percent_valid_votes(self):
        return self._safe_divide(self.voting.valid_votes, self.voting.total_votes)

    def get_percent_blank_votes(self):
        return self._safe_divide(self.voting.blank_votes, self.voting.total_votes)

    def get_percent_null_votes(self):
        return self._safe_divide(self.voting.null_votes, self.voting.total_votes)

    def validate_vote_totals(self):
        total_calculated = self.voting.valid_votes + self.voting.null_votes + self.voting.blank_votes
        return total_calculated != self.voting.total_votes