# w^2.py
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