import sys

if len(sys.argv) != 4:
    print("Usage:{0} {1} {2} {3}".format(sys.argv[0], "test.vcf", "test.sg", "output.csv")) 
    sys.exit(1)

import numpy as np
import pandas as pd

a = pd.read_csv(sys.argv[1],sep='\t',  header=None)
b = pd.read_csv(sys.argv[2], sep='\t', header=None)

a[2] = a[1]
a.rename(columns={0:'chromosome', 1:'a_start', 2:'a_end'}, inplace=True)

b[3] = b[2] + 20
b.rename(columns={1:'chromosome', 2:'b_start', 3:'b_end'}, inplace=True)

a.chromosome = a.chromosome.astype('str')
b.chromosome = b.chromosome.astype('str')
c = a.merge(b, on=['chromosome'])

c = c[ c.b_start <= c.a_start ]
c = c[ c.a_start <= c.b_end ]

c.to_csv(sys.argv[3], index=None, sep='\t')
# c.to_csv("./output.csv", index=None)
