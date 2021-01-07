import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
#스플릿을 사용하여 단어를 편리하게 입력했다
def getRandomWord(wordlist):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    #랜덤으로 수를 하나 뽑았다. 다만, 배열은 0부터 시작하니 1을 빼주어 배열과 수를 일치시켰다. wordList에는 인풋이 들어올거고, 그 인풋에서 1을 빼서 배열과 맞출거다. 페러미터는 곧 인풋.
    return wordList[wordIndex]
#wordIndex가 랜덤으로 수를 뽑아 글자수를 리턴해 주었다.
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len (missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    #this for loop is going to display the missed letters.