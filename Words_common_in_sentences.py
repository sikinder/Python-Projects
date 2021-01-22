sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

set1 = set(sentence1.split())
set2 = set(sentence2.split())
    
words_common = sorted(list(set1&set2))
words_not_common = sorted(list(set1^set2))
   
print("The words that are present in both sentences are : \n", words_common)
print("The words that are in only one of the sentences are : \n", words_not_common)  
