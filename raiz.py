import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Leitura da base de dados
    file_path = os.path.join(os.path.dirname(__file__), 'MBA.csv')
    data = pd.read_csv(file_path)
    
    # Análise da variável categórica 'work_industry'
    work_industry = data['work_industry']
    
    # Número de observações
    n = len(work_industry)
    
    # Cálculo do número de classes usando o método da raiz
    k = int(np.sqrt(n))
    
    # Contagem de frequências para cada categoria de 'work_industry'
    work_industry_counts = work_industry.value_counts()
    
    # Cálculo das frequências acumuladas
    cumulative_counts = np.cumsum(work_industry_counts)
    
    # Criação do gráfico de polígonos de frequências acumuladas
    plt.figure(figsize=(10, 6))
    plt.plot(work_industry_counts.index, cumulative_counts, marker='o', color='blue', linestyle='-', alpha=0.7)
    
    plt.title('Polígono de Frequências Acumuladas de Indústrias de Trabalho (Work Industry)')
    plt.xlabel('Indústria de Trabalho')
    plt.ylabel('Frequência Acumulada')
    
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()

if __name__ == "__main__":
    main()
