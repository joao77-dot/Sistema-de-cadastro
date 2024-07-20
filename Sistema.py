import pandas as pd
from lib.Interface import *
from time import sleep

from lib.Interface import cabeçalho, linha, menu, validaidade, validanome, validasexo
try:
    df = pd.read_excel('cadastro.xlsx')
except:
    df = pd.DataFrame(columns=['Nome', 'Sexo', 'Idade'])
    df.to_excel('cadastro.xlsx', index=False)
df = pd.read_excel('cadastro.xlsx')
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
                 'Excluir uma pessoa do cadastro', 'Alterar dados', 'Sair do sistema'])
    if resp == 1:
        cabeçalho('PESSOAS CADASTRADAS')
        sleep(1)
        if len(df) >= 1:
            print(df)
        else:
            print('Nenhuma pessoa cadastrada.')
        sleep(1)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        sleep(1)
        nome = validanome()
        sexo = validasexo()
        idade = validaidade()
        novalinha = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
        df = df.append(novalinha, ignore_index=True)
        df.to_excel('cadastro.xlsx', index=False)
        print('Cadastro atualizado com sucesso!')
        sleep(1)
    elif resp == 3:
        cabeçalho('EXCLUIR UMA PESSOA DO CADASTRO')
        sleep(1)
        df2 = df['Nome']
        print(df2.to_string())
        print(linha())
        while True:
            try:
                n = int(input('Quem você deseja excluir do cadastro?\n'
                              '(digite o índice): '))
                n = abs(n)
            except (ValueError, TypeError):
                print('\033[1;31mERRO! Digite uma opção válida.\033[m')
            except KeyboardInterrupt:
                print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            else:
                break
        df = df.drop(df.index[n])
        df.to_excel('cadastro.xlsx', index=False)
        print('Cadastro atualizado com sucesso!')
        sleep(1)
    elif resp == 4:
        cabeçalho('ALTERAR DADOS')
        sleep(1)
        df2 = df['Nome']
        print(df2.to_string())
        print(linha())
        while True:
            try:
                n = int(input('Deseja alterar os dados de qual pessoa?\n'
                              '(digite o índice): '))
                n = abs(n)
            except (ValueError, TypeError):
                print('\033[1;31mERRO! Digite uma opção válida.\033[m')
            except KeyboardInterrupt:
                print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            else:
                break
        df = df.drop(df.index[n])
        df.to_excel('cadastro.xlsx', index=False)
        print('Digite os novos dados:')
        nome = validanome()
        sexo = validasexo()
        idade = validaidade()
        novalinha = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
        df = df.append(novalinha, ignore_index=True)
        df.to_excel('cadastro.xlsx', index=False)
        print('Cadastro atualizado com sucesso!')
        sleep(1)
    elif resp == 5:
        cabeçalho('ENCERRANDO O SISTEMA... Até logo!(Criador Joao Lucas)')
        sleep(1)
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')

