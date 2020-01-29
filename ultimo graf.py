import pandas as pd
import matplotlib.pyplot as plt
projeto = pd.read_csv('C:/Users/David/Downloads/IaC.csv')
linhas = projeto.loc[0:29]
selcolunas = linhas['Energia']
anocolu = linhas['Ano']

fig, ax = plt.subplots()
ax.set_title('Consumo de energia')
plt.ylabel('Valores de consumo')
plt.xlabel('Ano e Mês')
plt.xticks(rotation=90)
plt.plot(anocolu,selcolunas)
ax.grid()
plt.show()
plt.savefig("sample.png")
