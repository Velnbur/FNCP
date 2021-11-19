"""
Baibula Kyrylo K-21
This program emulates working co-processor
for float numbers.
The expression I must compute:
    f(a, b) = (a + b) / b

"""

from stack import Stack


def greating_mess():
    print(__doc__)


def main():
    greating_mess()
    while True:
        stack = Stack()
        try:
            print("Enter a and b: ", end="")
            a, b = map(float, input().split())
        except ValueError:
            return
        except KeyboardInterrupt:
            print("Quit. Have a nice day!")
            return

        print("push a")
        stack.push(a)
        print(stack, end="\n\n")

        print("push b")
        stack.push(b)
        print(stack, end="\n\n")

        print("add")
        stack.add()
        print(stack, end="\n\n")

        print("push b")
        stack.push(b)
        print(stack, end="\n\n")

        print("div")
        stack.div()
        print(stack, end="\n\n")    

if __name__ == "__main__":
    main()
