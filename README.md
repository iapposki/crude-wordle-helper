# crude-wordle-helper

Takes in  'words.txt' file as initial list of words, narrows down the words to five letter words and saves it to a new file 'five-words.txt'. 
Run 'code.py' to run the helper. The input takes in rules as : Input data as (1)letter followed by its correct position or (2)only letter if it is not in the word or (3)letter followed by its incorrect position followed by '.' 
For example : 'd2 f g5.'  rule means 'd' is at the correct position 2, 'f' is not in the word to be guessed and 'g' is is the word but not at the position 5.

Currently doesn't support multiple letter cases in the single word.
