#!/usr/bin/env python3
"""
takes two integer arguments page with default value 1 and
page_size with default value 10.
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    takes two integer arguments
    return a tuple containing a start index and an end index
    """
    start = int(page_size * (page - 1))
    end = int(page * page_size)
    result = (start, end)
    return result


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
        """
        return the appropriate page of the dataset
        (i.e. the correct list of rows)
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        correct_indexes = index_range(page, page_size)
        start_index = correct_indexes[0]
        end_index = correct_indexes[1]
        data = self.dataset()
        return data[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing page_size, page, data, next_page, 
        prev_page, total_pages
        """
        data_list = self.dataset()
        return_list = self.get_page(page, page_size)
        total_page = math.ceil(len(data_list) / page_size)
        next_page = page + 1
        if next_page > total_page:
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        page_dict = {
            "page_size": page_size,
            "page": page,
            "data": return_list,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_page
        }
        return page_dict
    
