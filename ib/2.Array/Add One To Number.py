'''
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of
the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you
 should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words,
is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other
words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before
the most significant digit.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        return [i for i in str(int(''.join(map(str, A)))+1)]

# test
print(Solution().plusOne([1, 2, 3]))
