import time

#a function that calculates the sum of all numbers
# from 1 up to and including 'num'
def add_up_to_2(num):
    return num * (num +1) /2
#^ 3 operations, multiplication, addition, division

#counting milliseconds
start_time = time.perf_counter()
end_time = time.perf_counter()
elapsed_time = (end_time - start_time) * 1000.0

num1 = add_up_to_2(5)

print(num1)
print(elapsed_time / 1000)