import sys 
import numpy
import pandas
import datetime
import calendar

sys.path.append("../module")
import basicutils

file = ""

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    print "Usage ", sys.argv[0] , " filename "
    exit(1)

df = pandas.read_excel(file)

#print the column names
cn = df.columns

count = len(df[cn[0]].values)

mat = numpy.zeros((count, len(cn)-1))

dates = []

for i in range(1,len(cn)):
    date = cn[i].split("-")
    dates.append(date)

c = 0
for i in range(1,len(cn)):
    values = df[cn[i]].values
    #print values
    j = 0
    for k in range(0, len(values)):
        v = values[k]
        if (basicutils.is_float(v)):
            mat[j,c] = v
        else:
            mat[j,c] = float('nan')
            print "Error in value ", v
        j = j + 1
    c = c + 1

print mat


for k in range(mat.shape[1]):
    for i in range(0,len(dates)):
        y0 = int(dates[i][0])
        m0 = int(dates[i][1])
        ld = calendar.monthrange(y0,m0)

        for j in range(ld[1]):
            sys.stdout.write("%f , "%(mat[i,k]))
    sys.stdout.write("\n")
