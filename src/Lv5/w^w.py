# By meditating upon w.py, w^2.py, w^3.py, and w^4.py, we discern an
# underlying pattern, which allows us to write a single program that
# transcends them. This program involves an infinite sequence of
# wildcards X1, X2, X3, ..., and super-wildcards XX and Xi. Verify
# that the first few outputs notate 1, ω, ω^2, ω^3, ω^4.
X=get_file('1.py')

TEMPLATE="""
TEMPLATE = '''XX'''.replace('=\\""', '=\\\"\"\"Xi\"\"\"')

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