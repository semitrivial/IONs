import sys

if len(sys.argv) != 2:
    print("Which level would you like to test?")
    exit(0)

if sys.argv[1] == "1":
    from Lv1.test import test_level_1
    test_level_1()

if sys.argv[1] == "2":
    from Lv2.test import test_level_2
    test_level_2()

