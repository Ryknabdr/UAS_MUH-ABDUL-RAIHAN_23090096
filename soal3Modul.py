class warmindoer:
    def _init_(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' added to the queue.")

    def dequeue(self):
        if not self.queue:
            print("No orders in the queue.")
        else:
            order = self.queue.pop(0)
            print(f"Order -{order}- melayani.")

    def display_queue(self):
        print("Current queue:")
        for i, order in enumerate(self.queue, start=1):
            print(f"{i}. {order}")
