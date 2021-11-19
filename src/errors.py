class StackError(Exception):
    pass


class StackOverflow(StackError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__() + "Stack overflow. Not enough space in stack"


class EmptyStack(StackError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__() + "Stack is empty. There is nothing to pop"


class NotEnoughArgs(StackError):
    operator: str
    num_of_operands: int

    def __init__(self, operator: str, num_of_operands: int, *args: object) -> None:
        super().__init__(*args)
        if not isinstance(operator ,str) and not isinstance(num_of_operands, int):
            raise TypeError

        self.operator = operator
        self.num_of_operands = num_of_operands

    def __str__(self) -> str:
        return super().__str__() + \
            f"Can't use {self.operator}. " \
            f"There is must at least {self.num_of_operands} arguments"
