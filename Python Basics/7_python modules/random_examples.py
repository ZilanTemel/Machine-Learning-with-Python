import random

# Custom greetings to randomly pick from
greetings = ['Hey!', 'Hello!', 'What’s up?', 'Hi there!', 'Greetings!', 'Yo!']
# Randomly select a greeting
selected_greeting = random.choice(greetings)
print(f"Greeting: {selected_greeting}")

# List of student names for a mini game or example
students = ['Zilan', 'Arda', 'Mert', 'Elif', 'Selin', 'Burak']

# Pick 3 random students for a quiz group
group = random.sample(students, 3)
print(f"Random Group: {group}")

# Simulate a dice roll (1 to 6)
dice_roll = random.randint(1, 6)
print(f"Dice Roll: {dice_roll}")

# Generate a random even number between 100 and 200
even_number = random.choice([x for x in range(100, 201) if x % 2 == 0])
print(f"Random Even Number: {even_number}")

# Shuffle a playlist
playlist = ['Song A', 'Song B', 'Song C', 'Song D']
random.shuffle(playlist)
print(f"Shuffled Playlist: {playlist}")

# Create a secret code made of 5 random letters
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
secret_code = ''.join(random.choices(letters, k=5))
print(f"Secret Code: {secret_code}")
