class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Tạo một từ điển để lưu giá trị và vị trí
        seen = {}
        # Duyệt qua từng số trong danh sách
        for i, num in enumerate(nums):
            # Tính số còn thiếu để đạt được tổng target
            complement = target - num
            # Kiểm tra xem số còn thiếu có trong từ điển chưa
            if complement in seen:
                return [seen[complement], i]
            # Lưu số hiện tại và vị trí của nó vào từ điển
            seen[num] = i
