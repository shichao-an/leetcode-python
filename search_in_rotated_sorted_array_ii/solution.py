class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if target == A[mid]:
                return True
            # Left part is sorted
            if A[mid] > A[right]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right part is sorted
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right -= 1
        return False
