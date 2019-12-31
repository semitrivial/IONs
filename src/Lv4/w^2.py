# Next, we review our notation for ω^2.
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