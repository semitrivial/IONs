X=get_file('1.py')
WW=get_file('w^w.py')

TEMPLATE="""
TEMPLATE = '''XX'''.replace('=\\""', '=\\\"\"\"Xi\"\"\"')

Xi=""

while True:
    output(Xi)
    Xi = TEMPLATE.replace(\"Xi\", escape(Xi))
"""

METATEMPLATE="""
TEMPLATE = '''XXX'''.replace('=\""', '=\"""Xi\"""')

Xi='''W^W'''

while True:
    output(Xi)
    Xi = TEMPLATE.replace("Xi", escape(Xi))
"""

i = 0
while True:
    i += 1
    Xi = "X" + str(i)
    result = METATEMPLATE.replace('XXX', escape(X))
    result = result.replace('Xi', Xi)
    result = result.replace('W^W', escape(WW))
    output(result)
    X = TEMPLATE.replace('XX', escape(X)).replace('Xi', Xi)