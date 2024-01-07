import random
import time
import threading
# generae a word, no rep
def generate_random_word(used_words):
    word_list = [
        "apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "house", "igloo", "jacket",
        "kangaroo", "lemon", "mango", "nutmeg", "orange", "penguin", "quilt", "rabbit", "strawberry", "tiger",
        "umbrella", "violin", "watermelon", "xylophone", "yacht", "zebra", "ocean", "sunflower", "butterfly",
        "dragonfly", "firework", "lighthouse", "happiness", "moonlight", "rainbow", "starfish", "waterfall",
        "whisper", "chocolate", "carousel", "paradise", "adventure", "treasure", "fireplace", "mountain",
        "whistle", "giraffe", "elephant", "octopus", "butterfly", "peacock", "scorpion", "pineapple", "caterpillar",
        "blossom", "sparrow", "dolphin", "waterfall", "sunset", "thunder", "lightning", "volcano", "harmony",
        "serenity", "chameleon", "delicate", "marathon", "sunrise", "scissors", "gazelle"
    ]

    available_words = [word for word in word_list if word not in used_words]

    if not available_words:
        used_words.clear()
        available_words = word_list

    selected_word = random.choice(available_words)
    used_words.add(selected_word)
    return selected_word

def preload_next_word(queue, used_words):
    while True:
        time.sleep(1)
        next_word = generate_random_word(used_words)
        queue.put(next_word)

def countdown():
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
    print("Start typing!\n")

def typing_game():
    print("Welcome to the Simple Typing Game!")
    print("You have 30 seconds to type words (max 8 letters).")
    print("Press Enter to start...")
    input()

    start_time = time.time()
    end_time = start_time + 30

    score = 0
    total_words_typed = 0
    used_words = set()

    word_queue = queue.Queue()
    word_thread = threading.Thread(target=preload_next_word, args=(word_queue, used_words))
    word_thread.daemon = True
    word_thread.start()

    countdown()

    while time.time() < end_time:
        target_word = word_queue.get()
        print("Type this word:", target_word)
        user_input = input("Your input: ")

        if user_input.lower() == target_word.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        total_words_typed += 1

    elapsed_time = time.time() - start_time
    wpm = int((score / elapsed_time) * 60)

    print(f"Time's up! Your score is: {score} words typed.")
    print(f"Your words per minute (WPM): {wpm}")

if __name__ == "__main__":
    import queue
    typing_game()
