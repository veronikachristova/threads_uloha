import threading

values = []
min_value = None
max_value = None
def values_input(user_input):
    values.append(user_input)

def max_value_function():
    global max_value
    max_value = max(values)
    return max_value

def min_value_function():
    global min_value
    min_value = min(values)
    return min_value

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

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")
print(values)

