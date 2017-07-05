from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np

### Plot node-process time

fig = plt.figure()
ax1 = fig.add_subplot(111)

#Plot data

nodecount = np.array([1, 5,10,15,20])
processtime = np.array([162, 106.8, 53.3, 33.55, 27.9])


ax1.set_xlabel('Node Count')
ax1.set_ylabel('Processing Time (minutes)')
ax1.plot(nodecount, processtime, label='Processing time')

ax1.legend()

#plt.savefig('../Figure/node-process-time.png', transparent=True)

#### End plot

#### Plot prediction vCPU utilization

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)


mapcount1 = np.array([0,1,3,5,7,10])
cpuutil1 = np.array([0,2,7,9,10,12])

xnew = np.linspace(mapcount1.min(),mapcount1.max(),30)
power_smooth = spline(mapcount1,cpuutil1,xnew)
ax2.set_ylim([0,25])
ax2.set_xlabel('Map count')
ax2.set_ylabel('vCores Utilization (24 vCores)')
ax2.plot(xnew, power_smooth, label='vCores Utilization')
ax2.legend()
#plt.savefig('../Figure/map-cpuutil.png', transparent=True)

#### End plot

#### Plot accuracy vs map

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)

mapcount2 = np.array([0,1,3,5,7,10])
accuracy = np.array([95, 95, 93, 90, 87, 85])

xnew = np.linspace(mapcount2.min(),mapcount2.max(),30)
power_smooth = spline(mapcount2,accuracy,xnew)
ax3.set_ylim([0,100])
ax3.set_xlabel('Map count')
ax3.set_ylabel('Prediction Accuracy (%)')
ax3.plot(xnew, power_smooth, label='Accuracy')
ax3.legend()

#plt.savefig('../Figure/map-accuracy.png', transparent=True)

#### End plot

#### Plot accuracy vs map

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)

nodecount2 = np.array([0, 1, 5,10,15,20])
cpuutil2 = np.array([0, 7,39, 79, 119, 151])

xnew = np.linspace(nodecount2.min(),nodecount2.max(),30)
power_smooth = spline(nodecount2,cpuutil2,xnew)

ax4.set_xlabel('Node Count')
ax4.set_ylabel('vCores Utilization (100%)')
ax4.plot(xnew, power_smooth, label='vCores Utilization')
ax4.legend(loc='upper left')

#plt.savefig('../Figure/node-cpuutil.png', transparent=True)

#### End plot


#### Plot accuracy vs map

fig5 = plt.figure()
ax5 = fig5.add_subplot(111)

memory = np.array([0, 11.25, 56.25, 112.5, 168.75, 213.75])

xnew = np.linspace(nodecount2.min(),nodecount2.max(),30)
power_smooth = spline(nodecount2,memory,xnew)

ax5.set_xlabel('Node Count')
ax5.set_ylabel('Memory Utilization (GB/100%)')
ax5.plot(xnew, power_smooth, label='Memory Utilization (GB)')
ax5.legend(loc='upper left')

#plt.savefig('../Figure/node-memory.png', transparent=True)

#### End plot

#Plot data

fig6 = plt.figure()
ax6 = fig6.add_subplot(111)

nodecount3 = np.array([0, 5,10,15,20])
speedup = np.array([0, 1.5, 3, 4.8, 5.8])

xnew = np.linspace(nodecount3.min(),nodecount3.max(),30)
power_smooth = spline(nodecount3,speedup,xnew)
ax6.set_ylim([0,6])
ax6.set_xlabel('Node Count')
ax6.set_ylabel('Speedup')
ax6.plot(xnew, power_smooth, label='Speedup')

ax6.legend(loc='upper left')

plt.savefig('../Figure/speedup.png', transparent=True)

#### End plot
