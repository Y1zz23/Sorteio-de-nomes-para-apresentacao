from random import shuffle
aluno1 = input('Insira o nome do aluno 1: ')
aluno2 = input('Insira o nome do aluno 2: ')
aluno3 = input('Insira o nome do aluno 3: ')
aluno4 = input('Insira o nome do aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print("Os alunos""(a)"" sorteados para apresentarem o trabalho foram {}".format(alunos))
