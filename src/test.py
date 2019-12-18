import sys

from util import *
from compile import compile_files

if len(sys.argv) != 2:
    print("Which level would you like to test?")
    exit(0)

print("Compiling files...")

set_test_level(int(sys.argv[1]))

if sys.argv[1] == "1":
    from Lv1.test import test_level_1
    test_level_1()

if sys.argv[1] == "2":
    from Lv2.test import test_level_2
    test_level_2()

if sys.argv[1] == "3":
    from Lv3.test import test_level_3
    test_level_3()

if sys.argv[1] == "4":
    from Lv4.test import test_level_4
    test_level_4()

if sys.argv[1] == "5":
    from Lv5.test import test_level_5
    test_level_5()

if sys.argv[1] == "6":
    from Lv6.test import test_level_6
    test_level_6()