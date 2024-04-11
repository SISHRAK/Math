import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла
data = pd.read_csv('iris.csv')

# Какой вид в датасете представлен больше всего, какой -- меньше
most_common_species = data['Species'].mode()[0]
least_common_species = data['Species'].value_counts().idxmin()

# Рассчет выборочного среднего, выборочной дисперсии, выборочной медианы и выборочной квантили порядка 2/5 для суммарной площади чашелистика и лепестка
total_area = data['Sepal.Length'] * data['Sepal.Width'] + data['Petal.Length'] * data['Petal.Width']
mean_total_area = np.mean(total_area)
var_total_area = np.var(total_area)
median_total_area = np.median(total_area)
quantile_total_area = np.quantile(total_area, q=0.4)

# Рассчет для каждого вида
mean_species = data.groupby('Species')['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'].apply(lambda x: np.mean(x['Sepal.Length'] * x['Sepal.Width'] + x['Petal.Length'] * x['Petal.Width']))
var_species = data.groupby('Species')['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'].apply(lambda x: np.var(x['Sepal.Length'] * x['Sepal.Width'] + x['Petal.Length'] * x['Petal.Width']))
median_species = data.groupby('Species')['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'].apply(lambda x: np.median(x['Sepal.Length'] * x['Sepal.Width'] + x['Petal.Length'] * x['Petal.Width']))
quantile_species = data.groupby('Species')['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'].apply(lambda x: np.quantile(x['Sepal.Length'] * x['Sepal.Width'] + x['Petal.Length'] * x['Petal.Width'], q=0.4))

# Построение графиков
plt.figure(figsize=(15, 5))

# Гистограмма
plt.subplot(1, 3, 1)
plt.hist(total_area, bins=20, color='skyblue', edgecolor='black')
plt.title('Total Area Histogram')
plt.xlabel('Total Area')
plt.ylabel('Frequency')

# Эмпирическая функция распределения
plt.subplot(1, 3, 2)
plt.hist(total_area, bins=20, color='lightgreen', cumulative=True, edgecolor='black', density=True)
plt.title('Empirical CDF')
plt.xlabel('Total Area')
plt.ylabel('CDF')

# Box-plot
plt.subplot(1, 3, 3)
plt.boxplot(total_area)
plt.title('Total Area Boxplot')

plt.tight_layout()
plt.show()
