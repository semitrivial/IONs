import sys

from util import *
from compile import compile_files

print("Compiling files...")
compile_files()

if len(sys.argv) != 2:
    from Level1.test import test_level_1
    from Level2.test import test_level_2
    from Level3.test import test_level_3
    from Level4.test import test_level_4
    from LevelOmega.test import test_level_omega
    print("Testing Level 1")
    set_test_level(1)
    test_level_1()
    print("Testing Level 2")
    set_test_level(2)
    test_level_2()
    print("Testing Level 3")
    set_test_level(3)
    test_level_3()
    print("Testing Level 4")
    set_test_level(4)
    test_level_4()
    print("Testing Level Omega")
    set_test_level("omega")
    test_level_omega()
    sys.exit()

set_test_level(int(sys.argv[1]))

if sys.argv[1] == "1":
    from Level1.test import test_level_1
    test_level_1()

if sys.argv[1] == "2":
    from Level2.test import test_level_2
    test_level_2()

if sys.argv[1] == "3":
    from Level3.test import test_level_3
    test_level_3()

if sys.argv[1] == "4":
    from Level4.test import test_level_4
    test_level_4()

if sys.argv[1] == "5" or sys.argv[1].lower() == "omega":
    from LevelOmega.test import test_level_omega
    test_level_omega()
