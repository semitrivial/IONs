## w^2*3.py
# In w^2*2.py, we changed the initial value of X in w^2.py to be
# the contents of w^2.py. What if instead, we change the initial
# value of X in w^2.py to be the contents of w^2*2.py?
# Exercise: convince yourself the below program outputs notations
# for for (ω^2)*2, (ω^2)*2+ω, (ω^2)*2+ω*2, (ω^2)*2+ω*3, ...
# Therefore, it notates (ω^2)*2+ω^2, i.e., (ω^2)*3.
# NOTE: If you see "get_file", that's a utility function for
# compiling an ION. The compiled ION is obtained by replacing the
# "get_file" with an escaped copy of w^2.py.
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=<INSERT_FILE w^2*2.py>

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))