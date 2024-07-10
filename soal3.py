class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' anda suda ditambahkan ke dalam antrian.")
    
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pesanan yang bisa dihapus.")
            return None
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian pesanan saat ini:")
            for i, item in enumerate(self.items):
                print(f"{i + 1}. {item}")

