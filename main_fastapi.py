from __future__ import annotations

from fastapi import FastAPI, Depends

from api_models.loanApplication import LoanApplication
from di import DI
from usecases.interfaces.iGetApplicationStatusUseCase import IGetApplicationStatusUseCase
from usecases.interfaces.iSubmitApplicationUseCase import ISubmitApplicationUseCase
from usecases.useCaseResult import UseCaseResult

app = FastAPI()


@app.get("/")
async def about():
    return {"about": "Loan application service"}


@app.post("/application/")
async def submit_application(
        application: LoanApplication,
        usecase: ISubmitApplicationUseCase = Depends(DI().submit_application_usecase)
):
    result: UseCaseResult = await usecase.execute(application)
    return {
        "success": result.success,
        "message": result.message,
        "data": result.data
    }


@app.get("/application/{applicant_id}")
async def application_status(
        applicant_id: str,
        usecase: IGetApplicationStatusUseCase = Depends(DI().get_application_status_usecase)):
    result: UseCaseResult = await usecase.execute(applicant_id)
    return {
        "success": result.success,
        "message": result.message,
        "data": result.data
    }
