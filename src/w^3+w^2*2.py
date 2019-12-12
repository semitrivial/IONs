TEMPLATE="""
X='''{}'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=get_file('w^3+w^2.py')

while True:
    output(X)
    X = TEMPLATE.format(escape(X))