import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv.txt', usecols=['index', 'within_month', 'within_2month', 'within_3month', 'within_4month', 'within_5month', 'within_6month', 'within_7month', 'final'])
df.set_index('index', inplace=True)
df.plot(kind='line') 

df_long = pd.melt(df, id_vars=['index', 'final'], var_name='time', value_name='probability')
df_long['time'] = pd.to_datetime(df_long['time'].str.replace(',', ''))

plt.plot('time', 'probability', data=df_long[df_long['index'] == 0], label='Deal 0')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 1], label='Deal 1')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 2], label='Deal 2')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 3], label='Deal 3')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 4], label='Deal 4')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 5], label='Deal 5')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 6], label='Deal 6')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 7], label='Deal 7')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 8], label='Deal 8')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 9], label='Deal 9')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 10], label='Deal 10')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 11], label='Deal 11')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 12], label='Deal 12')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 13], label='Deal 13')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 14], label='Deal 14')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 15], label='Deal 15')
plt.plot('time', 'probability', data=df_long[df_long['index'] == 16], label='Deal 16')

plt.legend()
plt.xlabel('Time')
plt.ylabel('Probability')
plt.title('Probability of Deals within Time Periods')
plt.show()

