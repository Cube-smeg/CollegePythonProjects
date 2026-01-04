import random

# Intro and asking for gamemode
print("There are two game modes, 1: Guess the genre based on the song or 2: Guess the song based on the genre (multiple choice)")
GameMode = int(input("Would you like to play game version 1 or 2?"))
Score = 0 

# Using error handling making sure the rounds fit between 10 and 20
try:
    Rounds = int(input("How many rounds would you like to play? (Minimum of 10)"))
    if Rounds < 10 or Rounds > 20:
        raise ValueError("You must have 10 rounds at minimum with a cap of 20.")
    print("Your Input: " + str(Rounds))
except ValueError as e:
    print("Error: " + str(e))

# Creating a dictionary for the songs, artists, and genres
Songs_Genres = {
    "Rap": [
        {"God's Plan": "Drake"},
        {"Family Ties": "Kendrick Lamar"},
        {"Location": "Playboi Carti"},
        {"Life Goes On": "Lil Baby"},
        {"Ski": "Young Thug"},
        {"New Drank": "Lucki"}
    ],
    "Pop": [
        {"California Gurls": "Katy Perry"},
        {"One of Your Girls": "Troye Sivan"},
        {"Firework": "Katy Perry"},
        {"Blinding Lights": "The Weeknd"},
        {"Save Your Tears": "The Weeknd"}
    ],
    "Rock": [
        {"Everlong": "Foo Fighters"},
        {"Smells Like Teen Spirit": "Nirvana"},
        {"Bohemian Rhapsody": "Queen"},
        {"Seven Nation Army": "The White Stripes"},
        {"Change (In the House of Flies)": "Deftones"}
    ]
}

def CreateQuestion():
    global Score  

    # --- Select the correct genre, song, and artist ---
    CorrectGenre = random.choice(list(Songs_Genres.keys()))
    CorrectSongDict = random.choice(Songs_Genres[CorrectGenre])
    CorrectSong = list(CorrectSongDict.keys())[0]
    CorrectArtist = CorrectSongDict[CorrectSong]

    # --- Build the correct pair ---
    CorrectPairText = CorrectArtist + ": " + CorrectSong

    # --- Build incorrect pairs (mismatched artist/song) ---
    IncorrectPairs = []
    for i in range(3):
        # pick a random genre, song and artist from different entries
        wrong_genre = random.choice(list(Songs_Genres.keys()))
        wrong_song_dict = random.choice(Songs_Genres[wrong_genre])
        wrong_song = list(wrong_song_dict.keys())[0]
        wrong_artist = wrong_song_dict[wrong_song]

        # to make it wrong, mismatch artist and song
        random_genre2 = random.choice(list(Songs_Genres.keys()))
        wrong_artist2_dict = random.choice(Songs_Genres[random_genre2])
        wrong_artist2 = list(wrong_artist2_dict.values())[0]

        IncorrectPairs.append(wrong_artist2 + ": " + wrong_song)

    # --- Combine all pairs and shuffle ---
    QuestionList = IncorrectPairs + [CorrectPairText]
    random.shuffle(QuestionList)

    # --- Display the question ---
    print("\n------------- Question -----------")
    print("Which is the correct pair?")
    for i, option in enumerate(QuestionList, 1):
        print(str(i) + ". " + option)

    # --- Get the user's answer ---
    UserPick = int(input("\nWhich do you think is the correct answer (1-4)? "))

    # --- Check the answer ---
    if QuestionList[UserPick - 1] == CorrectPairText:
        Score += 1
        print("Correct! Your current score: " + str(Score))
    else:
        print("Incorrect! The correct answer was: " + CorrectPairText)



# Start the game for GameMode 2
if GameMode == 2:
    print("This one is multiple choice, find the correct pair of the 3!")
    for x in range(Rounds):
        CreateQuestion()
    
    print("Good job! You scored: " + str(Score))

elif GameMode == 1:
    print("This game is guess the genre based on the song, Good luck!")
    
else:
    print("You selected an invalid game mode.")
