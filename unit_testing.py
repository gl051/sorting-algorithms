import unittest
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def run_sorting(iarray):
    return bubble_sort(iarray)
    #return quicksort(iarray)
    #return insertion_sort(iarray)
    #return merge_sort(iarray)

class TestSorting(unittest.TestCase):

    # Verification logic is all the same, I put it here
    def __verify(self, test_array, result_array):
        if len(result_array) != len(test_array):
            self.RuntimeError('The two arrays have different lenght')
        else:
            for i in range(0, len(result_array)-1):
                self.assertTrue(result_array[i] <= result_array[i+1])

    def test_1(self):
        test_array = [56, 7, 89, 2, 9, 12]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_2(self):
        test_array = []
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_3(self):
        test_array = [1, 2, 3, 4, 5, 6]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_4(self):
        test_array = [67, 4, 23, 56, 56, 1, 212, 567, 78, 90, 12, 45, 67, 0]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_5(self):
        test_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_6(self):
        test_array = [5, 5, 5, 5]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

    def test_7(self):
        test_array = [10, 8, 10, 8, 98, 23, 67, 12, 56, 1, 89, 100, 2]
        result_array = run_sorting(test_array)
        self.__verify(test_array, result_array)

if __name__ == '__main__':
    unittest.main()
