class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        given a list >= length 1, return k most frequent elements
        k >= 1 and <= distinct elements in the array

        Questions:
        - Will there ever be ties and tie breakers? ex: we have 3 copies of both 4 and 5, k = 1, we would need only pick one
        - Will the input array ever be empty
        - Will the array be sorted

        Edge Cases:
        - k = len(nums)
        - len(nums) = 1
        - elements scattered throughout 
        - elements clustered at beginning
        - elements clustered at end

        Brute Force:
        1. count each element in array with HashMap 0(n)
        2. find the k most frequent elements O(m * k) - O(n^2)
            * scan through list, find max
            * add max to output, remove from HashMap
            * repeat k times

        problem with brute force:
            * have to scan through distinct elements (m) 
            many times

        Solution: O(nlgn) - O(n) extra space
            * hash map
            * order map by frequency O(nlgn)
            * get k elements
                        
        Observations: 
        - Order of the elements matters
        - If we sorted the array we could easily see count(el)
        - We need O(k) data structure to store output

        loop invariant:
        - if we have array of len k sorted by frequency
        - we only need to compare to smallest element in arr
        - that is element being popped
        """
        # get the frequencies - O(n)
        freq = {}
        for el in nums:
            if el not in freq:
                freq[el] = 0
            freq[el] += 1

        freq_arr = [] 
        # map frequencies into array - O(n)
        for key, val in freq.items():
            freq_arr.append((key, val))

        # sort frequencies array in place - O(nlgn)
        freq_arr.sort(key=lambda item:item[1], reverse=True)

        # return first k elements
        output = []
        for i in range(k):
            output.append(freq_arr[i][0])

        return output
