class solution(object):
   def generateparentesis(self,n):
      """
      :type n: int
      :rtype: list[str]
      """
      result = []
      self.generateparanthesisUtil(n,n,"",result)
      return result
   def genetateparenthesisUtil(self,left,right,temp,result):
      if left == 0 and right == 0:
         result.append(temp)
         return
      if left>0:
         self.generateparaenthesisUtil(left-1,right,temp+'(',result)
      if right > left:
         self.generateparaenthesisUtil(left,right-1,temp + ')',result)
ob = solution()
n = int(input("enter the number:"))
print("ob.generateparenthesis(n)")
