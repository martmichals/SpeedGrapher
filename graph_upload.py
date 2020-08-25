import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import datetime, os

# Get the date yesterday, since the script runs on the day after the data is collected, at 12:30 AM
yesterday =  datetime.date.today() - datetime.timedelta(days=1)

# Generate file name based on date
date_str = yesterday.strftime('%m-%d-%Y')

# X axis
time = []

# Y axes
ping = []
up = []
down = []

with open('{}.txt'.format(date_str), 'r') as file:
    for line in file:
        data = [x.strip() for x in line.split(',')]
        if len(data) != 5:
            continue
        else:
            time_data = data[1].split(':')
            time.append(int(time_data[0]) + int(time_data[1])/60)
            ping.append(float(data[2]))
            up.append(float(data[3]))
            down.append(float(data[4]))

os.mkdir(date_str)

grid = gridspec.GridSpec(2, 12)

fig = plt.figure(0, figsize=(16, 5))
fig.clf()

ax1 = fig.add_subplot(grid[0:2, 0:3])
ax1.set_xlabel('Time(hrs)')
ax1.set_ylabel('Ping(ms)')
ax2 = fig.add_subplot(grid[0:2, 4:7])
ax2.set_xlabel('Time(hrs)')
ax2.set_ylabel('Upload(Mb/s)')
ax3 = fig.add_subplot(grid[0:2, 8:11])
ax3.set_xlabel('Time(hrs)')
ax3.set_ylabel('Download(Mb/s)')

ax1.plot(time, ping, color='royalblue')
ax2.plot(time, up, color='forestgreen')
ax3.plot(time, down, color='darkorange')

plt.savefig('{}.png'.format(date_str))
plt.close(fig)