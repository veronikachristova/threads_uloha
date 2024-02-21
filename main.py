import threading

values = []

def values_input(user_input):
    values.append(user_input)

def max_value_function():
    max_value = max(values)
    print(f"The maximum value is: {max_value}")

def min_value_function():
    min_value = min(values)
    print(f"The minimum value is: {min_value}")

while True:
    user_input = int(input("Input a number: "))
    values_input(user_input)
    if len(values) == 5:
        break

thread1 = threading.Thread(target=max_value_function)
thread2 = threading.Thread(target=min_value_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(values)

