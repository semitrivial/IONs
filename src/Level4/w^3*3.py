## w^3*3.py
# In the same way, we hypothesize that to get a notation for ω^3*3,
# we can take our program for ω^3 and change the initial X value to
# be the contents of w^3*2.py (line 19 below). Verify that the first
# few outputs of this program are notations for ω^3*2.py, ω^3*2+ω^2.py,
# and ω^3*2+ω^2*2.py. By induction, this program notates ω^3*2+ω^2*ω,
# i.e. ω^3*2+ω^3, i.e. ω^3*3.
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
X=<INSERT_FILE w^3*2.py>
while True:
    output(X)
    X = TEMPLATE.replace('***', escape(X))