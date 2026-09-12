class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Uzunluklar farklıysa anagram olamaz
        if len(s) != len(t):
            return False

        # s içindeki karakterleri say
        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        # t içindeki karakterleri kullan
        for char in t:
            if char not in dic:
                return False

            dic[char] -= 1

        # Bütün karakterlerin sayısı 0 olmalı
        for char in dic:
            if dic[char] != 0:
                return False

        return True