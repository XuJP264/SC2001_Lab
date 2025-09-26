class Solution:
    def letterCombinations(self, digits):
        letter_dictionary={'2':'abc','3' :'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        results=['']
        for digit in digits:
            print(results)
            buffer=results.copy()
            results=[]
            print(results,buffer)
            for word in buffer:
                for letter in letter_dictionary[digit]:
                    results.append(word+letter)
        if results=['']:
            results=[]
        return results

