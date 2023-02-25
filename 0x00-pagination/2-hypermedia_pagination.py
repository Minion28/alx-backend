#!/usr/bin/env python3
'''
pagination using dataset
'''
import csv
import math
from typing import List, Tuple, Dict


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
        use asset to verify both arguments and integers greater than 0
        """
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0]:i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves information about a page.
        """
        data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total = math.ceil(len(self.__dataset) / page_size)
        output = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total': total,
        }
        return output


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    use index_range to find correct indexes to
    paginate the dataset correctly
    """
    start_index = page * page_size - page_size
    end_index = start_index + page_size

    return (start_index, end_index)
