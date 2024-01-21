import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

from multiprocessing import Process

def square_numbers(numbers):
    for number in numbers:
        print('Square:', number * number)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a process
    process = Process(target=square_numbers, args=(numbers,))

    # Start the process
    process.start()

    # Wait for the process to finish
    process.join()
