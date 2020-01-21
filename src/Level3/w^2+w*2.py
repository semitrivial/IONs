## w^2+w*2.py
# The program below is the resulting of taking w.py and changing the
# initial value of X so that instead of starting as the empty string,
# X starts as the contents of w^2+w.py. Convince yourself that this
# program outputs ordinals notating ω^2+ω, ω^2+ω+1, ω^2+ω+2, etc.,
# so this program itself notates ω^2+ω*2. NOTE: If you see "get_file",
# that's a utility function we use to compile an ION. The fully
# compiled ION is obtained by replacing the get_file with an escaped
# copy of the contents of w^2+w.py.
X=<INSERT_FILE w^2+w.py>

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"