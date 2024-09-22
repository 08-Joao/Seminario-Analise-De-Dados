import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Leitura da base de dados
    file_path = os.path.join(os.path.dirname(__file__), 'MBA.csv')
    data = pd.read_csv(file_path)
    
    # Análise da variável categórica 'major'
    major = data['major']
    
    # Número de observações
    n = len(major)
    
    # Cálculo do número de classes usando o método da raiz
    k = int(np.sqrt(n))
    
    # Contagem de frequências para cada categoria de 'major'
    major_counts = major.value_counts()
    
    # Cálculo dos limites das classes (neste caso, apenas um exemplo para o gráfico)
    bins = np.linspace(0, len(major_counts), k + 1)
    
    # Cálculo das frequências acumuladas
    cumulative_counts = np.cumsum(major_counts)
    
    # Criação do gráfico de colunas para frequências acumuladas
    plt.figure(figsize=(10, 6))
    plt.bar(major_counts.index, cumulative_counts, color='skyblue', alpha=0.7)
    
    plt.title('Frequências Acumuladas de Áreas de Especialização (Major)')
    plt.xlabel('Área de Especialização')
    plt.ylabel('Frequência Acumulada')
    
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()

if __name__ == "__main__":
    main()
