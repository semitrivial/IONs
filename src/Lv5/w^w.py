X=get_file('1.py')

i = 0
while True:
    output(X)
    Xa = "X" + str(i)
    Xb = "X" + str(i+1)
    X = """
TEMPLATE = '''"""+escape(X)+"""'''
TEMPLATE = TEMPLATE.replace('=\\""', '=\\\"\"\""""+Xb+"""\"\"\"')

"""+Xb+"""=""

while True:
    output("""+Xb+""")
    """+Xb+""" = TEMPLATE.replace(\""""+Xb+"""\", escape("""+Xb+"""))
"""
    i += 1