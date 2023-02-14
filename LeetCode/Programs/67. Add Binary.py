class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a) > len(b): a,b = b,a
    lena,lenb = len(a),len(b)
    xs = ['0']*(lenb-lena)
    a = ''.join(xs) + a

    res = ''
    sumCase = {'000':['0','0'], '010':['1','0'], '001':['1','0'], '011':['0','1'], '100':['1','0'], '110':['0','1'], '101':['0','1'], '111':['1','1']}
    carry = '0'
    lenb -= 1

    while lenb > -1:
        resBit, carry = sumCase[carry+a[lenb]+b[lenb]]
        res = resBit+res
        lenb -= 1
    
    return carry+res if carry=='1' else res