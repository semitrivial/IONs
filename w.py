X="""
""".strip()

while True:
    output(X)
    X = "output(\"" + escape(X) + "\")"