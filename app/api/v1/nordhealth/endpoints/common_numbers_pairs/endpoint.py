from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.api.v1.nordhealth.endpoints.common_numbers_pairs.schema import (
    ExtractCommonNumbersPairsInputDataSchema,
)
from app.api.v1.nordhealth.endpoints.common_numbers_pairs.utils import (
    format_common_numbers_pairs,
)
from app.modules.nordhealth.processors import IterableNumbersProcessor

router = APIRouter()


@router.post("/extract_numbers_pairs/", response_class=PlainTextResponse)
async def extract_common_numbers_pairs(data: ExtractCommonNumbersPairsInputDataSchema):
    processor = IterableNumbersProcessor(input_data=data.input_data)
    result = format_common_numbers_pairs(processor.common_pairs)

    return result
