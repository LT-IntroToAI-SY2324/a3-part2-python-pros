from typing import Any, Callable, List, Tuple
from match import match
from database import *

def games_by_publisher(src: List[str]):
    pass




pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What games have % published"), games_by_publisher)
]