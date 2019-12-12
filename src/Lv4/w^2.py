TEMPLATE="""
X='''{}'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=""

while True:
    output(X)
    X = TEMPLATE.format(escape(X))