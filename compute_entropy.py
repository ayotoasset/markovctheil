import scipy
import numpy
import math
import sys 
import scipy.stats 
import scipy.io 

import matplotlib.pyplot as plt
sys.path.append("./module")
import basicutils 

if len(sys.argv) != 2:
    print "need to specify a filename"
    exit(1)

filename=sys.argv[1]

msd = scipy.io.loadmat(filename)

namems = "spread_synth"

r = msd[namems] #traiettorie spread simulate

run = r.shape[0]
time = r.shape[1]
countries = r.shape[2]
print "countries: ", countries, "time: ", time, "run: ", run

#exit(1)

R = numpy.sum(r, axis=2)

print "R.shape: ", R.shape

entropy = numpy.zeros((time), dtype = 'float64')
std = numpy.zeros((time), dtype = 'float64')
T = numpy.zeros((time, run), dtype = 'float64')

p = numpy.zeros((countries, time, run), dtype = 'float64')

for c in range(countries):
    print c+1 , " of ", countries
    for t in range(time):
        for i in range(run):
            p[c, t, i] = r[i,t,c] / R[i, t]

for t in range(time):
    print t+1 , " of ", time
    for i in range(run):
       for c in range(countries):
            if p[c, t, i] > 0: 
                T[t,i] += p[c, t, i] * math.log(float(countries) * p[c, t, i])

for t in range(time):
    entropy[t] = numpy.mean(T[t, :])
    std[t] = numpy.std(T[t, :]
            )
basicutils.vct_to_file(entropy, 'edt.txt')
basicutils.vct_to_file(std, 'std.txt')

plt.plot(entropy)
#plt.plot(std)
plt.show()

