# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# * Importando e entendendo base de dados

# %%
#Ler aquivo CSV
df = pd.read_csv(r"data\student_habits_performance.csv")

# %%
#Visualizar dados
df

# %% [markdown]
# * Quais hábitos impactam mais o desempenho dos alunos? 

# %%
#Tipos de dados

df.info()

# %%
#Colunas numéricas
cols = [
    "study_hours_per_day",
    "social_media_hours",
    "netflix_hours",
    "sleep_hours",
    "attendance_percentage",
    "exercise_frequency",
    "mental_health_rating",
    "exam_score",
]

# Plotar mapa de calor (heatmap)
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlação entre hábitos e nota final")
plt.show()

# %% [markdown]
# * Alunos que estudam mais tem melhor desempenho?

# %%
# Gráfico de dispersao com linha de regressao
# x="study_hours_per_day" / y="exam_score"
sns.lmplot(data=df, x="study_hours_per_day", y="exam_score")
plt.title("Mais estudo -> notas mais altas?")
plt.show()

# %%
#Comparado médias: quem estuda >5h x <2h
filtro_Estudo_alto = df["study_hours_per_day"] > 5
filtro_estudo_baixo = df["study_hours_per_day"] < 2

grupo_estudo_alto = df[filtro_Estudo_alto]["exam_score"]
grupo_estudo_baixo = df[filtro_estudo_baixo]["exam_score"]

print("Média notas (estuda > 5h):", grupo_estudo_alto.mean())
print("Média notas (estuda < 2h):", grupo_estudo_baixo.mean())

# %% [markdown]
# * O tempo gasto em redes sociais afeta o desempenho dos alunos?

# %%
# Redes sociais: distribuição geral (Histograma)
# x="social_media_hours"

sns.histplot(data=df, x="social_media_hours")
plt.title("Distribuição de tempo em redes sociais")
plt.show()

# %%
#Avaliando notas médias
#por diferentes intervalos (bins) de periodos gastos em redes sociais
# ["0-2h", "2h-4h", "4h-6h", "6h+"]

df["social_media_bin"] = pd.cut(
    df["social_media_hours"],
    bins=[0, 2, 4, 6],
    labels=["0-2h", "2h-4h", "4h-6h"]
)
#Gráfico de caixa
sns.boxplot(x="social_media_bin", y="exam_score", data=df)
plt.title("Notas por tempo em redes sociais")
plt.show()

# %% [markdown]
# * Alunos mais saudáveis têm melhores desempenhos?

# %%
#Frequência de exercícios físicos
for col in ["exercise_frequency", "mental_health_rating", "diet_quality"]:
    sns.boxplot(x=col, y="exam_score", data=df)
    plt.show()

# %% [markdown]
# * Há diferença nas notas entre homens e mulheres?

# %%
#Estatistica por gênero (média e desvio padrão)
df.groupby(["gender"])["exam_score"].agg(["mean", "std"])

# %%
#Avaliar distribuição de gênero
df["gender"].value_counts(normalize=True)


