
class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if self.is_empty():
            print("Underflow error. Stack is empty.")
            return
        else:
            return self.stack.pop()

    def display(self):
        stack_size = len(self.stack) - 1
        while stack_size >= 0:
            print(self.stack[stack_size])
            stack_size -= 1


if __name__ == "__main__":

    stack = Stack()

    print("Check that stack is empty:")
    print(stack.is_empty())

    print("")
    print("Push Monday, Tuesday, Wednesday to stack:")
    stack.push("Monday")
    stack.push("Tuesday")
    stack.push("Wednesday")
    stack.display()

    print("")
    print("Peek top of stack:")
    print(stack.peek())

    print("")
    print("Pop top element:")
    stack.pop()
    stack.display()

    print("")
    print("Add Thursday to top of stack:")
    stack.push("Thursday")
    stack.display()


