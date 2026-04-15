from chatbot_base import ChatbotBase
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
import os
import warnings
warnings.filterwarnings('ignore')
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
os.environ['TOKENIZERS_PARALLELISM'] = 'False'
from transformers import AutoModelForCausalLM, AutoTokenizer

print('\n' * 100)

class MyChatbot(ChatbotBase):
    def __init__(self, name='Pre-dream'):
        super().__init__(name)
        self.dataset_path = 'songs.csv'
        self.column_names = ['SONG_NAME', 'ARTIST', 'LYRICS', 'ENVIRONMENT', 'WEATHER', 'ERA', 'MOOD_TAG']
        self.dataset_separator = ','
        self.df = self.load_songs(self.dataset_path, self.dataset_separator, self.column_names)
        self.vectorizer, self.moods_matrix = self.moods_to_tfidf(self.df)
        self.analyzer = SentimentIntensityAnalyzer()

    # function to calculate vader sentiment
    def vadersentimentanalysis(self, review):
        vs = self.analyzer.polarity_scores(review)
        return vs['compound']
        
    # function to analyse
    def vader_analysis(self, compound):
        if compound >= 0.5:
            return 'positive'
        elif compound <= -0.5 :
            return 'negative'
        else:
            return 'neutral'

    def enter(self, message):
        input(message)

    def greeting(self):
        print(
             "🐑: BAAA! Welcome to Pre-dreameh ~\n"
            "           __  _\n"
            "       .-.'  `; `-._  __  _\n"
            "      (_,         .-:'  `; `-._\n"
            "    ,'o\"(        (_,           )\n"
            "   (__,-'      ,'o\"(            )>\n" 
            "      (       (__,-'            )\n"
            "       `-'._.--._(             )\n"
            "          |||  |||`-'._.--._.-'\n"
            "                     |||  |||\n"
            "It's time to go to bed and enjoy your dream!"
        )
        time.sleep(1)
        print("\nHold on, let me craft a little pre-dream for you—a tiny story and a sweet tune to ease you into sleep!\n")
        time.sleep(1)
        user_name = input("🐑: Because it's a HIGHLY customized experience (^_~), let me have your name first: \n").strip()
        ready_response = input(f"🐑: Ok, {user_name}. Are you ready? (yes/no)\n").strip().lower()

        if ready_response not in ["yes", "no"]:
            self.enter("🐑: I'll take that as a yes! Let's get it started! zZZ...\n")
        elif ready_response == "no":
            self.enter("🐑: You know what... Dreaming is like the feeling that you suddenly want to pee and you can't control 😈 Let's move on anyway!\n")
    
    def load_songs(self, file_path, separator, column_names):
        df = pd.read_csv(file_path, sep=separator, usecols=column_names)
        return df

    def moods_to_tfidf(self, df):
        vectorizer = TfidfVectorizer(stop_words='english')
        moods_matrix = vectorizer.fit_transform(df['MOOD_TAG'])
        return vectorizer, moods_matrix

    def ask_questions(self):
        while True:
            lyrics_fav = None
            environment_fav = None
            weather_fav = None
            era_fav = None

            while lyrics_fav is None:
                print("🐑: Alright, let's start with a few deep breaths. Inhale deeply, hold for a moment, then exhale slowly. Let your mind empty and welcome the calm.\n")
                time.sleep(1)
                print("\nWhen the music plays, do you like it pure and wordless ❌, or do you enjoy the stories told through lyrics ✅?\n")
                time.sleep(1)
                lyrics_fav = input(
                    "(A) Music with lyrics\n"
                    "(B) Music without lyrics\n"
                ).strip().lower()

                if re.search(r'\b(B|b|(B)|(b)|no|pure|wordless|no lyrics|without lyrics|through)\b', lyrics_fav):
                    lyrics_fav = 'no'
                    print("🐑: Ah, you prefer music without lyrics. Good choice. Sometimes, silence speaks louder than words!\n")

                elif re.search(r'\b(A|a|(A)|(a)|yes|story|stories|with lyrics|with)\b', lyrics_fav):
                    lyrics_fav = 'yes'
                    print("🐑: Looks like you enjoy listening to stories. There's always a tale waiting to be told through lyrics!\n")

                else:
                    print("🐑: I didn't quite catch that. Could you please say if you prefer music without lyrics ❌ or with lyrics ✅ ?\n")
                    lyrics_fav = None


            while environment_fav == None:
                print("🐑: Our journey is about to begin —- will you follow the forest's quiet whispers 🌳, or the sea's endless call 🌊?\n")
                time.sleep(1)
                environment_fav = input(
                    "(A) Forest 🌳\n"
                    "(B) Sea 🌊\n"
                ).strip().lower()
                
                if re.search(r'\b(A|a|(A)|(a)|forest|quiet whispers|whispers|whisper|follow whisper|follow whispers)\b', environment_fav):
                    environment_fav = 'forest'
                    print("You step into the forest, where sunlight streams through the branches, and the gentle rustling of leaves fills the air.\n")
                    time.sleep(1)
                    print("Suddenly, the ground disappears beneath you, and you tumble down—into a place you've never been before.🤔\n")
                    time.sleep(1)
                    print("When you're completely confused, you hear a voice...\n")
                    time.sleep(1)
                    print("'Ei hey hey! Hi everybody. It's me Mickey Mouse!'\n"
                    "         .-\"\"\"-.\n"
                    "        /       \\\n"
                    "        \\       /\n"
                    "   .-\"\"\"-.-`.-.-.<  _\n"
                    "  /      _,-\\ ()()_/:)\n"
                    "  \\     / ,  `     `|\n"
                    "   '-..-| \\-.,___,  /\n"
                    "         \\ `-.__/  /\n"
                    "          `-.__.-'`\n"
                    )
                    time.sleep(1)
                elif re.search(r'\b(B|b|(B)|(b)|sea|endless|call)\b', environment_fav):
                    environment_fav = 'sea'
                    print("You wade into the sea, water cool against your ankles.\n")
                    time.sleep(1)
                    print("Suddenly, a wave pulls you under. To your amazement, you can breathe. \n")
                    time.sleep(1)
                    print("In the quiet depths, a familiar song reaches your ears:\n")
                    time.sleep(1)
                    print("Are you ready kids?\n")
                    time.sleep(1)
                    print("Aye, aye, captain!\n")
                    time.sleep(1)
                    print("I can't hear you!\n")
                    time.sleep(1)
                    print("Aye, aye, captain!\n")
                    time.sleep(1)
                    print("Ooh——\n")
                    time.sleep(1)
                    print(
                        """      .--..--..--..--..--..--.
                             .' '   |  '._)         (_)  |
                            \\ _.')\\      .----..---.   /
                            |(_.'  |    /    .-\\-.  \\  |
                            \\     0|    |   ( O| O) | o|
                              |  _  |  .--.____.'._.-.  |
                             \\ (_) | o         -` .-`  |
                               |    \\   |`-._ _ _ _ _\\ /
                               \\    |   |  `. |_||_|   |
                               | o  |    \\_      \\     |
                               |    \\     `--..-'   O  |
                               '. .' |     `-.-'        |
                                  '. |='=.='=.='.='=.='=\n"""
                    )
                    time.sleep(1)
                    print("It's Spongebob squarepants!\n")
                    time.sleep(1)
                else:
                    print("🐑: I didn't quite understand. Could you please say if you prefer the forest🌳 or the sea🌊 ?\n")
                    environment_fav = None

            while weather_fav is None:
                print("He looked like he had so much to say when you showed up out of the blue.\n")
                time.sleep(1)
                print("After what felt like ages, he finally spoke: \n")
                time.sleep(1)
                weather_fav = input("So... How's the weather? (Turns out, he's the British edition.)\n")
                time.sleep(1)
                if re.search(r'\b(good|nice|nice weather|sun|bright|sunny|like)\b', weather_fav):
                    weather_fav = 'positive'
                    print("Ah, lovely weather! You don't get this kind of sunshine often!\n")
                    time.sleep(1)

                elif re.search(r'\b(ok|windy|cloudy|not bad)\b', weather_fav):
                    weather_fav = 'neutral'
                    print("Well, at least it's not pouring. ")
                    time.sleep(1)

                elif re.search(r'\b(rain|rainy|not good|bad)\b', weather_fav):
                    weather_fav = 'negative'
                    print("Bad weather may be a bit of a downer, but I hope it hasn't put you off too much.\n")
                    time.sleep(1)

                else:
                    print("🐑: I didn't quite get it. Could you please say if it is sunny, cloudy or rainy?\n")
                    weather_fav = None

            while era_fav is None:
                era_fav = input("Looks like your destination isn't here. Do you want to go back to your world, or stay here and have some fun with me?\n")
                if re.search(r'\b(go back|back)\b', era_fav):
                    era_fav = 'old'
                    self.enter(
                        "I really want you to stay, but it looks like you've made up your mind. Goodbye, my friend!👋\n"
                        "▶▶ Press Enter to go back\n"
                    )
                    time.sleep(1)

                elif re.search(r'\b(stay|here|have fun|with you)\b', era_fav):
                    era_fav = 'new'
                    self.enter(
                        "That would be great! But, looking back-it feels like something is calling out to you...\n"
                        "▶▶ Press Enter to look back\n"
                    )
                    time.sleep(1)

                else:
                    era_fav = 'old'
                    self.enter(
                        "I really want you to stay. But, looking back-it feels like something is calling out to you...\n"
                        "▶▶ Press Enter to look back\n"
                    )
                    time.sleep(1)

            return lyrics_fav, environment_fav, weather_fav, era_fav

    def filter_songs(self, lyrics_fav, environment_fav, weather_fav, era_fav):
        filtered_songs = self.df[
            (self.df['LYRICS'].str.lower() == lyrics_fav) &
            (self.df['ENVIRONMENT'].str.lower() == environment_fav) &
            (self.df['WEATHER'].str.lower() == weather_fav) &
            (self.df['ERA'].str.lower() == era_fav)
        ]
        return filtered_songs if not filtered_songs.empty else self.df


    def recommend_song(self, user_query, filtered_songs):
        input_vec = self.vectorizer.transform([user_query])
        similarities = cosine_similarity(input_vec, self.moods_matrix).flatten()
        if not filtered_songs.empty:
            # similarities_filtered = similarities[filtered_songs.index]
            recommend_index = similarities[filtered_songs.index].argmax()
            return filtered_songs.iloc[recommend_index]
        else:
            recommend_index = similarities.argmax()
            return self.df.iloc[recommend_index]

    def process_input(self, user_input):
        return user_input.strip().lower()
    
    def generate(self):
        lyrics_fav, environment_fav, weather_fav, era_fav = self.ask_questions()
        filtered_songs = self.filter_songs(lyrics_fav, environment_fav, weather_fav, era_fav)
        print("You found yourself come back to where you from.\n")
        time.sleep(1)
        print("🐑: Ah, there you are! Finally found you! Where have you been? Don't tell me... you just had a pre-pre-dream, didn't you? 😉\n")
        time.sleep(1)
        print("Dreams are like memories in motion. Sometimes they bring back things we've experienced or feelings we've had, and other times, they surprise us with something new.\n")
        time.sleep(1)

        user_query = input("Think of a place, a feeling, or even a wild idea. I'll weave it into a dream with a song for you. 🌌\n").strip().lower()
        time.sleep(1)

        print("🐑: I think I've got a pretty good idea of what kind of pre-dream and sleep music you need!\n")
        time.sleep(1)
        print("While I'm searching for it, could you do me a favor and count some sheep for me? Just to, you know, set the mood!\n")
        time.sleep(1)
        print(
        """
                        _-(_)-  _-(_)-  _-(_)-  _-(_)-  
                         `(___)  `(___)  `(___)  `(___)  
            Inhale for    // \\\\   // \\\\   // \\\\   // \\\\  

                        _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  
                         `(___)  `(___)  `(___)  `(___)  `(___)  `(___)  `(___)  
            Hold for      // \\\\   // \\\\   // \\\\   // \\\\   // \\\\   // \\\\   // \\\\  

                        _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  _-(_)-  
                         `(___)  `(___)  `(___)  `(___)  `(___)  `(___)  `(___)  `(___) 
            Exhale for    // \\\\   // \\\\   // \\\\   // \\\\   // \\\\   // \\\\   // \\\\   // \\\\    ...\n
            """
        )
        time.sleep(1)
        hypnosis = input("* REMEMBER * Try to breathe when you are counting, and give me numbers of every each line. (eg. 123)\n")
        if hypnosis == '478':
            print("\n🐑: Bingo! Looks like you're still wide awake! Let this song help you drift off to sleep.")
        else:
            print("\n🐑: Looks like you're already getting sleepy. Let this song tuck you in.")

        self.processed_input = self.process_input(user_query)
        
        recommended = self.recommend_song(user_query, filtered_songs)

        if recommended is not None:
            sentiment_score = self.vadersentimentanalysis(recommended['MOOD_TAG'])
            self.sentiment = self.vader_analysis(sentiment_score)
            self.recommended_song = self.recommend_song(user_query, filtered_songs)
            checkpoint = "HuggingFaceTB/SmolLM-135M"

            device = "cpu" 
            tokenizer = AutoTokenizer.from_pretrained(checkpoint)

            input_str = (
                f"You find yourself immersed in a dream inspired by '{user_query}'. "
                "Your dream start to take shape based on this idea: \n"
            )

            model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
    
            inputs = tokenizer.encode(input_str, return_tensors="pt").to(device)
            outputs = model.generate(
                inputs,
                max_new_tokens=100,
                temperature=0.3,
                top_p=0.95,
                min_p=0.1,
                do_sample=True,
                repetition_penalty=1.5
            )
            story = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"\n🎧 - {recommended['SONG_NAME']} by {recommended['ARTIST']} (Tags: {recommended['MOOD_TAG']})")
            print(f"\n🌀 - {story}")
        else:
            print("🐑: Hmm, I couldn't find the perfect song. Tell me more about what do you want to explore tonight!")

if __name__ == "__main__":
    chatbot = MyChatbot()
    chatbot.greeting()
    chatbot.generate()
    
