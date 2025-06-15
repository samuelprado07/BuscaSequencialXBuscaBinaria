# Importar bibliotecas
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Funções de busca
def busca_sequencial(vetor, alvo):
    visitas = 0
    for i, valor in enumerate(vetor):
        visitas += 1
        if valor == alvo:
            return i, visitas
    return -1, visitas

def busca_binaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1
    visitas = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        visitas += 1
        if vetor[meio] == alvo:
            return meio, visitas
        elif vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, visitas
# Função para coletar métricas
def coletar_metricas(vetor):
    resultados = []
    tamanho = len(vetor)
    alvo_medio = random.choice(vetor)
    alvo_pior = -1
    print("\n Alvo caso médio:", alvo_medio)
    print("\n Alvo pior caso:", alvo_pior)

    for algoritmo, func, alvo, caso in [
        ("Sequencial", busca_sequencial, alvo_medio, "Médio"),
        ("Sequencial", busca_sequencial, alvo_pior, "Pior"),
        ("Binária", busca_binaria, alvo_medio, "Médio"),
        ("Binária", busca_binaria, alvo_pior, "Pior"),
    ]:
        ini = time.time()
        _, visitas = func(vetor, alvo)
        tempo = time.time() - ini
        resultados.append({
            "Algoritmo": algoritmo,
            "Caso": caso,
            "Tamanho": tamanho,
            "Tempo (s)": tempo,
            "Visitas": visitas
        })
    
    return resultados
# Coleta dos dados
tamanhos = [1000, 10000, 100000]
todos_resultados = []

for tam in tamanhos:
    vetor = list(range(tam))
    todos_resultados.extend(coletar_metricas(vetor))

# Criar DataFrame e salvar
df_resultados = pd.DataFrame(todos_resultados)
df_resultados.to_csv("resultados_busca.csv", index=False)

df_resultados

# Gráfico de Tempo x Tamanho
seq_medio = df_resultados[(df_resultados["Algoritmo"] == "Sequencial") & (df_resultados["Caso"] == "Médio")]["Tempo (s)"].values
seq_pior = df_resultados[(df_resultados["Algoritmo"] == "Sequencial") & (df_resultados["Caso"] == "Pior")]["Tempo (s)"].values
bin_medio = df_resultados[(df_resultados["Algoritmo"] == "Binária") & (df_resultados["Caso"] == "Médio")]["Tempo (s)"].values
bin_pior = df_resultados[(df_resultados["Algoritmo"] == "Binária") & (df_resultados["Caso"] == "Pior")]["Tempo (s)"].values

# Gráfico de Tempo vs Tamanho da Entrada
plt.figure(figsize=(12, 6))
plt.plot(tamanhos, seq_medio, 'o-', label="Sequencial - Médio")
plt.plot(tamanhos, seq_pior, 'o-', label="Sequencial - Pior")
plt.plot(tamanhos, bin_medio, 's-', label="Binária - Médio")
plt.plot(tamanhos, bin_pior, 's-', label="Binária - Pior")

plt.xlabel('Tamanho da Entrada')
plt.yscale("log")
plt.xscale("log")
plt.ylabel('Tempo (s)')
plt.title('Tempo de Execução x Tamanho da Entrada')
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Junta nome para legenda mais clara
df_resultados["Algoritmo_Caso"] = df_resultados["Algoritmo"] + " - " + df_resultados["Caso"]

plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=df_resultados,
    x="Tamanho",
    y="Visitas",
    hue="Algoritmo_Caso",
    palette="tab10",
    ci=None
)

for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', fontsize=8)
plt.xlabel("Tamanho da Entrada")
plt.yscale("log")
plt.ylabel("Quantidade de Visitas (Comparações)")
plt.title("Comparações por Algoritmo e Tamanho da Entrada")
plt.grid(axis='y', linestyle='--', linewidth=1.5)
plt.legend(title="Algoritmo - Caso")
plt.tight_layout()
plt.show()