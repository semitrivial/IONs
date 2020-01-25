## w^2*2.py
# In w^2+w.py and w^2+w*2.py, we changed the initial value of X
# in w.py. What if we change the initial value of X in w^2.py?
# Exercise: convince yourself the below program outputs notations
# for for ω^2, ω^2+ω, ω^2+ω*2, ω^2+ω*3, ...
# Therefore, it notates ω^2+ω^2, i.e., (ω^2)*2.
#
# NOTE: If you see "INSERT_FILE", that's a utility signal for
# compiling an ION. The compiled ION is obtained by replacing the
# "INSERT_FILE" with an escaped copy of w^2.py.
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=<INSERT_FILE w^2.py>

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))