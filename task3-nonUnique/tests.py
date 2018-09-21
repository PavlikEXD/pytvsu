import unittest
from solution import solution

class NonUniqueBasicTests(unittest.TestCase):
    def test1(self):
        assert solution([1,2,3,1,3]) == [1,3,1,3]

    def test2(self):
        assert solution([1,2,3,4,5]) == []

    def test3(self):
        assert solution([5,5,5,5,5]) == [5,5,5,5,5]

    def test4(self):
        assert solution([10,9,10,10,9,8]) == [10,9,10,10,9]

    def test5(self):
        assert solution([2,2,3,2,2]) == [2,2,2,2]

    def test6(self):
        assert solution([10,20,30,10]) == [10,10]

    def test7(self):
        assert solution([7]) == []

    def test8(self):
        assert solution([0,1,2,3,4,0,1,2,4]) == [0,1,2,4,0,1,2,4]

    def test9(self):
        assert solution([99,98,99]) == [99,99]

    def test10(self):
        assert solution([0,0,0,1,1,100]) == [0,0,0,1,1]

    def test11(self):
        assert solution([0,0,0,-1,-1,100]) == [0,0,0,-1,-1]


class NonUniqueExtraTests(unittest.TestCase):
    def test1(self):
        assert solution([-10,10,0]) == []
    
    def test2(self):
        assert solution([-10,10,0,-1,-1,1,1]) == [-1,-1,1,1]
    
    def test3(self):
        assert solution([1000000,999999,1999999,2000000,2000000]) == [2000000,2000000]
    
    def test4(self):
        assert solution([1,1,2,2,3,3,-1,-1,-2,-2,-3,-3,0]) == [1,1,2,2,3,3,-1,-1,-2,-2,-3,-3]
    
    def test5(self):
        assert solution([x for x in range(1000)]) == []
    
    def test6(self):
        assert solution([0] * 500) == [0] * 500
    
    def test7(self):
        assert solution([x for x in range(-100, 1)] + [x for x in range(0, 101)]) == [0,0]
    

if __name__ == "__main__":
    unittest.main()