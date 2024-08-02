def password(n):
    pairs= []
    for i in range(1,21):
        for j in range(i+1, 21):
            if n % (i+j) == 0:
                pairs.append(f'{i}{j}')
    result = "".join(pairs)
    return result
for n in range(3,21):
    print(f'{n}-{password(n)}')