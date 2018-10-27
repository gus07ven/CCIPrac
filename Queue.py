
class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        if data is None:
            print("None is not a valid data value.")
            return
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty() is True:
            print("Queue is empty. Nothing to delete.")
            return
        self.queue.remove(self.queue[0])

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def display(self):
        if self.is_empty() is True:
            return
        for element in self.queue:
            print(element)
        print("")


if __name__ == "__main__":

    queue = Queue()

    print("Enqueuing/inserting Monday, Tuesday, Wednesday to queue:")
    queue.enqueue("Monday")
    queue.enqueue("Tuesday")
    queue.enqueue("Wednesday")
    queue.display()

    print("Dequeuing/deleting Monday from queue:")
    queue.dequeue()
    queue.display()

    print("Is queue empty?")
    print(queue.is_empty())






