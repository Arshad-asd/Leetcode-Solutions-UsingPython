                                            #LEETCODE ARAY QUESTIONS SOLVED

'''--------------------------------------------------------------------------------------------'''

# QUESTIOIN NO : 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False
        
        return increasing or decreasing

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count_map = {}
        n = len(nums)
        target_count = n // 2
        
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] == target_count:
                return num


'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 1128. Number of Equivalent Domino Pairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counts = {}
        total_pairs = 0
        for domino in dominoes:
            domino.sort()
            identifier = tuple(domino)
            domino_counts[identifier] = domino_counts.get(identifier,0) + 1
        for count in domino_counts.values():
            total_pairs += (count * (count -1)) // 2
        return total_pairs

'''--------------------------------------------------------------------------------------------'''


# QUESTION NO: 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
            j +=1
        return i
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            lists = [[1],[1,1]]
            for i in range(2,numRows):
                temp = []
                for j in range(0,i+1):
                      if j==0 or j==i:
                        temp.append(1)
                      else:
                        temp.append(lists[i-1][j-1]+lists[i-1][j])
                lists.append(temp)
            return lists

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1) , set(nums2)
        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2Set:
                res1.add(n)
        
        for n in nums2:
            if n not in nums1Set:
                res2.add(n)

        return [list(res1), list(res2)]

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2824. Count Pairs Whose Sum is Less than Target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if nums[i] + nums[j] < target:
                   count += 1
        return count

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 1200. Minimum Absolute Difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
       arr.sort()
       min_dif = float('inf')
       res = []
       for i in range(1 ,len(arr)):
           cur = abs(arr[i] - arr[i -1])
           if min_dif > cur:
               min_dif = cur
               res = [[arr[i-1], arr[i]]]
           elif min_dif == cur:
               res.append([arr[i-1],arr[i]])
       return res
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2828. Check if a String Is an Acronym of Words

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
         return ''.join(word[0] for word in words) == s


# QUESTION NO : 2859. Sum of Values at Indices With K Set Bits

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
       return sum(x for i,x in enumerate(nums) if bin(i).count('1') == k)
                
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2798. Number of Employees Who Met the Target

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                count += 1
        return count

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2553. Separate the Digits in an Array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] > 9:
                temp = [int(char) for char in str(nums[i])]
                res.extend(temp)
            else:
                res.append(nums[i])
        return res
        

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return   [abs(sum(nums[:i + 1])-sum(nums[i:])) for i in range(len(nums))]
    

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        store = {}
        sort_arr = sorted(set(arr))

        for i in range(len(sort_arr)):
            store[sort_arr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = store[arr[i]]

        return arr


'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2535. Difference Between Element Sum and Digit Sum of an Array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        temp = [int(digit) for number in nums for digit in str(number)]
        return sum(nums) - sum(temp)

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO : 2418. Sort the People

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       _,names = zip(*sorted(zip(heights,names),reverse = True))
       return list(names)

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and  j != i:
                    count += 1
            result.append(count)
        return result

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 1389. Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
       target = []
       for n,i in zip(nums,index):
           target.insert(i,n)
       return target

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO : 2114. Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in range(len(sentences)):
                array = sentences[i].split(' ')
                if len(array) > count:
                    count = len(array)
        return count

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO : 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        res = ''
        for i in range(k):
           res += arr[i]
           if k-1!=i:
               res += ' '
        return res

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO : 1920. Build Array from Permutation
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       ans = []
       for i in range(len(nums)):
           ans.append(nums[nums[i]])
       return ans

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 2367. Number of Arithmetic Triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        seen = set()
        for n in nums:
            seen.add(n)
            if n-diff in seen and n-2*diff in seen:
                count += 1
        return count

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] == k:
                    count += 1
        return count 

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1313. Decompress Run-Length Encoded List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        generated = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            generated += [val] * freq
        return generated

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER :  2500. Delete Greatest Value in Each Row 

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid[0])
        for i in range(n):
            maxi = 0
            for j in grid:
                new = max(j)
                maxi = max(maxi,new)
                j.remove(new)
            res += maxi
        return res


'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER : 1748. Sum of Unique Elements


#Method 1

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            if nums.count(i)==1:
                sum += i
        return sum

#Method 2

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            flag = 0
            for j in range(len(nums)):
                if nums[i]==nums[j] and i !=j:
                    flag =  1
            if flag==0:
                sum += nums[i]
        return sum



'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2011. Final Value of Variable After Performing Operations


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == '--X' or i == 'X--':
                x -= 1
            if i == '++X' or i == 'X++':
                x += 1
        return x

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2913. Subarrays Distinct Element Sum of Squares I
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
         res = []
         for i in range(len(nums)):
             for j in range(i,len(nums)+1):
                 res.append(len(set(nums[i:j]))**2)
         return sum(res)
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2778. Sum of Squares of Special Elements

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                sum = sum + nums[i] **2
        return sum


'''--------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 1051. Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
         nums = sorted(nums)
         res = []
         for i in range(len(nums)):
             if nums[i] == target:
                res.append(i)
         return res

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
          count = 0
          for i in range(len(startTime)):
              if endTime[i] >= queryTime and startTime[i] <= queryTime:
                  count += 1
          return count

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2357. Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniq_non_zero = set()
        for num in nums:
            if num == 0:
                continue
            uniq_non_zero.add(num)
        return len(uniq_non_zero)


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count_operations = 0

        while any(num != 0 for num in nums):
            smallest_non_zero = float('inf')

            # Find the smallest non-zero element
            for num in nums:
                if num != 0 and num < smallest_non_zero:
                    smallest_non_zero = num

            # Subtract the smallest non-zero element from each non-zero element in the list
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= smallest_non_zero

            count_operations += 1

        return count_operations

'''--------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 2154. Keep Multiplying Found Values by Two
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original

'''--------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 2529. Maximum Count of Positive Integer and Negative Integer

#Method 1
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        max_count = 0
        min_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] > 0:
                    min_count += 1
                else:
                    max_count += 1
        return max_count if max_count >= min_count else min_count

#Method 2
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l1 = list(filter(lambda x: x>0, nums))
        l2 = list(filter(lambda x: x<0, nums))
        return max(len(l1),len(l2))
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2124. Check if All A's Appears Before All B's
class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == 'b':
                if 'a' in s[i+1:]:
                    return False
                return True
            elif 'b' not in s:
                return True
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  :1827. Minimum Operations to Make the Array Increasing
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                temp = nums[i]
                nums[i] += (nums[i-1] - nums[i]) + 1
                count += nums [i] - temp
        return count

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2176. Count Equal and Divisible Pairs in an Array
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res.append([i,j])
        return len(res)

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2942. Find Words Containing Character

#Method 1
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            for j in words[i]:
                 if j == x:
                     res.append(i)
        return set(res)

#Metod 2
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2578. Split With Minimum Sum
class Solution:
    def splitNum(self, num: int) -> int:
        split = sorted([int(i) for i in str(num)])
        num1 = ''
        num2 = ''
        for ind, val in enumerate(split):
            if ind%2 == 0:
                num1 += str(val)
            else:
                num2 += str(val)
        return int(num1)+int(num2)

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
           for j in range(len(nums)):
               if nums[i] == nums[j] and i < j:
                   count += 1
        return count
'''--------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            x,y = i,n+i
            if x != n:
                res.append(nums[x])
                res.append(nums[y])
        return res

'''--------------------------------------------------------------------------------------------'''

#QUESTION NUMBER  : 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
                res.append(sum)
        return max(res)
        
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2433. Find The Original Array of Prefix Xor
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]] + [pref[i]^pref[i-1] for i in range(1,len(pref))]
        return res
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 1863. Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res =0
        for x in nums:
            res |= x
        return res*(2**(len(nums)-1))

'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 2951. Find the Peaks
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peak = []
        for i in range(1,len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                peak.append(i)
        return peak
            
'''--------------------------------------------------------------------------------------------'''
#QUESTION NUMBER  : 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left,right = 0,len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid+1
        return left

#QUESTION NUMBER  : 912. Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1:
            mid = len(nums)//2
            left = nums[mid:]
            right = nums[:mid]
            self.sortArray(left)
            self.sortArray(right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1
        return nums

#QUESTION NUMBER  : 692. Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = {}
        for key in words:
            if key in seen:
                seen[key] +=1
            else:
                seen[key] =1
        sorted_words = sorted(seen.keys(), key=lambda x: (-seen[x], x))
        return sorted_words[:k]

#QUESTION NUMBER  : 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[-k]


#QUESTION NUMBER  : 2053. Kth Distinct String in an Array
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for key in arr:
             if key in seen:
                 seen[key] +=1
             else:
                 seen[key] = 1
        sorted_arr = sorted(seen.keys(),key = lambda item:seen[item])
        for i in arr:
                if seen[i]==1:
                    k-=1
                    if k==0:
                        return i
        return ""

#QUESTION NUMBER  : 1588. Sum of All Odd Length Subarrays
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                result +=sum(arr[i:j+1])
        return result

#QUESTION NUMBER  : 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1        

#QUESTION NUMBER  : 2974. Minimum Number Game
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums

#QUESTION NUMBER  : 179. Largest Number
class Solution:
    def compare(self, x: str, y: str) -> int:
        return int(str(y) + str(x)) - int(str(x) + str(y))

    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(nums,key=cmp_to_key(self.compare))
        ans = ''.join(str(i) for i in sorted_nums)
        return ans if ans[0] != '0' else '0'

#QUESTION NUMBER  : 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

#QUESTION NUMBER  :  49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())

#QUESTION NUMBER  : 3005. Count Elements With Maximum Frequency
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {}
        max_freq = 0
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            max_freq = max(max_freq, frequency[num])
        
        count_max_freq = sum(1 for freq in frequency.values() if freq == max_freq)
        
        return max_freq * count_max_freq
#QUESTION NUMBER  : 225. Implement Stack using Queues
class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped_element = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self) -> int:
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        top_element = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self) -> bool:
        return not self.queue1
#QUESTION NUMBER  : 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

#QUESTION NUMBER  : 2610. Convert an Array Into a 2D Array With Conditions
from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        max_freq = max(freq_map.values())
        result = [[] for _ in range(max_freq)]
        
        row = 0
        for num, freq in freq_map.items():
            for _ in range(freq):
                result[row % max_freq].append(num)
                row += 1
        
        return result
#QUESTION NUMBER  :  2149. Rearrange Array Elements by Sign
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posative = []
        negative = []
        result = []
        for i in range(len(nums)):
            if nums[i] >0:
                posative.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums) // 2):
            result.append(posative[i])
            result.append(negative[i])
        return result