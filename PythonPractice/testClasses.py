import sys
import mathfn
a=mathfn.math()
for i in sys.argv:
    if i != sys.argv[0]:
        i = int(i)
        a.getTable(i)