''' importar bibliotecas usando o comando 'import' e renomeando usando comando 'as' '''
import pandas as pd
import matplotlib.pyplot as plt

''' 'pd.read_csv' usado para importar arquivos'''
projeto = pd.read_csv('C:/Users/David/Downloads/IaC.csv')

''' criando variavel para a atribuição dos valores'''
''' função 'loc' usada para buscar dados de uma area determinada de linhas atraves de seu indice '''
Ulinhas = projeto.loc[131:141]

'''criando variavel e atribuindo valores usando comando de busca por coluna'''
Ano = Ulinhas['Ano']
Energia = Ulinhas['Energia']

''' 'plt' comando usado para a criação de dados'''
plt.plot(Ano,Energia)

''' criar legendas'''
plt.title('Consumo')

'''criar legendas no eixo y do grafico'''
plt.ylabel('Valores de consumo')

''' criar legenda no eixo x do grafico'''
plt.xlabel('Ano e Mês')

''' rotacionar legendas do eixo x'''
plt.xticks(rotation=90)

'''acrescentando grid'''
plt.grid(True)

''' aplicar fundo de grades no grafico'''
plt.plot(Ano, Energia, color='black')

''' mostrar grafico criado'''
plt.show()
