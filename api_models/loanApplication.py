from pydantic import BaseModel


# todo: separate api and domain model, create mapper
class LoanApplication(BaseModel):
    applicant_id: str
    amount: int
    term_months: int




