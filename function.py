def my_function():
    print("Halo Semua")

# my_function()

#function with parameter

def halo(first_name, last_name): #bisa di default dengan menambah tanda =
    print("Halo " +first_name + " "+last_name)

# halo("Ayu", "Meilisa")
# halo("Al", "Khalif")
# halo("Agus", "Budi")

def my_function2(child3, child2, child1):
    print("The youngest child is " + child3)

# my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #untuk mendefinisikan parameternya

#function return value

def tambah(x,y):
    tambah = x + y
    return tambah

jumlah = tambah(2,9)
print(jumlah)