X=get_file('1.py')

i = 0
while True:
    output(X)
    i += 1
    Xi = "X" + str(i)
    X = """
TEMPLATE = '''"""+escape(X)+"""'''
TEMPLATE = TEMPLATE.replace('=\\""', '=\\\"\"\"Xi\"\"\"')

Xi=""

while True:
    output(Xi)
    Xi = TEMPLATE.replace(\"Xi\", escape(Xi))
""".replace("Xi", Xi)