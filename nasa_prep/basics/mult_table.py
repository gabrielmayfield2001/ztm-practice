def print_multiplication_table(n):
    outer = 1
    while outer <= n:
        inner = 1
        while inner <= n:
            print(f'{outer} * {inner} = {outer * inner}')
            inner += 1
        outer += 1


print_multiplication_table(3)
