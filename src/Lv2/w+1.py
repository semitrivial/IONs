## w+1.py
# In the same way we went from 1 to 2, we go from ω to ω+1.
#
# The Intuitive Ordinal Notations (IONs) are defined so that:
#   "For any computer program P, if all the outputs of P are
#   IONs, then P itself is an ION."
#
# The following program only has one output, and that output
# is the ION which we previously wrote to notate ω. Since all
# the outputs of the following program are IONs, the following
# program is an ION.
output("""
X=\"\"

while True:
    output(X)
    X = \"output(\'\" + escape(X) + \"\')\"
""")