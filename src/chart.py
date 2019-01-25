#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, AnnotationBbox
import pandas as pd

data = pd.read_csv('../DATA/unified.csv')

ticks = data['anno']
n_ticks = len(ticks)
index = np.arange(n_ticks)

# Soglie e picchi
donne_morte = 20000
aborti_clandestini = 1000000
picco82 = 234593

######################## GRAFICI ########################

# 1. Aborti
fig, ax = plt.subplots()
ax = data[['aborti']].plot(kind='bar', title='1. Aborti', legend=True, fontsize=12)
plt.xticks(index, list(ticks), rotation=60, fontsize=8)

ax.annotate('Picco massimo aborti', 
            xy=(9,picco82 + 2), 
            xytext=(n_ticks/2,picco82),
            va='center', ha= 'center',
            bbox=dict(boxstyle='round', fc='w'),
            arrowprops=dict(arrowstyle='->'))

plt.savefig('../CHARTS/aborti.png')

# 2. Nascite e Aborti
fig, ax = plt.subplots()
ax = data[['aborti','nascite']].plot(kind='bar', title='2. Nascite e Aborti', legend=True, fontsize=12)
plt.xticks(index, list(ticks), rotation=60, fontsize=8)

# trendlines
z1=np.polyfit(index, data['nascite'],1)
p1=np.poly1d(z1)
plt.plot(index, p1(index), "r--")

z2=np.polyfit(index[9:], data['aborti'][9:],1) # Scartiamo deliberatamente gli anni prima del 1982
p2=np.poly1d(z2)
plt.plot(index, p2(index), "k--")

plt.savefig('../CHARTS/nascite_aborti.png')

# 3. Nascite, aborti e popolazione totale
fig, ax = plt.subplots()
ax = data[['aborti','nascite', 'popolazione']].plot(kind='bar', title='3. Nascite, Aborti e Popolazione', legend=True, fontsize=12., logy=True)
plt.xticks(index, list(ticks), rotation=60, fontsize=8)

plt.savefig('../CHARTS/nascite_aborti_popolazione.png')

# 4. Morti e Aborti
fig, ax = plt.subplots()
ax = data[['morti','aborti']].plot(kind='bar', title='4. Morti e Aborti', legend=True, fontsize=12)

plt.xlabel('Anni')

plt.xticks(index, list(ticks), rotation=60, fontsize=8)

plt.savefig('../CHARTS/morti_aborti.png')

# 5. Morti naturali e da Aborti Clandestini
fig, ax = plt.subplots()

ax = data[['morti']].plot(kind='bar', title='5. Morti Rosa', legend=True, fontsize=12)

plt.xlabel('Anni')

plt.xticks(index, list(ticks), rotation=60, fontsize=8)

#label

ax.annotate('20 mila donne morte ogni anno per aborti clandestini', 
            xy=(n_ticks*0.25,donne_morte), 
            xytext=(n_ticks/2,donne_morte*0.75),
            va='center', ha= 'center',
            bbox=dict(boxstyle='round', fc='w'),
            arrowprops=dict(arrowstyle='->'))

plt.plot([0, n_ticks], [donne_morte, donne_morte], "k--")

plt.savefig('../CHARTS/morti_da_fake_news.png')

# 6. Aborti Reali e Aborti Clandestini
fig, ax = plt.subplots()

ax = data[['morti','aborti']].plot(kind='bar', title='6. Aborti Clandestini e Aborti Veri', legend=True, fontsize=12)

plt.xlabel('Anni')

plt.xticks(index, list(ticks), rotation=60, fontsize=8)

#labels
plt.plot([0, n_ticks], [donne_morte, donne_morte], "k--")
ax.annotate('20 mila donne morte ogni anno per aborti clandestini', 
            xy=(n_ticks*0.25,donne_morte), 
            xytext=(n_ticks/2,aborti_clandestini*0.30),
            va='center', ha= 'center',
            bbox=dict(boxstyle='round', fc='w'),
            arrowprops=dict(arrowstyle='->'))

plt.plot([0, n_ticks], [aborti_clandestini, aborti_clandestini], "k--")
ax.annotate('Un milione di aborti clandestini ogni anno', 
            xy=(n_ticks*0.25,aborti_clandestini), 
            xytext=(n_ticks/2,aborti_clandestini*0.75),
            va='center', ha= 'center',
            bbox=dict(boxstyle='round', fc='w'),
            arrowprops=dict(arrowstyle='->'))

plt.savefig('../CHARTS/total_fake_news.png')

