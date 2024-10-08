def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
            return result
    return wrapper


@is_prime
def sum_three(*args):
    sm = sum(args)
    return sm


result = sum_three(2, 3, 6)
print(result)
