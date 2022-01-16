def notas(*nota, sit=False):
    """
    :param nota: Uma ou mais notas dos alunos (Aceita varias)
    :param sit: Mostra uma avaliação da media
    :return: Retorna o dicionario com varias informações
    """
    media = sum(nota)/len(nota)
    dic = {'Total': len(nota), 'Maior': max(nota), 'Menor': min(nota), 'Media': media}
    if sit:
        if media <= 4:
            dic['Sit'] = 'Ruim'
        elif media < 7:
            dic['Sit'] = 'Razoável'
        else:
            dic['Sit'] = 'Boa'
    return dic


n = notas(4, 6, 8, sit=True)
print(n)
