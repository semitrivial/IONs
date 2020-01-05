## w.py
# This program outputs computer programs equivalent to
# 0.py, 1.py, 2.py, 3.py, and so on forever.
#
# The Intuitive Ordinal Notations (IONs) are defined so that:
#   "For any computer program P, if all the outputs of P are
#   IONs, then P itself is an ION."
#
# By induction, all the outputs of this program are IONs.
# Therefore, this program is an ION.
# It notates ω ("omega"), the smallest infinite ordinal.
#
# See ../util.py for definition of the "escape" function.
# For convenience, we will always assume this "escape"
# function is defined in the background.
X=""

while True:
    output(X)
    X = "output('" + escape(X) + "')"