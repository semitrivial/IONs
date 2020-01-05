## w^3.py
# The below program is obtained by meditating upon
# w^2.py, w^2*2.py, w^2*3.py, figuring out the pattern,
# and generalizing the pattern. Note the inner and outer
# wildcards "___" and "***", respectively. Verify that
# the first few outputs of this program are IONs that
# notate 0, ω^2, (ω^2)*2, (ω^2)*3. By induction, this
# program notates (ω^2)*ω, i.e., ω^3.
TEMPLATE='''
TEMPLATE="""
X=\'''___\'''
while True:
    output(X)
    X='output(\\\"""' + escape(X) + '\\\""")'
"""
X=\'''***\'''
while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))
'''
X=""
while True:
    output(X)
    X = TEMPLATE.replace('***', escape(X))