TEMPLATE="""
X='''{}'''
while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=""

while True:
    X = TEMPLATE.format(escape(X))
    output(X)
