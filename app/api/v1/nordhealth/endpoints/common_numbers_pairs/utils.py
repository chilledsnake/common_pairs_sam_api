from typing import Dict, List

from app.modules.nordhealth.utils import Number


def format_common_numbers_pairs(pairs: Dict[Number, List[tuple[Number, Number]]]):
    """
    Formats a list of number pairs into a string representation.
    """

    representation = "\n".join(
        f"Pairs : {', '.join(map(str, values))} have sum : {key}"
        for key, values in pairs.items()
    )
    return representation or "No pairs found."
