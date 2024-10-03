import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    # Leitura da base de dados
    file_path = os.path.join(os.path.dirname(__file__), 'MBA.csv')
    data = pd.read_csv(file_path)
    
    # Análise da variável quantitativa 'gmat'
    gmat = data['gmat']
    
    # Verifica se há pelo menos 100 ocorrências
    if len(gmat) < 100:
        print("A variável 'gmat' não possui pelo menos 100 ocorrências.")
        return
    
    # Número de observações
    n = len(gmat)
    
    # Cálculo do número de classes usando o método de Sturges
    k = int(np.ceil(np.log2(n) + 1))
    
    # Criação dos limites das classes usando o método de Sturges
    min_gmat = gmat.min()
    max_gmat = gmat.max()
    bins = np.linspace(min_gmat, max_gmat, k + 1)

    # Cálculo das frequências em cada classe
    gmat_classes = pd.cut(gmat, bins=bins)
    class_counts = gmat_classes.value_counts().sort_index()

    # Definindo limites para as frequências de 50 em 50
    frequency_bins = np.arange(0, class_counts.max() + 50, 50)
    
    # Cálculo das frequências das classes de GMAT
    frequency_counts, _ = np.histogram(class_counts, bins=frequency_bins)

    # Cálculo da média total
    mean_gmat = gmat.mean()

    # Cálculo da variância global
    global_variance = gmat.var()

    # Resultados
    print(f"Média do GMAT: {mean_gmat}")
    print(f"Variância global do GMAT: {global_variance}\n")
    print("Frequências das classes:")
    print(class_counts)

    # Visualização das frequências das classes com gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(class_counts.index.astype(str), class_counts, color='skyblue', alpha=0.7, label='Frequência das Classes')
    
    # Adiciona linha da média total
    plt.axhline(y=mean_gmat, color='red', linestyle='--', label='Média Total')
    
    plt.title('Frequência das Classes de GMAT')
    plt.xlabel('Classes de GMAT')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Cálculo das variâncias das classes
    class_variances = gmat.groupby(gmat_classes).var()

    # Imprime as variâncias das classes
    print("\nVariâncias das classes de GMAT:")
    print(class_variances)

    # Visualização das variâncias das classes
    plt.figure(figsize=(12, 6))
    plt.bar(class_variances.index.astype(str), class_variances, color='lightgreen', alpha=0.7)
    plt.title('Variâncias das Classes de GMAT')
    plt.xlabel('Classes de GMAT')
    plt.ylabel('Variância')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
