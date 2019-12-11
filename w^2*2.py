TEMPLATE="""
X='''{}'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=get_file('w^2.py')

while True:
    X = TEMPLATE.format(escape(X))
    output(X)