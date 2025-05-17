a = 0
while a < 2: # невизначена ітерація
    print("hi")
    a += 1

hello = "Hello, boys and girls!" # визначена ітерація
for i in hello:
    print(i)

class Counting:
    def __init__(self, count_to):
        self.current = 1
        self.count_to = count_to

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.count_to:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

class FibonacciIterator:
    def __init__(self):
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


my_iter = Counting(5)
print(my_iter)
for i in my_iter:
    print(i)

my_iter_list = iter([1, 2, 3])
print(my_iter_list)
print(next(my_iter_list))
print(next(my_iter_list))
print(next(my_iter_list))
# print(next(my_iter_list)) # StopIterration
print("*"*88)
my_fib = FibonacciIterator()
for i in range(20):
    print(next(my_fib))
print("do smth")
for i in range(20):
    print(next(my_fib))

def my_for(numbers):
    iterator = iter(numbers)  # Отримуємо ітератор

    while True:
        try:
            item = next(iterator)  # Отримуємо наступний елемент
            yield item
        except StopIteration:
            break  # Завершуємо цикл

print("Forward only!!!")
numbers = [1, 2, 3]
i = my_for(numbers)
print(next(i))
print(next(i))
print(next(i))

print("No len!!!")
my_list = [1, 2, 3]
my_iter_list = iter(my_list)
print(len(my_list))
try:
    print(len(my_iter_list))
except TypeError as e:
    print(e)

print("No index!!!")
print(my_list[1])
try:
    print(my_iter_list[1])
except TypeError as e:
    print(e)

iterator = iter([1, 2, 3])
print(*iterator)
print(*iterator) # Нічого не виведе, бо ітератор вже вичерпано!

iterator = iter((1, 2, 3))
# Перетворюємо у список
lst = list(iterator)
print(lst) 

iterator = iter([0, 1, 2, 3, 4])
print(all(iterator)) 
print(any(iterator)) 