class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        encodings = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        map = dict()
        for letter, encoding in zip(letters,encodings):
            map[letter] = encoding
            
        for i in range(len(words)):
            words[i] = "".join([map[c] for c in words[i]])
        
        return len(set(words))