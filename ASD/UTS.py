def fib(n):
    fib_num = [0, 1]
    for i in range(2, n):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
    return fib_num

print(fib(6))
'''
Algoritma di atas adalah algoritma untuk menghitung deret Fibonacci hingga bilangan ke-n. 
Deret Fibonacci adalah deret bilangan yang diawali dengan angka 0 dan 1, kemudian setiap 
bilangan berikutnya dihasilkan dengan menjumlahkan dua bilangan sebelumnya.
Proses dari algoritma tersebut adalah sebagai berikut:

Fungsi fib() didefinisikan dengan satu parameter yaitu n, yang akan menentukan sampai 
bilangan keberapa deret Fibonacci akan dihitung.

Variabel fib_num diinisialisasi dengan dua bilangan awal yaitu 0 dan 1. Variabel ini 
akan digunakan untuk menyimpan setiap bilangan deret Fibonacci yang dihasilkan.

Dilakukan loop dengan range dari 2 hingga n-1. Loop ini akan melakukan iterasi sebanyak 
n-2 kali karena bilangan awal 0 dan 1 sudah diinisialisasi sebelumnya.

Setiap iterasi loop, bilangan deret Fibonacci baru dihasilkan dengan menjumlahkan dua 
bilangan sebelumnya. Bilangan baru tersebut kemudian ditambahkan ke dalam variabel 
fib_num menggunakan metode append().

Setelah selesai melakukan iterasi sebanyak n-2 kali, fungsi fib_num akan mengembalikan 
list fib_num yang berisi deret Fibonacci hingga bilangan ke-n.
List fib_num kemudian dicetak menggunakan perintah print().
'''

class Buku():
    def __init__(self, jumlah, judul):
        self.jumlah = jumlah
        self.judul = judul

    def __str__(self):
        return "Buku berjudul : " + str(self.judul) + " berjumlah " + str(self.jumlah)

b1 = Buku(3, 'MyDiary')
print(b1)
'''
---a---
Class Buku di atas memiliki dua atribut yaitu jumlah dan judul, yang merepresentasikan 
jumlah buku dan judul buku tersebut. Method init() digunakan untuk menginisialisasi 
atribut jumlah dan judul ketika object diinstansiasi. Method str() digunakan untuk 
mengubah object menjadi string yang dapat dicetak. Pada method ini, akan dikembalikan 
string "Buku berjudul : " diikuti dengan nilai atribut judul dan jumlah.
---c---
mengubah method str(), dengan menghapus nilai atribut jumlah
'''

class Array:
    def __init__(self, length):
        self.array = [""] * length
    
    def set_value(self, index, value):
        if isinstance(value, str):
            self.array[index] = value
        else:
            print("Error: Value must be a string")
    
    def get_value(self, index):
        return self.array[index]
    
    def get_length(self):
        return len(self.array)

## Output
my_array = Array(5)
my_array.set_value(3, "hello")
my_array.set_value(2, "hai")
print(my_array.get_value(3)) # Output: hello
print(my_array.get_value(2))
print(my_array.get_length())
'''
Pada method init, array dibuat dengan panjang yang diinginkan, yaitu sebanyak length, dengan setiap elemen array diinisialisasi sebagai string kosong ("").
Method set_value digunakan untuk mengisi nilai pada elemen array pada index tertentu. Sebelum nilai dimasukkan, akan dilakukan pengecekan apakah nilai tersebut bertipe data string atau tidak. Jika iya, maka nilai akan dimasukkan ke dalam array pada index yang dimaksud. Jika tidak, akan muncul pesan error.
Method get_value digunakan untuk mendapatkan nilai pada elemen array pada index tertentu.
Method get_length digunakan untuk mendapatkan panjang array.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_node(self, index):
        current_node = self.head
        i = 0
        while current_node is not None and i < index:
            current_node = current_node.next
            i += 1
        if current_node is None:
            return
        if current_node.prev is None:
            self.head = current_node.next
        else:
            current_node.prev.next = current_node.next
        if current_node.next is None:
            self.tail = current_node.prev
        else:
            current_node.next.prev = current_node.prev
        del current_node
        
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next

llist = DoublyLinkedList()
llist.add_node(2)
llist.add_node(0)
llist.add_node(0)
llist.add_node(2)
llist.add_node(1)
llist.add_node(0)
llist.add_node(0)
llist.add_node(2)
llist.add_node(1)
llist.display()

'''
Class Node merepresentasikan setiap node pada doubly linked list dengan atribut data, prev (pointer ke node sebelumnya), dan next (pointer ke node selanjutnya).
Class DoublyLinkedList merepresentasikan linked list dengan atribut head (pointer ke node pertama) dan tail (pointer ke node terakhir). Method add_node() digunakan untuk menambahkan node baru ke dalam linked list.
'''


def sequential_search(llist, x):
    current = llist.head
    index = 0
    
    while current is not None:
        if current.data == x:
            return index
        current = current.next
        index += 1
        
    return -1

print(sequential_search(llist, 1))