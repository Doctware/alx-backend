#!/usr/bin/env python3
""" this module contsins simole helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    the helper fuction
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
