import time

#adds each number incrementally
#prints total
def add_up_to(num):

    total = 0

    for i in range(1, num + 1):
        total += i
    return total

#counting milliseconds
start_time = time.perf_counter()
end_time = time.perf_counter()
elapsed_time = (end_time - start_time) * 1000.0

num1 = add_up_to(5)

print(num1)
print(elapsed_time / 1000)