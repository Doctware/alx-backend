#!/usr/bin/env python3
""" this module implement simple pagination """
import math
import csv
from typing import List, Dict, Any
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to peginate a database of populat baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cashed dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dic[int, List]:
        """Dataset indexed by sorting posistion, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        this method implement deletion-reselint hypermedia pagination
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(index, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)
        assert index < total_items

        data = []
        current_idx = index
        count = 0

        while count < page_size and current_idx < total_items:
            if current_idx in indexed_data:
                data.append(indexed_data[current_idx])
                count += 1
            current_idx += 1

        next_index = current_idx if current_idx < total_items else None

        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data),
                "data": data
        }
