class node:
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next

    def __str__(self):
        return str(self.dato)+str("\n")

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, dato):
        if not self.head:
            self.head = node(dato=dato)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node(dato=dato)
        self.size+=1

    def iterar(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    def __len__(self):
        return self.contador

    def __str__(self):
        String = ""
        node = self.head
        while node != None:
            String += str(node)
            node = node.next
        return String

    def search(self, id):
        current = self.head

        while current and current.dato.id != id:
            current = current.next
        return current.dato

    def searchNombre(self, nombre):
        current = self.head

        while current and current.dato.nombre != nombre:
            current = current.next
        return current.dato