"""
Python Clearcode intern summer 2019 task

To solve this task I used a dynamic programming algorithm.
The idea of dynamic programming is explained in a simple way in
Aditya Y. Bhargava book, titled "Grokking Algorithms".
Dynamic programming consists of breaking the problems into subproblems.
To get the most efficient code solution I adapt solution from  site
https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution/20581#20581
"



"""
from typing import List, Tuple, Set
from functools import lru_cache


'''Function find the most profitable set of mems '''
def calculate(usb_size: int, memes: List[Tuple[str, int, int]]) -> Tuple[int, Set[str]]:
    memes = list(set(memes))
    result = 0
    mems = set()
    usb_size = usb_size*1024

    'Finds the most profitable set'
    @lru_cache(maxsize=None)
    def bestvalue(i, usb_size):
        if usb_size < 0:
            return float('-inf')
        if i == 0:
            return 0
        _, weight, value = memes[i - 1]

        return max(
            bestvalue(i - 1, usb_size), bestvalue(i - 1, usb_size - weight) + value
        )

    for i in reversed(range(len(memes))):
        if bestvalue(i + 1, usb_size) != bestvalue(i, usb_size):
            print(memes[i])
            result += memes[i][2]
            mems.add(memes[i][0])
            usb_size -= memes[i][1]
    return result, mems


usb_size = 1
memes = [
('rollsafe.jpg', 205, 6),
('sad_pepe_compilation.gif', 410, 10),
('yodeling_kid.avi', 605, 12)
]
print(calculate(usb_size, memes))