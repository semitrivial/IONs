X=get_file('1.py')

i = 1
while True:
    output(X)
    Xi = "X" + str(i)
    X = """
TEMPLATE = '''"""+escape(X)+"""'''
TEMPLATE = TEMPLATE.replace('=\\""', '=\\\"\"\""""+Xi+"""\"\"\"')

"""+Xi+"""=""

while True:
    output("""+Xi+""")
    """+Xi+""" = TEMPLATE.replace(\""""+Xi+"""\", escape("""+Xi+"""))
"""
    i += 1