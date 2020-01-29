''' importar bibliotecas e renomear'''
import pandas as pd
import matplotlib.pyplot as plt

'''importar arquivos e atribuir a uma variavel'''
primeiro = pd.read_csv('C:/Users/David/Downloads/IaC.csv')

trinta = primeiro.loc[0:29]

''' criar variavel e usar comando para selecionar coluna a ser atribuida'''
Ano = trinta['Ano']
Energia = trinta['Energia']

''' criar grafico'''
plt.plot(Ano,Energia)

''' criar legedas acima do grafico'''
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
plt.plot(Ano, Energia, color='yellow')

''' mostrar grafico criado'''
plt.show()
     
