'''usando comando 'import' para importar bibliotecas e o comando 'as'  para renomear'''
import pandas as pd
import matplotlib.pyplot as plt

'''importar aquivo no formanto csv passando endereço como referencia e atribuir os dados a uma variavel'''
projeto = pd.read_csv ('C:/Users/David/Downloads/IaC.csv')

''' criar varialvel e usar comando de busca para selecionar a parte a ser atribuida a variavel.
usando comando 'loc' para filtrar as linhas apartir do indice'''
linhas = projeto.loc[0:9]

''' usando nome do arquivo com '[ ]' para filtar coluna atraves do nome atribuido a ela
e passar e atribuir seus valores a variaveis'''
Ano = linhas['Ano']
Energia = linhas['Energia']

'''comando 'plt.plot' une as variaves para criação de um grafico'''
plt.plot(Ano,Energia)

'''mostra o grafico criado'''
plt.show()
