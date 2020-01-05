## w^3+w^2*2.py
# To get from ω^3+ω^2 to ω^3+ω^2*2, let's take w^2.py and change the
# initial X-value from "" to w^3+w^2.py. Verify that the first few
# outputs of this program notate ω^3+ω^2, ω^3+ω^2+ω, ω^3+ω^2+ω*2, ...,
# so this program notates ω^3+ω^2+ω*ω, i.e., ω^3+ω^2+ω^2, i.e., ω^3+ω^2*2.
# NOTE: If you see "get_file", that's a util function. The
# compiled ION is obtained by replacing the get_file with an
# escaped copy of the contents of w^3+w^2.py.
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=get_file('w^3+w^2.py')

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))