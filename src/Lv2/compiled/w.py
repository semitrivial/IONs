# We begin with the program we left off with at the end of
# Level 1. This program notates ω, the smallest infinite
# ordinal. We would like to move beyond ω. How can we go
# beyond infinity?
X=""

while True:
    output(X)
    X = "output('" + escape(X) + "')"