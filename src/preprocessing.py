#!/usr/bin/env python3

import numpy as np
import pandas as pd

tavole_mortalita = pd.read_csv('../sources/istat_tavole_mortalità_donne_età_fertile_not_processed.csv')
aborti_per_anno = pd.read_csv('../sources/aborti_italia_dati_per_anno.csv')
demografia = pd.read_csv('../sources/demografia.csv')

# Preparazione dei dati ISTAT provenienti dalle tavole di mortalità
morti_territorio_nazionale = tavole_mortalita.loc[tavole_mortalita['Territorio'] == 'Italia']
morti_per_anno_per_fascie = morti_territorio_nazionale.loc[morti_territorio_nazionale['TIME'].isin(list(np.arange(1974,2018)))]
morti_rosa_per_fascie = morti_per_anno_per_fascie.loc[morti_per_anno_per_fascie['Sesso'] == 'femmine']
morti_rosa_per_fascie_clean = morti_rosa_per_fascie[['TIME', 'ETA1','Value']]
morti_rosa_per_anno = morti_rosa_per_fascie_clean.groupby(['TIME']).sum().reset_index()
morti_rosa_per_anno.columns = ['anno', 'morti']

# Unificazione dei dati
morti_e_aborti = pd.merge(morti_rosa_per_anno, aborti_per_anno, how='outer').fillna(0).astype(int)
unified = pd.merge(demografia[['anno', 'popolazione', 'nascite']], morti_e_aborti).fillna(0).astype(int)

# Creazione file
unified.to_csv('../DATA/unified.csv', sep=',', index=False)
