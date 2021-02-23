# Merge two sorted lists. Merge two sorted linked lists and return it as a sorted list.

class Solution(object):
    def mergeSortedLists(self, l1, l2):
        """
        :type l1: []
        :type l2: []
        :rtype:
        """

        output = []
        index1 = 0
        index2 = 0
        while (index1 < len(l1) and index2 < len(l2)):
            if l1[index1] <= l2[index2]:
                output.append(l1[index1])
                index1 += 1
            else:
                output.append(l2[index2])
                index2 += 1

        if (index1 < len(l1)):
            output += l1[index1:]
        else:
            output += l2[index2:]

        return output

solution = Solution()
l1 = [1,4,5,10,15,20]
l2 = [2,3,4]
print(solution.mergeSortedLists(l1, l2))