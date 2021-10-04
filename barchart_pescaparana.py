#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importar pacotes necessários para manipulação dos dados
import pandas as pd
import numpy as np


# In[8]:


#carregar dados
dados = pd.read_csv('C:/Users/diego morroni/Desktop/portfolio/relatorio30_.csv', sep=';', encoding = 'windows-1252')


# In[13]:


#filtrando ano de 2020
dados_filtrados = dados[dados.Ano.eq(2020)]


# In[14]:


#escolhendo as colunas que desejo trabalhar
dados_filtrado= dados[['Ano','Mês','Pescado', 'kg no Período']]


# In[15]:


#alterando o nome dos meses para que apareçam emordem ( deve ter jeito melhor de fazer isso)
dados_filtrado['Mês']= dados_filtrado['Mês'].replace({1:'01.Janeiro', 2:'02.Fevereiro',3:'03.Março', 4:'04.Abril', 5:'05.Maio', 6:'06.Junho',7:'07.Julho', 8:'08.Agosto', 9:'09.Setembro', 10:'10.Outubro',11:'11.Novembro', 12:'12.Dezembro'})


# In[16]:


#verificando se deu certo
dados_filtrado.sort_values(by='Mês')


# In[18]:


#criando tabela dinamica para facilitar a confecção do bar-chart-race
dados_pivo= dados_filtrado.pivot_table(values='kg no Período', index=['Mês'], columns= 'Pescado')


# In[21]:


# substituindo os "Nan" por "0"
dados_pivo= dados_pivo.fillna(0)


# In[20]:


#realizando a soma acumulada por espécie e por mês
dados_pivo.iloc[:, 0:-1]= dados_pivo.iloc[:, 0:-1].cumsum()
#fim da manipulação dos dados


# In[235]:


#instalando biblioteca para fazer o gráfico animado
#ATENÇÃO: é necessario ter a extensao ffmpeg instalada no maquina!
get_ipython().system('pip install bar-chart-race')
import bar_chart_race as bcr


# In[281]:


#por fim, chamamos o bcr e configuramos os argumentos
bcr.bar_chart_race(df=dados_pivo,
                  n_bars=10,
                  sort = 'desc',
                  title= 'Produção pesqueira paranaense em 2020 - Toneladas',
                  filename='pesca_pr.mp4',
                  steps_per_period=10,
                  period_length=2000,)

