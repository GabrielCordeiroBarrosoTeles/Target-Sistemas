def pertence_a_fibonacci(numero):
    a, b = 0, 1
    sequencia_fibonacci = [a, b]

    while b <= numero:
        a, b = b, a + b
        sequencia_fibonacci.append(b)

    if numero in sequencia_fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

# Número informado (pode ser alterado)
numero_informado = int(input("Informe um número: "))
resultado = pertence_a_fibonacci(numero_informado)
print(resultado)
