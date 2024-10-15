# Target-Sistemas

# Desafios de Programação

## Resolvi as questões utilizando a linguagem Python

### [1. Sequência de Fibonacci](https://github.com/GabrielCordeiroBarrosoTeles/Target-Sistemas/blob/main/q1.py)

```python
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
```

## [2. Verificação da letra 'a'](https://github.com/GabrielCordeiroBarrosoTeles/Target-Sistemas/blob/main/q2.py)

```
def contar_letra_a(texto):
    quantidade_a = texto.lower().count('a')  # Conta 'a' minúsculo e maiúsculo
    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

texto_informado = input("Informe uma string: ")
resultado = contar_letra_a(texto_informado)
print(resultado)
```

## 3. Valor da variável SOMA

```
int INDICE = 12, SOMA = 0, K = 1; 
enquanto K < INDICE faça { 
    K = K + 1; 
    SOMA = SOMA + K; 
} 
imprimir(SOMA);
```

### Resultado :
O valor final da variável `SOMA` é **78!!!**.

## 4. Próximos elementos

### Descrição
Complete os próximos elementos das seguintes sequências:
- a) 1, 3, 5, 7, **9**
- b) 2, 4, 8, 16, 32, 64, **128**
- c) 0, 1, 4, 9, 16, 25, 36, **49**
- d) 4, 16, 36, 64, **100**
- e) 1, 1, 2, 3, 5, 8, **13**
- f) 2, 10, 12, 16, 17, 18, 19, **20**

## 5. Interruptores e Lâmpadas

### Método para solução
1. Ligue o primeiro interruptor e mantem ele ligado por alguns minutos.
2. Após esse tempo, desligue o primeiro interruptor e ligue o segundo interruptor.
3. Vá até as lâmpadas.

### Identificação
- A lâmpada acesa corresponde ao segundo interruptor.
- A lâmpada apagada, mas quente, corresponde ao primeiro interruptor.
- A lâmpada apagada e fria corresponde ao terceiro interruptr.
