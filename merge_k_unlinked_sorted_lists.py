'''
    
    Merge k sorted lists and return it as one sorted list.

    
    Example:

        Input:
            [
                1->4->5,
                1->3->4,
                2->6
            ]
        Output: 1->1->2->3->4->4->5->6
        
'''


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists
        :rtype: list
        """

        if lists is None:
            return None

        if 0 == len(lists):
            return None


        def findInsertIndex(data, num):

            if num <= data[0]:
                return 0

            if num >= data[-1]:
                return len(data)

            idx = len(data) - 1

            while idx >= 0:

                if data[idx] > num:
                    idx -= 1
                else:
                    return idx + 1


        def insertItemToList(item, ret):

            idx = findInsertIndex(ret, item)
            ret = ret.insert(idx, item)



        def insertListAToListB(listA, listB):
            return listB + listA


        ret = None

        for l in lists:

            if 0 != len(l):

                if ret is None:
                    ret = l
                    continue


            if l[-1] <= ret[0]:
                ret = insertListAToListB(l, ret)

            elif l[0] >= ret[-1]:
                ret = insertListAToListB(l, ret)

            else:

                for item in l:
                    insertItemToList(item, ret)


        return ret


if __name__ == '__main__':


    lists = [[1,4,5],
             [1,3,4],
             [2,6],
             [0, 123],
             [-10, 123]]

    assert [-10,0,1,1,2,3,4,4,5,6,123,123] == Solution().mergeKLists(lists)


