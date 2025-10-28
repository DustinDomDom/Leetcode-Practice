import random
import string

# Emoji Unicode ranges
emoji_ranges = [
    (0x1F600, 0x1F64F),  # Smileys & Emotion
    (0x1F300, 0x1F5FF),  # Symbols & Pictographs
    (0x1F680, 0x1F6FF),  # Transport & Map
    (0x1F900, 0x1F9FF),  # Supplemental Symbols
]

def random_emoji():
    """Generate a random emoji from the defined ranges."""
    start, end = random.choice(emoji_ranges)
    code_point = random.randint(start, end)
    try:
        return chr(code_point)
    except:
        return random_emoji() 

emoji_dict = {letter: random_emoji() for letter in string.ascii_uppercase}

# Display results
for k, v in emoji_dict.items():
    print(f"{k}: {v} | {hex(ord(v))} | {int(hex(ord(v)), 16)}")
