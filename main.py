# ---  Exercises 05 ---

# exercise 1:

def selection_sort(numbers: list):
    for fill_slot in range(0, len(numbers) - 1):
        position_of_max = fill_slot
        for location in range(0, len(numbers) - 1):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp


numbers = [-4, 0, 2, 11, 15, 24]
selection_sort(numbers)
print(numbers)


# Exercise 2:

def binary_search(text: list, target: str) -> str:
    text_sorted = sorted(text)
    first = 0
    last = len(text_sorted) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if text_sorted[mid] == target:
            found = True
        else:
            if target < text_sorted[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if not found:
        return None
    return target


text = ["Joy", "Mary", "John", "Anna", "Tory"]
print(binary_search(text, "me"))


# Exercise 3 - 6:

class HashTable:

    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # multidimensional list, lists inside of list

    def __my_hash(self, key):
        if isinstance(key, str):
            return len(key) % self.size
        else:
            return key % self.size

    def put(self, key, data):
        hash_value = self.__my_hash(key)
        bucket = self.buckets[hash_value]

        # Delete entry with key from bucket if it exists
        # using enumerate for finding out the index of the elements inside the bucket
        for idx, key_and_data in enumerate(bucket):
            cur_key, _ = key_and_data  # unpacking tuple, '_' for variable I'm not using
            if cur_key == key:
                bucket.pop(idx)
                break

        # Add entry to bucket
        bucket.append((key, data))

    def get(self, key):
        hash_value = self.__my_hash(key)
        bucket = self.buckets[hash_value]

        for cur_key, cur_data in bucket:
            if cur_key == key:
                return cur_data

        return None


table = HashTable(10)
table.put("Banana", 3)
table.put("Peach", 1)
table.put("Apple", 4)
print(table.buckets)

print(table.get("Peach"))
print(table.get("Apple"))
print(table.get("Banana"))

