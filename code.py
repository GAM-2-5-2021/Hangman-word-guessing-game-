import random

word_list = ['Aatrox', 'Ekko', 'Jinx', 'Miss Fortune', 'Shen', 'Varus', 'Ahri', 'Elise', 'Kalista', 'Mordekaiser', 
                 'Shyvana', 'Vayne', 'Akali', 'Evelynn', 'Karma', 'Morgana' , 'Singed', 'Veigar', 'Alistar', 'Ezreal', 
                 'Karthus', 'Nami', 'Sion', 'Vel Koz', 'Amumu', 'Fiddlesticks', 'Kassadin', 'Nasus', 'Sivir', 'Vi', 'Anivia', 
                 'Fiora', 'Katarina', 'Nautilus', 'Skarner', 'Viktor', 'Annie', 'Fizz', 'Kayle', 'Nidalee', 'Sona', 'Vladimir' ,
                 'Ashe', 'Galio', 'Kennen', 'Nocturne', 'Soraka', 'Volibear', 'Aurelion Sol', 'Gangplank', 'Kha Zix', 
                 'Nunu', 'Swain', 'Warwick', 'Azir', 'Garen', 'Kindred', 'Olaf', 'Syndra', 'Wukong', 'Bard', 'Gnar', 'Kled', 'Orianna', 
                 'Tahm Kench', 'Xerath', 'Blitzcrank', 'Gragas', 'Kog’Maw', 'Pantheon', 'Taliyah', 'Zin Zhao', 'Brand', 'Graves',
                 'LeBlanc', 'Poppy', 'Talon', 'Yasuo', 'Braum', 'Hecarim', 'Lee Sin', 'Quinn', 'Taric', 'Yorick', 'Caitlyn', 
                 'Heimerdinger', 'Leona', 'Rammus', 'Teemo', 'Zac', 'Camille', 'Illaoi', 'Lissandra', 'Rek Sai', 'Thresh', 'Zed',
                 'Cassiopeia', 'Irelia', 'Lucian', 'Renekton', 'Tristana', 'Ziggs', 'Cho Gath', 'Ivern', 'Lulu', 'Rengar', 'Trundle',
                 'Zilean', 'Corki', 'Janna', 'Lux', 'Riven', 'Tryndamere', 'Zyra', 'Darius', 'Jarvan IV', 'Malphite', 'Rumble', 
                 'Twisted Fate', 'Diana', 'Jax', 'Malzahar', 'Ryze', 'Twitch', 'Dr. Mundo', 'Jayce', 'Maokai', 'Sejuani', 'Udyr', 
                 'Draven', 'Jhin', 'Master Yi', 'Shaco', 'Urgot']

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    print("Let's play Hangman!")
    print('There is a twist though, instead of everyday normal words, ')
    print('you will be tested your champion knowledge from a video game called Leuge of Legends!')
    print('Good luck!')
    print('\n')
    print('Your word contains', len(word), 'letters.')
    tries = int(input('How many tries would you like to have? '))
    print('You have', tries, 'tries left')
    print(word_completion)
    while not guessed and tries > 0:
        guess = input('Enter your guess here (word/letter): ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Try not to guess', guess, 'more than once, ok?')
            elif guess not in word:
                print(guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Nicely done', guess, 'is in the word.')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Wooah buddy, you already guessed', guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess.')
        print('You still have', tries, 'tries.')
        print(word_completion)
        print('\n')
    if guessed:
        print('Alright great job!, even though', word, 'was an easy one...')
    else:
        print('Aww,' , word , 'was an easy champion to guess...')
        print('Better luck next time buddy!')
def main():
    word = get_word()
    play(word)
    while input('Play Again? (Y/N) ').upper() == 'Y':
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

    word = random.choice(word_list)
    return word.upper()

