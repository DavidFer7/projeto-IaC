''' importar bibliotecas'''
import pandas as pd
import matplotlib.pyplot as plt

''' importar arquivos'''
projeto = pd.read_csv('C:/Users/David/OneDrive/Documentos/codigos python/IaC.csv')

''' selecionar atraves de nome da coluna'''
box = projeto['Energia']

'''criar boxplot'''
plt.boxplot(box)


''' mostrar grafico criado'''
plt.show()
