class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		if len(nums)<4: return []
		if len(nums) == 4:  return [[_ for _ in nums]] if sum(nums) == target else []
	
		nums = sorted(nums)
		# print(nums)
	
		p1,p2 = 0,1
		# retList = []
		retSet = set()
	
		def searchP34(l,r,t):
			while r>l:
				tSum = nums[r]+nums[l]
				# print(l,r,tSum)
				if tSum == t:		return l,r
				if tSum > t:		r -= 1
				else:   l += 1
				# print(l,r,'c')
			return l,r
				
	
		while p1<len(nums)-3:
			# print(p1,p2)
			while p2<len(nums)-2:
				p3,p4 = searchP34(p2+1,len(nums)-1,target-(nums[p1]+nums[p2]))
				while p3<p4:
					if ((nums[p1],nums[p2],nums[p3],nums[p4])) not in retSet:	
						# retList.append([nums[p1],nums[p2],nums[p3],nums[p4]])
						retSet.add((nums[p1],nums[p2],nums[p3],nums[p4]))
					p3,p4 = searchP34(p3+1,p4-1,target-(nums[p1]+nums[p2]))
				p2 += 1
			p1 += 1
			p2 = p1+1
	
		# print(retList)
		return list(retSet)