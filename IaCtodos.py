''' usando comando' import' para importar bibliotecas e usando o comando 'as' para renomear'''
import matplotlib.pyplot as plt
import pandas as pd

'''importar um arquivo com um dos comandos do pandas'''
projeto = pd.read_csv('C:/Users/David/Downloads/IaC.csv')

''' criar variavel para atribuir valores do arquivo selecionando por coluna '''
Ano = projeto['Ano']
Energia = projeto['Energia']

'''usar função da biblioteca pandas para plotar dados'''
plt.plot(Ano,Energia)

'''usar plt.show para criação do grafico'''
plt.show()
