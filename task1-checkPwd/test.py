import unittest
from solution import solution

class CheckPwdTests(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        assert solution('ULFFunH8ni') == True

    def test2(self):
        assert solution('aaaaaaaaaaaaaaaaaaaaa') == False

    def test3(self):
        assert solution('aA1') == False

    def test4(self):
        assert solution('awzbdzkfz') == False

    def test5(self):
        assert solution('RCAGOSHTTS') == False

    def test6(self):
        assert solution('6691219721') == False

    def test7(self):
        assert solution('PVlppfwrT') == False

    def test8(self):
        assert solution('45ae5lkgz') == False

    def test9(self):
        assert solution('1cmuPF1Ycz') == True

    def test10(self):
        assert solution('Pv4HdnUNb') == False

    def test11(self):
        assert solution('jRNfXg6CdM15SLChALq') == True

    def test12(self):
        assert solution('HZeLrcRR3NU5KprAybp') == True

    def test13(self):
        assert solution('aaaaaaaaaa1A') == True

    def test14(self):
        assert solution('aaaaaaaaa1Za') == True

    def test15(self):
        assert solution('aaaaaaaaa9Aa') == True

    def test16(self):
        assert solution('AAAAAAAAA1zA') == True

    def test17(self):
        assert solution('1') == False

    def test18(self):
        assert solution('vcugdgywnlj') == False

    def test19(self):
        assert solution('abcdef1') == False

    def test20(self):
        assert solution('ABCDEF') == False

    def test21(self):
        assert solution('HJKKJDSHJKHDKWJWDW') == False

    def test22(self):
        assert solution('123456') == False

    def test23(self):
        assert solution('123456789012') == False

    def test24(self):
        assert solution('fsDSkjSD') == False

    def test25(self):
        assert solution('fsDSkjSDDSJhjhjd') == False

    def test26(self):
        assert solution('gfh123') == False

    def test27(self):
        assert solution('erer798rew9rew9r7ew987rw') == False

    def test28(self):
        assert solution('DHJK8768D') == False

    def test29(self):
        assert solution('DHJK87DSKJHWW68D') == False

    def test30(self):
        assert solution('Fa11con77') == False

    def test31(self):
        assert solution('Fa11con77YES') == True

    def test32(self):
        assert solution('Fa11con777') == True

    def test33(self):
        assert solution('aaaaaaaaaaaaaaaaaaaaaaaaaaSSSSSSSSSSSSSSSSSSSSSSSSS111111111111') == True

    def test34(self):
        assert solution('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') == True

    def test35(self):
        assert solution('9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba') == True

    def test36(self):
        assert solution('IAKxnvZokrsWP1S0NCfJq4pti9Q6c8gXmB2alzuwUVRbD73OGE5HjMTFYLyhed') == True


if __name__ == "__main__":
    unittest.main()