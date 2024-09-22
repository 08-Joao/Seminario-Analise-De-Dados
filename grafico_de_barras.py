import pandas as pd
import os
import matplotlib.pyplot as plt

def main():
    # Leitura da base de dados
    file_path = os.path.join(os.path.dirname(__file__), 'MBA.csv')
    data = pd.read_csv(file_path)
    
    # Análise da variável qualitativa 'race'
    race_counts = data['race'].value_counts()
    
    # Criação do gráfico de barras
    plt.figure(figsize=(10, 6))
    race_counts.plot(kind='bar', color='skyblue')
    plt.title('Frequência de Raça')
    plt.xlabel('Raça')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)  # Rótulos do eixo x inclinados para melhor legibilidade
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()

if __name__ == "__main__":
    main()
