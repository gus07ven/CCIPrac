import collections


class MyDeque:

    def __init__(self, listOfElements):
        self.dq = collections.deque(listOfElements)

    def append_right_side(self, element):
        self.dq.append(element)

    def append_left_side(self, element):
        self.dq.appendleft(element)

    def pop_right_side(self):
        self.dq.pop()

    def pop_left_side(self):
        self.dq.popleft()


if __name__ == "__main__":

    # Create dequeue
    print("Create double ended queue:")
    days_of_week = MyDeque(["Monday", "Tuesday", "Wednesday"])
    print(days_of_week.dq)
    print("")

    # Append element to right side
    days_of_week.append_right_side("Thursday")
    print("Append element to right end:")
    print(days_of_week.dq)
    print("")

    # Append element to left side
    days_of_week.append_left_side("Sunday")
    print("Append element to left end:")
    print(days_of_week.dq)
    print("")

    # Delete element at right end
    days_of_week.pop_right_side()
    print("Remove element at right end:")
    print(days_of_week.dq)
    print("")

    # Delete element at left end
    days_of_week.pop_left_side()
    print("Remove element at left end:")
    print(days_of_week.dq)
    print("")

    # Delete element at left end bc nobody likes Mondays
    days_of_week.pop_left_side()
    print("Remove element at left end because nobody likes Mondays:")
    print(days_of_week.dq)
    print("")
