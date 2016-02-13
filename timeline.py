#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys

datafname = sys.argv[1]
age_xlabel = sys.argv[2]

data = np.genfromtxt(datafname, names=['caption','linestyle','start','stop','errstart','errstop'], delimiter=',', dtype=None)
data = np.sort(data, axis=0, order='start')
#cap, start, stop=data['caption'], data['start'], data['stop']

# Remove spaces
for i in range(len(data['linestyle'])):
  data['linestyle'][i] = ''.join(data['linestyle'][i].split(' '))

start = np.min(data['start'])
stop = np.max(data['stop'])
daterange = stop - start

# Create y-values by optimizing for space storage
levels = [] # one entry per item in data
occupied_until = [] # one entry per level (level in plot, not in var above)
for i in range(len(data)):
  #print i
  if i == 0:
    # Start with very first one
    levels.append(0)
    occupied_until.append(data[i]['stop'] + data[i]['errstop'])
  else:
    for j in range(len(occupied_until)):
      if data[i]['start'] - data[i]['errstart'] > occupied_until[j]:
        levels.append(j)
        #print "using old level"
        occupied_until[j] = data[i]['stop'] + data[i]['errstop']
        break
    # if we haven't found a spot for it; +1 for indexing
    if len(levels) < i+1:
      levels.append(max(levels) + 1)
      occupied_until.append(data[i]['stop'] + data[i]['errstop'])
      #print "new level created"
    
if (np.array(levels) == 0).all():
  dy = 0.5 + np.array(levels)
else:
  dy = np.array(levels) / float(max(levels))
figheight = float(1.5 + np.max(levels)*0.75)
y = 0.7 * dy + 0.1
#y = 0.1 + np.array(levels) * 0.2

plt.figure(figsize=(16,figheight))

plt.xlim(start - daterange * 0.05, stop + daterange * 0.05)
plt.ylim((0,1))
#xlim(plt.xlim()[::-1])

plt.hlines(y,data['start'],data['stop'],lw=4, linestyles=data['linestyle'])
plt.hlines(y,data['start']-data['errstart'],data['start'],lw=2, linestyles=data['linestyle'])
plt.hlines(y,data['stop'],data['stop']+data['errstop'],lw=2, linestyles=data['linestyle'])
plt.vlines(data['start'][data['errstart'] == 0], y[data['errstart'] == 0]+0.03,y[data['errstart'] == 0]-0.03,lw=2)
plt.vlines(data['stop'][data['errstop'] == 0], y[data['errstop'] == 0]+0.03,y[data['errstop'] == 0]-0.03,lw=2)
for k in range(len(data)):
  plt.text( (data['stop'][k] + data['start'][k]) / 2., y[k] + figheight/100., data['caption'][k], horizontalalignment='center')

ax = plt.gca()
for t in ax.yaxis.get_ticklines(): t.set_visible(False)
for t in ax.yaxis.get_ticklabels(): t.set_visible(False)

plt.xlabel(age_xlabel, fontsize=16)
plt.tight_layout()

plt.show()

