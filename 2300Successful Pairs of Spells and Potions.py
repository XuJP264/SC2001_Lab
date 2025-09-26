def remove_duplicates_and_cumulative_count(sorted_array):
    """
    输入一个升序数组，返回去重后的数组和每个元素对应的累计元素个数数组。

    参数:
        sorted_array: List[int] - 升序排序的整数数组

    返回:
        Tuple[List[int], List[int]] - (去重数组, 累计元素个数数组)

    示例:
        输入: [1, 1, 2, 3, 3, 3]
        输出: ([1, 2, 3], [2, 3, 6])
        解释: 1出现2次→2; 2出现1次，累计2+1=3; 3出现3次，累计2+1+3=6
    """
    if not sorted_array:  # 处理空数组
        return [], []

    unique_elements = []  # 去重后的数组
    cumulative_counts = []  # 累计元素个数数组
    current_element = sorted_array[0]  # 当前处理的元素
    current_count = 1  # 当前元素的计数
    total_count = 1  # 累计元素总数

    # 从第二个元素开始遍历
    for i in range(1, len(sorted_array)):
        if sorted_array[i] == current_element:
            # 当前元素与前一个相同，计数加1
            current_count += 1
            total_count += 1
        else:
            # 遇到新元素，保存当前元素和累计计数
            unique_elements.append(current_element)
            cumulative_counts.append(total_count)
            current_element = sorted_array[i]  # 更新当前元素
            current_count = 1  # 重置当前元素计数
            total_count += 1  # 更新累计总数

    # 处理最后一个元素
    unique_elements.append(current_element)
    cumulative_counts.append(total_count)

    return unique_elements, cumulative_counts
class Solution:
    def binarySearch(self,target,potions):
        left=0
        right=len(potions)-1
        mid=(left+right)//2
        while left<=right:
            mid = (left + right) // 2
            if potions[mid]==target:
                return mid
            if potions[mid]<target:
                left=mid+1
            if potions[mid]>target:
                right=mid-1
        return mid
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        new_potions,numbers=remove_duplicates_and_count(potions)

        for i in range(len(spells)):
            target= float(success/spells[i])
            result=self.binarySearch(target,new_potions)
            if new_potions[result]<target:
                ansI=length-numbers[result]
            elif new_potions[result]>=target and result==0:
                ansI = length
            elif new_potions[result]==target:
                ansI=length-numbers[result-1]
            else:
                ansI=length-numbers[result-1]
            ans.append(ansI)
        return ans