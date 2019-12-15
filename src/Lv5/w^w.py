X=get_file('1.py')

TEMPLATE="""
TEMPLATE = '''XX'''
TEMPLATE = TEMPLATE.replace('=\\""', '=\\\"\"\"Xi\"\"\"')

Xi=""

while True:
    output(Xi)
    Xi = TEMPLATE.replace(\"Xi\", escape(Xi))
"""

i = 0
while True:
    output(X)
    i += 1
    Xi = "X" + str(i)
    X = TEMPLATE.replace('XX', escape(X)).replace('Xi', Xi)