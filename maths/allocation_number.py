"""
In a multi-threaded download, this algorithm could be used to provide
each worker thread with a block of non-overlapping bytes to download.
For example:
    for i in allocation_list:
        requests.get(url,headers={'Range':f'bytes={i}'})
"""
from __future__ import annotations

class Mathing:
    def __init__(self, number_of_bytes, partitions):
        self.number_of_bytes = number_of_bytes
        self.partitions = partitions

    def allocation_num(self) -> list[str]:

        if self.partitions <= 0:
            raise ValueError("partitions must be a positive number!")
        if self.partitions > self.number_of_bytes:
            raise ValueError("partitions can not > number_of_bytes!")
        bytes_per_partition = self.number_of_bytes // self.partitions
        allocation_list = []
        for i in range(self.partitions):
            start_bytes = i * bytes_per_partition + 1
            end_bytes = (
                self.number_of_bytes if i == self.partitions - 1 else (i + 1) * bytes_per_partition
            )
            allocation_list.append(f"{start_bytes}-{end_bytes}")
        return allocation_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
