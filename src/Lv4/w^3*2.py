TEMPLATE='''
TEMPLATE="""
X=\'''{}\'''
while True:
    output(X)
    X='output(\\\"""' + escape(X) + '\\\""")'
"""
X=\'''{}\'''
while True:
    output(X)
    X = TEMPLATE.format(escape(X))
'''
X=get_file('w^3.py')
while True:
    output(X)
    X = TEMPLATE.format("{}", escape(X))