import pandas as pd
import numpy as np
import os
import sys

data = pd.read_csv('data_position_manchester_unclean.csv')
print(data)

manchester = {'Team':[],'Position':[],'Value':[]}

def cal(team):
    gk_stats = 0
    count_gk = 0
    defender_stats = 0
    count_defender = 0
    midfielder_stats = 0
    count_midfielder = 0
    forward_stats = 0
    count_forward = 0
    for i in range(len(data)):
        if team in data['Team & Contract.1'][i]:
            #print(data['Name'][i], data['Positions'][i],'W' in data['Positions'][i] or 'ST' in data['Positions'][i])
            if 'GK' in data['Positions'][i]:
                gk_stats += data['↓OVA'][i]
                count_gk += 1
            if 'B' in data['Positions'][i]:
                defender_stats += data['↓OVA'][i]
                count_defender += 1
            if 'M' in data['Positions'][i]:
                midfielder_stats += data['↓OVA'][i]
                count_midfielder += 1
            if 'W' in data['Positions'][i] or 'ST' in data['Positions'][i]:
                print('W',data['Name'][i], data['Positions'][i])
                forward_stats += data['↓OVA'][i]
                count_forward += 1
    return [team,team,team,team], ['GK','DEF','MID','FOR'],[gk_stats/count_gk, defender_stats/count_defender, midfielder_stats/count_midfielder, forward_stats/count_forward]

print('Manchester City')   
team, position, stats = cal('Manchester City')
manchester['Team'].extend(team)
manchester['Position'].extend(position)
manchester['Value'].extend(stats)

print('Manchester United')
team, position, stats = cal('Manchester United')
manchester['Team'].extend(team)
manchester['Position'].extend(position)
manchester['Value'].extend(stats)

manchester = pd.DataFrame(manchester)
print(manchester)
manchester.to_csv('data_position_manchester_clean.csv', index=False)
