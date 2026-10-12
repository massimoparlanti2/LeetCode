class Solution:

  def queryString(self, s: str, n: int) -> bool:
    # A string of length <= 1000 cannot contain all binary representations for n > 1000
    if n > 1000:
      return False

    # Check only from n down to n // 2 + 1
    for i in range(n, n // 2, -1):
      if bin(i)[2:] not in s:
        return False

    return True