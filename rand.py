import time

def random_number(minimum, maximum):
    now = time.time()
    now = str(now)[::-1]
    rnd = int(now[:3])
    return minimum + rnd * (maximum - minimum)

min = 1 
max = 100
print(random_number(min, max)) 
