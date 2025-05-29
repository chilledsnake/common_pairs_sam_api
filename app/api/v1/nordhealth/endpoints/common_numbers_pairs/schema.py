from typing import List

from fastapi.params import Query
from pydantic import BaseModel

from app.modules.nordhealth.utils import Number


class ExtractCommonNumbersPairsInputDataSchema(BaseModel):
    input_data: List[Number] = Query(
        [], description="List of numbers to extract common pairs from"
    )  # type: ignore
