## w^2.py
# Look at w.py, w*2.py, and w*3.py. In like manner, you could
# notate ω*4, ω*5, and so on. But let's be more intelligent.
#
# Convince yourself that the following program first outputs
# a program we used to notate 0. Then, a program we used to
# notate ω. Then, a program we used to notate ω*2. Then, ω*3.
# Etc. The ordinal after ω, ω*2, ω*3, ..., is ω*ω, i.e. ω^2.
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=""

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))