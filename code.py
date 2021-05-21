import random

word_list_lol = ['Aatrox', 'Ekko', 'Jinx', 'Miss Fortune', 'Shen', 'Varus', 'Ahri', 'Elise', 'Kalista', 'Mordekaiser', 
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

word_list_fortnite = ['Chug Jug', 'Pump Shotgun', 'Tactical Shotgun', ]

word_list_siege = ['', '']


word_list_normal_words = ['Backpack', 'Hangman']

def get_word():
    word_list_q = input('Do you want special words from your favorite games (Y/N)')
    if word_list_q == Y:
        word_list_q2 = input('What game would you like to select: lol/fortnite/siege')
        if word_list_q2 == lol:
            word_list == word_list_lol
        elif word_list_q2 == fortnite:
            word_list == word_list_fortnite
        else:
            word_list == word_list_siege
    else:
        word_list == word_list_normal_words
    word = random.choice(word_list)
    return word.upper()

