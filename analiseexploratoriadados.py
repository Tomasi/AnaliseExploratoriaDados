import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/drive')

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams['figure.figsize']  = (16, 10)
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['axes.titlesize']  = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 4
plt.ion()

def despine(ax=None):
    if ax is None:
        ax = plt.gca()
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

path = "/content/drive/MyDrive/especialidades.xlsx"

df = pd.read_excel(path)

df.columns = ['ambulatorio', 'jul', 'ago', 'set', 'out', 'nov', 'dez', 'total']
df = df[['ambulatorio', 'jul', 'ago', 'set', 'out','nov', 'dez', 'total']]
df = df.dropna()
df.count()
df.head()

print(df.dtypes)
print(df.describe())

df['total'] = pd.to_numeric(df['total'], errors='coerce')

data = df.iloc[:-1]['total'].dropna()
data.shape

plt.hist(data, bins=20, edgecolor='k')
plt.xlabel('Total atendimentos especializado')
plt.ylabel('Frequência.')
despine(plt.gca())
plt.show()

def ecdf(data):
    x = np.sort(data)
    count = np.arange(len(data))
    y = count.cumsum()
    y = y / y.max()
    return x, y

x, y = ecdf(data)
plt.plot(x, y)
plt.xlabel('Total atendimentos especializados')
plt.ylabel('$P(X \leq x)$')
despine()
plt.show()

data.head()

num_points = len(data)
print("número de pontos:", num_points)

maiorTotalAtendimento = max(data) 
menorTotalAtendimento = min(data)
print("máximo: ", maiorTotalAtendimento, "\nminimo: ", menorTotalAtendimento)

def mean(x):
    return sum(x) / len(x)

plt.hist(data, bins=20, label='PDF', edgecolor='k')
plt.vlines(data.mean(), 0, 10, label='Mean', edgecolor='k')
plt.xlabel('Total atendimentos especializados')
plt.ylabel('P(X = x)')
plt.legend()
despine()
plt.show()

plt.hist(data, bins=20, label='Freq.', edgecolor='k')
plt.vlines(data.mean(), 0, 10, label='Mean', edgecolor='k')
plt.vlines(data.median(), 0, 10, linestyles='--', label='Median', color='red')
plt.xlabel('Duração em minutos')
plt.ylabel('Freq')
plt.legend()
despine()
plt.show()

def mode(x):
    x = np.asanyarray(x)
    unique, counts = np.unique(x, return_counts=True)
    max_count = counts.max()
    return unique[counts == max_count]

def data_range(x):
    return max(x) - min(x)

print("range: ", data_range(data))

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    deviations = np.array(deviations)
    return np.sum(deviations ** 2) / (n-1)

print("variância: ", variance(data))
print("desvio padrão: ", np.std(data))

data.describe()
