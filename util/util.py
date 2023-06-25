import string
import random


def gerar_sequencia_aleatoria(tamanho):
    caracteres = string.ascii_uppercase + string.digits
    sequencia_aleatoria = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return sequencia_aleatoria
