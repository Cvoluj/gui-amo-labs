from typing import Sequence, Iterable, List
from dataclasses import dataclass
from numbers import Number
import time
@dataclass
class BubbleSortResult:
    sequence: Sequence[Number]
    operations: int
    execution_time: float

    def __repr__(self):
        return f"Bubble sort operations: {self.operations}"


def bublle_sort(*args: Iterable[Sequence[Number]]) -> List[BubbleSortResult]:
    results: List[BubbleSortResult] = []
    for seq in args:
        start_time = time.time()
        flag = False
        operations = 0
        n = len(seq)
        while not flag:
            operations += 1
            flag = True
            for i in range(n - 1):
                operations += 1
                if seq[i] > seq[i + 1]:
                    operations += 3
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]
                    flag = False

        execution_time = time.time() - start_time
        obj = BubbleSortResult(seq, operations, execution_time)
        results.append(obj)
        print('done seq')
    return results
