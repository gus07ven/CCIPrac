
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
        element_to_remove = self.queue[0]
        self.queue.remove(element_to_remove)
        return "Removing from queue: {0}".format(element_to_remove)

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
    print(queue.dequeue())
    print("")

    print("Is queue empty?")
    print(queue.is_empty())
    print("")

    print("Final queue:")
    print(queue.display())






