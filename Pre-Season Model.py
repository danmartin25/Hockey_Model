# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Import Even-Strength On-Ice Totals Data
skater_ice_totals_raw = pd.read_csv('EV On-Ice Totals.csv')
print(skater_ice_totals_raw)
skater_ice_totals_raw.head()

#Restrict Totals Data to GP,TOI,GF%,CF%,xGF%,GF,GA,CF,CA,xGF,xGA
skater_ice_totals = skater_ice_totals_raw.loc[:,['Player','Season','Team','Position','GP','TOI','GF%','CF%','xGF%','GF','GA','CF','CA','xGF','xGA']]
skater_ice_totals

#Import Even-Strength On-Ice Rates Data
skater_ice_rates_raw = pd.read_csv('EV On-Ice Rates.csv')
print(skater_ice_rates_raw)
skater_ice_rates_raw.head()

#Restrict Rates Data
skater_ice_rates = skater_ice_rates_raw.loc[:,['Player','Season','Team','Position','GP','TOI','GF%','CF%','xGF%','GF/60','GA/60','CF/60','CA/60','xGF/60','xGA/60']]
skater_ice_rates

#Add columns for G+/-,xG+/-,G/s,xG/s
skater_ice_rates['G+/-'] = skater_ice_rates['GF/60'] - skater_ice_rates['GA/60']
skater_ice_rates['xG+/-'] = skater_ice_rates['xGF/60'] - skater_ice_rates['xGA/60']
skater_ice_rates['G/s'] = skater_ice_rates['G+/-'] / 3600
skater_ice_rates['xG/s'] = skater_ice_rates['xG+/-'] / 3600
skater_ice_rates

#Get the average of G/s and xG/s
G_s_mean = skater_ice_rates['G/s'].mean()
xG_s_mean = skater_ice_rates['xG/s'].mean()
G_s_mean
xG_s_mean

#Add column for stats above averag for G/s and xG/s
skater_ice_rates['G/s AAvg'] = skater_ice_rates['G/s'] - G_s_mean
skater_ice_rates['xG/s AAvg'] = skater_ice_rates['xG/s'] - xG_s_mean
skater_ice_rates

#Add column for impact
skater_ice_rates['G Impact'] = skater_ice_rates['G/s AAvg'] * (skater_ice_rates['TOI'] / (60^3))
skater_ice_rates['xG Impact'] = skater_ice_rates['xG/s AAvg'] * (skater_ice_rates['TOI'] / (60^3))
skater_ice_rates

#Import PP On-Ice Rates Data
skater_PP_rates_raw = pd.read_csv('PP On-Ice Rates.csv')
print(skater_PP_rates_raw)
skater_PP_rates_raw.head()


