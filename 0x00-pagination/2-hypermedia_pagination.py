#!/usr/bin/env python3
"""
Hyper media pagination module
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This is a function named index_range that takes
    two integer arguments page and page_size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves the page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves information about the page.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            "page_size": len(page_data),
            "page": page,
            "page_data": page_data,
            "next_page": page + 1 if end < len(self.__dataset) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_page": total_page,
        }
        return page_info
