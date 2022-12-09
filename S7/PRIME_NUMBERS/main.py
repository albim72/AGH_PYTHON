import time,concurrent.futures

def find_prime_numbers_sum(minimum,maximum):
    total = 0
    for number in range(minimum,maximum+1):
        count =0
        for i in range(2,(number//2+1)):
            if number%i==0:
                count=count+1
                break
        if count==0 and number!=1:
            total = total + number
    return total

def run_heavy_function(params):
    return find_prime_numbers_sum(*params)

def main():
    numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(800,15000),(355,1890)]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        result = executor.map(run_heavy_function,numbers)

    print(list(result))
    end_time = time.time()
    print(f'Całkowity czas wykonania wątków asynchronicznych: {end_time - start_time:2f} s')

if __name__ == '__main__':
    main()
