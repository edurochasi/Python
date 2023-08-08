
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

def main():
    object = Mathing(6, 2)
    result = allocation_num(object)
    

if __name__ == "__main__":
    main()
