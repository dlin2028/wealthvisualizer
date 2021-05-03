import csv
import os
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import imageio

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

plt.style.use('dark_background')

filenames = []

for i in range(len(data['Millennial'][1])):
    filename = f'{i}.png'
    filenames.append(filename)


    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')
    
    plt.plot(data['Silent'][0], data['Silent'][1], label='Silent')
    plt.plot(data['BabyBoom'][0], data['BabyBoom'][1], label='BabyBoom')
    plt.plot(data['GenX'][0], data['GenX'][1], label='GenX')
    plt.plot(data['Millennial'][0], data['Millennial'][1], label='Millennial')

    plt.scatter(data['Silent'][0][i], data['Silent'][1][i])
    plt.scatter(data['BabyBoom'][0][i], data['BabyBoom'][1][i])
    plt.scatter(data['GenX'][0][i], data['GenX'][1][i])
    plt.scatter(data['Millennial'][0][i], data['Millennial'][1][i])

    plt.xlim(0,80)
    plt.ylim(0,90)
    plt.yticks(range(0,100,10))
    plt.xlabel('Years after the last of each Generation has been born')
    plt.ylabel('Share of wealth [%]')

    plt.title("% Of US Wealth owned by each Generation\n vs Yongest Age For That Generation")
    yearText = "Date: " + str(math.floor(i/4 + 1988)) + ":Q" + str((i+2)%4 + 1)
    plt.legend()
    plt.text(5, 50, yearText)

    a = plt.axes([0.1, 0.55, .333, .333])
    plt.xlim(0, 0.2)
    A = [data['Silent'][1][i], data['BabyBoom'][1][i], data['GenX'][1][i], data['Millennial'][1][i]]
    plt.pie(A)


    plt.savefig(filename)
    plt.close()

# build gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    global image
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
    for i in range(50):
        writer.append_data(image)
        
#Remove files
for filename in set(filenames):
    os.remove(filename)