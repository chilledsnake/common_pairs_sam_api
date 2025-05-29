from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/get_info/", response_class=PlainTextResponse)
async def get_info():
    return """
    Github repository: xyz,
    Author: Cezary Wróblewski
    Email: cwroblewski@o2.pl
    """
