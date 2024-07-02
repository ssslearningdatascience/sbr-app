from pydantic import BaseModel


class OperationRequest(BaseModel):
    a: int
    b: int
    operator: str