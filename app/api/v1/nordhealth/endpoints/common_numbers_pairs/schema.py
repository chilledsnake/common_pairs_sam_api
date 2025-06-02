from typing import List

from pydantic import BaseModel, Field

from app.modules.nordhealth.utils import Number


class ExtractCommonNumbersPairsInputDataSchema(BaseModel):
    input_data: List[Number] = Field(
        [], description="List of numbers to extract common pairs from"
    )
