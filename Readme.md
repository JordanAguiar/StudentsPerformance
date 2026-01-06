# 📊 Student Performance Analysis

## 📌 Descrição do Projeto
Este projeto realiza uma **análise exploratória de dados (EDA)** com o objetivo de identificar **quais hábitos influenciam mais o desempenho acadêmico de estudantes**.  
Foram analisados fatores como tempo de estudo, uso de redes sociais, sono, saúde mental, exercícios físicos e frequência escolar, relacionando-os com a **nota final (exam_score)**.

O projeto utiliza **Python e bibliotecas de Data Science** para extrair insights visuais e estatísticos a partir de uma base de dados com 1000 estudantes.

---

## 🎯 Objetivos
- Analisar o impacto dos hábitos diários no desempenho acadêmico  
- Identificar correlações entre variáveis comportamentais e notas  
- Comparar grupos de estudantes com diferentes padrões de estudo  
- Explorar diferenças de desempenho por gênero e estilo de vida  

---

## 🗂️ Base de Dados
O dataset contém **1000 registros** e **16 variáveis**, incluindo:

- `study_hours_per_day`
- `social_media_hours`
- `netflix_hours`
- `sleep_hours`
- `attendance_percentage`
- `exercise_frequency`
- `mental_health_rating`
- `diet_quality`
- `exam_score`
- `gender`, `age`, entre outras

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Pandas** – manipulação e análise de dados  
- **Matplotlib** – visualização de dados  
- **Seaborn** – gráficos estatísticos  

---

## 📈 Análises Realizadas

### 🔹 Correlação entre hábitos e desempenho
- Heatmap de correlação entre variáveis numéricas
- Identificação dos fatores mais associados à nota final

### 🔹 Tempo de estudo vs desempenho
- Gráfico de dispersão com regressão linear
- Comparação entre estudantes que estudam:
  - **Mais de 5h/dia**
  - **Menos de 2h/dia**

### 🔹 Redes sociais e desempenho
- Distribuição do tempo gasto em redes sociais
- Análise das notas por faixas de uso diário

### 🔹 Saúde e estilo de vida
- Impacto de:
  - Frequência de exercícios físicos
  - Saúde mental
  - Qualidade da alimentação

### 🔹 Análise por gênero
- Média e desvio padrão das notas
- Distribuição percentual entre os gêneros

---

## 📊 Principais Insights
- Estudantes que estudam mais de 5h/dia apresentam **notas significativamente mais altas**
- Uso excessivo de redes sociais tende a impactar negativamente o desempenho
- Há relação positiva entre **saúde mental, exercícios físicos e notas**
- Não foram observadas diferenças significativas de desempenho entre gêneros

---

## ▶️ Como Executar
1. Clone o repositório
```bash
git clone <https://github.com/JordanAguiar/StudentsPerformance.git>
```
2. Instale as dependências

```bash
pip install pandas matplotlib seaborn
```

3. Execute o notebook ou script Python com a base de dados:

```bash
student_habits_performance.csv
```
