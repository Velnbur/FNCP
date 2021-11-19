from typing import List, Union
import struct

from errors import *


class Stack:
    """
    Class that represents co-processor's stack
    """
    _REG_COUNT = 8
    regs: List[float]
    last_used: int

    def __init__(self) -> None:
        self.regs = [0.0] * self._REG_COUNT
        self.last_used = 0

    def pop(self) -> float:
        """ Works just like 'pop' in nasm syntax.
            Delete last element from stack and return it.
        """
        if self.last_used <= 0:
            raise EmptyStack
        self.last_used -= 1
        return self.regs[self.last_used]

    def push(self, num: Union[int, float]) -> None:
        """ Works just like 'push' in nasm syntax.
            Add element to the end of the stack.
        """
        if(self.last_used >= self._REG_COUNT):
            raise StackOverflow

        self.regs[self.last_used] = float(num)
        self.last_used += 1

    def div(self) -> None:
        """ 'pop' two last elements from stack, 
            div them and 'push' result to stack
        """
        if self.last_used < 2:
            raise NotEnoughArgs("div", 2)
        val1, val2 = self.pop(), self.pop()
        if val1 == 0:
            self.push(float('inf'))
            return
        self.push(val2 / val1)
        
    def add(self) -> None:
        """ 'pop' two last elements from stack,
            add them and 'push' result to stack
        """
        if self.last_used < 2:
            raise NotEnoughArgs("add", 2)
        val1, val2 = self.pop(), self.pop()
        self.push(val2 + val1)

    @staticmethod
    def __binary(num: float) -> str:
        """ Method that transforms float to string
            of bits in 754 EEEI standart
        """
        return ' '.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

    def __str__(self) -> str:
        result = ""

        for i in range(self.last_used, 0, -1):
            result += f"R{i}: {self.__binary(self.regs[i-1])}"

            # result += f" DEBUG: {self.regs[i-1]}"
            
            if i != 1:
                result += "\n"
        return result