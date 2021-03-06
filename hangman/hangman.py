import string


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = True
    for letter in secretWord:
        result = letter in lettersGuessed
        if result == False:
            break

    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''

    secretLetters = list(secretWord)
    for i in range(len(secretLetters)):
        if (secretLetters[i] not in lettersGuessed):
            secretLetters[i] = '_'

    result = ''.join(secretLetters)

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ''
    alphabet = string.ascii_lowercase

    lettersAlphabet = list(alphabet)
    for letter in lettersGuessed:
        if letter in lettersAlphabet:
            lettersAlphabet.remove(letter)

    result = ''.join(lettersAlphabet)

    return result


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    welcomeMessage = 'Welcome to the game, Hangman!'
    guessingMessage = 'I am thinking of a word that is 1 letter long.'
    splitterLine = '-------------'

    numberAttempts = 8
    attemptsLeftTemplate = 'You have {} guesses left.'
    avaliableLetters = string.ascii_lowercase
    availableLettersTemplate = 'Available letters: {}'
    inputMessage = 'Please guess a letter: '

    letters = list()
    lettersGuessed = list()

    if len(secretWord) > 1:
        guessingMessage = 'I am thinking of a word that is {} letters long.'.format(
            len(secretWord))

    print(welcomeMessage)
    print(guessingMessage)
    print(splitterLine)

    while numberAttempts > 0:
        print(attemptsLeftTemplate.format(numberAttempts))
        print(availableLettersTemplate.format(avaliableLetters))
        letter = input(inputMessage).lower()

        if letter in letters:
            print("Oops! You've already guessed that letter: {}".format(
                getGuessedWord(secretWord, letters)))
        else:
            letters.append(letter)

            if letter in secretWord:
                if letter in lettersGuessed:
                    print("Oops! You've already guessed that letter: {}".format(
                        getGuessedWord(secretWord, letters)))
                else:
                    lettersGuessed.append(letter)
                    print('Good guess: {}'.format(
                        getGuessedWord(secretWord, letters)))
            else:
                print('Oops! That letter is not in my word: {}'.format(
                    getGuessedWord(secretWord, letters)))
                numberAttempts -= 1

            avaliableLetters = getAvailableLetters(letters)

            if isWordGuessed(secretWord, lettersGuessed):
                print(splitterLine)
                print('Congratulations, you won!')
                break

        print(splitterLine)

    if numberAttempts == 0:
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
