import time

def add_up_to_2(num):
    return num * (num +1) /2

start_time = time.perf_counter()
end_time = time.perf_counter()
elapsed_time = (end_time - start_time) * 1000.0

num1 = add_up_to_2(100000000)

print(num1)
print(elapsed_time / 1000)
