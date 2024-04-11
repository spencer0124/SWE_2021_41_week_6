from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    
    # 딕서녀리
    # 키: 이전에 탐색한 숫자들의 값
    # 값: 그 숫자들의 인덱스
    MapDictionary = {}
    
    for i, n in enumerate(nums) :
        diff = target - n
        if diff in MapDictionary:
            return [MapDictionary[diff], i]
        MapDictionary[n] = i