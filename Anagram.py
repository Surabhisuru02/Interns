def group_anagrams(words):#define function  
    anagrams = {}#create empty dictionary to store output 
    for word in words:#iterate them through each word 
        # Sort the letters in the word to create a key(key should be unique) 
        key = ''.join(sorted(word))# takes a word, sorted(word)sorts its letters 
alphabetically, 
        #''.join used tocombines them into a single string(i.e.,key).Uses the string 
"" (empty string) 
        # Add the word to the list of anagrams for this key. 
        #add word to anagram list 
        if key in anagrams:#Check if the key is Already a Key 
            anagrams[key].append(word)#Add the Word to the List of Anagrams 
        else: 
anagrams[key] = [word]#Create a New List if the Key Doesn't Exist 
# return the list of anagram groups 
return list(anagrams.values()) 
#implementation 
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] 
print(group_anagrams(words))
