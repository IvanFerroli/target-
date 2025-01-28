def fibonacci_check(num):

    a, b = 0, 1
    
    while b < num:
        a, b = b, a + b

    if b == num or num == 0:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número para verificar: "))
print(fibonacci_check(numero))
