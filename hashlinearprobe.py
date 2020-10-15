class HashFunction:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    def hash_func_1(self, str_list):
        for j in str_list:
            index = int(j)
            self.the_list[index] = j

    def hash_func_2(self, str_list_2):
        for k in str_list_2:
            str_int = int(k)
            index = str_int % 29
            print(f"Mod Index : {index} Value : {str_int}")

            while self.the_list[index] != "-1":
                index += 1
                print(f" Collision try {index} Instead")
                index %= self.list_size
            self.the_list[index] = k

    def find_key(self, key):
        list_index_hash = int(key) % 29
        while self.the_list[list_index_hash] != "-1":
            if self.the_list[list_index_hash] == key:
                print(f"{key} in Index {list_index_hash}")
                return self.the_list[list_index_hash]
            list_index_hash += 1
            list_index_hash %= self.list_size
        return False


# deal with 0-999 max space: 30

# hash_table = HashFunction(30)
# str_list = ["1", "5", "17", "21", "26"]
# hash_table.hash_func_1(str_list)
# for i in range(hash_table.list_size):
#     print(i, end=" ")
#     print(hash_table.the_list[i])

hash_table_2 = HashFunction(30)
str_list_2 = ["100", "510", "170", "214", "268", "398", "235",
              "802", "900", "723", "699", "1", "16", "999", "890",
              "725", "998", "990", "989", "984", "320", "321", "400", "415",
              "450", "50", "660", "624"]

hash_table_2.hash_func_2(str_list_2)
for i in range(hash_table_2.list_size):
    print(i, end=" ")
    print(hash_table_2.the_list[i])

hash_table_2.find_key("660")