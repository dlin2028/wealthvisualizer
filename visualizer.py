import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data = dict()

data['Silent'] = [[], []]
data['BabyBoom'] = [[], []]
data['GenX'] = [[], []]
data['Millennial'] = [[], []]

with open('dfa-generation-shares.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if csv_reader.line_num == 1:
            pass
        elif csv_reader != 1:
            time = row[0].split(':Q')
            time = int(time[0]) + int(time[1])/4
            data[row[1]][0].append(time)
            data[row[1]][1].append(float(row[2]))


for item in data:
    data[item][0] = np.array(data[item][0])
    data[item][1] = np.array(data[item][1])

for i in range(len(data['BabyBoom'][0])):
    data['Silent'][0][i] = data['Silent'][0][i] -1946
    data['BabyBoom'][0][i] = data['BabyBoom'][0][i] -1964
    data['GenX'][0][i] = data['GenX'][0][i] -1980
    data['Millennial'][0][i] = data['Millennial'][0][i] -1996

up_to_delete = 0

for i in range(len(data['Millennial'][0])):
    if data['Millennial'][0][i] >= 0:
        up_to_delete = i
        break

data['Millennial'][0] = data['Millennial'][0][up_to_delete:]
data['Millennial'][1] = data['Millennial'][1][up_to_delete:]

for i in range(20):
    plt.axhline(i * 5, color='grey', markersize='0.1')

plt.plot(data['Silent'][0], data['Silent'][1], label='Silent')
plt.plot(data['BabyBoom'][0], data['BabyBoom'][1], label='BabyBoom')
plt.plot(data['GenX'][0], data['GenX'][1], label='GenX')
plt.plot(data['Millennial'][0], data['Millennial'][1], label='Millennial')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.yticks(range(0,100,5))
plt.xlabel('Years after the last of each Generation has been born')
plt.ylabel('Share of wealth [%]')

plt.title("Fraction of all US Wealth owned by each Generation relativ to their age")

plt.legend()

plt.show()