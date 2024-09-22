import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    # Leitura da base de dados usando os.path para gerar o caminho correto
    file_path = os.path.join(os.path.dirname(__file__), 'MBA.csv')
    data = pd.read_csv(file_path)
    
    # Exibe as primeiras linhas da base para entender o formato
    print(data.head())
    
    # Análise da variável quantitativa 'gpa'
    gpa = data['gpa']
    
    # Cálculo da média
    media_gpa = gpa.mean()
    print(f"Média do GPA: {media_gpa}")
    
    # Cálculo da variância
    variancia_gpa = gpa.var()
    print(f"Variância do GPA: {variancia_gpa}")
    
    # Visualização com histograma
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, 1ª posição
    plt.hist(gpa, bins='sturges', edgecolor='black')
    plt.title('Distribuição do GPA')
    plt.xlabel('GPA')
    plt.ylabel('Frequência')
    
    # Cálculo dos quartis para o boxplot
    quartil1 = gpa.quantile(0.25)
    quartil2 = gpa.quantile(0.5)  # Quartil 2 ou mediana
    quartil3 = gpa.quantile(0.75)
    
    # Cálculo de Dq (a diferença entre o terceiro e o primeiro quartil)
    Dq = quartil3 - quartil1
    
    # Cálculo dos limites superior e inferior
    limite_superior = quartil3 + (3/2) * Dq
    limite_inferior = quartil1 - (3/2) * Dq
    
    # Exibe os resultados
    print(f"Quartil 1 (Q1): {quartil1}")
    print(f"Quartil 2 (Q2 - Mediana): {quartil2}")
    print(f"Quartil 3 (Q3): {quartil3}")
    print(f"Dq: {Dq}")
    print(f"Limite Superior: {limite_superior}")
    print(f"Limite Inferior: {limite_inferior}")
    
    # Criação do boxplot
    plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, 2ª posição
    plt.boxplot(gpa, vert=True)
    plt.title('Boxplot da variável GPA')
    plt.ylabel('GPA')
    plt.xticks([1], ['GPA'])  # Rótulo do eixo x

    # Ajusta o layout e exibe as figuras
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
