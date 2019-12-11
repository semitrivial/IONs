X="""LEFT=\"""X='''\"""

RIGHT=\"""'''
while True:
    output(X)
    X = 'output(\\\"""' + escape(X) + '\\\""")'
\"""
X=""
while True:
    X = LEFT + escape(X) + RIGHT
    output(X)
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"