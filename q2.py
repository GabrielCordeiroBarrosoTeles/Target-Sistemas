def contar_letra_a(texto):
    quantidade_a = texto.lower().count('a')  # Conta 'a' minúsculo e maiúsculo
    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."



texto_informado = input("Informe uma string: ")
resultado = contar_letra_a(texto_informado)
print(resultado)
