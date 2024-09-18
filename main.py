import matplotlib.pyplot as plt
import numpy as np

pesos = np.array([12, 13, 14, 14, 16, 18, 19, 22, 24, 26])
rendimentos = np.array([16, 14, 14, 13, 11, 12, 9, 9, 8, 6])

b0 = 22.252
b1 = -0.622
x_values = np.linspace(min(pesos), max(pesos), 100)
y_values = b0 + b1 * x_values

plt.figure(figsize=(10, 6))
plt.scatter(pesos, rendimentos, color='blue', label='Dados Observados')
plt.plot(x_values, y_values, color='red', label='Reta de Regressão')
plt.xlabel('Peso dos Carros (centenas de kg)')
plt.ylabel('Rendimento de Combustível (km/litro)')
plt.title('Diagrama de Dispersão e Reta de Regressão')
plt.legend()
plt.grid(True)
plt.show()
