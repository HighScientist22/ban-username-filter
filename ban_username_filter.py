import re

# Words to match for racism, slurs, hate speech, etc.
BANNED_RACIST_TERMS = [
    r"\bnigger\b", r"\bchink\b", r"\bkike\b", r"\bwetback\b", r"\bspic\b",
    r"\bporchmonkey\b", r"\bsandnigger\b", r"\bniglet\b", r"\bn1gger\b"
]

RANDOM_MIN_LENGTH = 8
RANDOM_NUM_RATIO = 0.6

def is_racist(username):
    for pattern in BANNED_RACIST_TERMS:
        if re.search(pattern, username, re.IGNORECASE):
            return True
    return False

def is_random(username):
    if len(username) < RANDOM_MIN_LENGTH:
        return False
    num_digits = sum(char.isdigit() for char in username)
    return (num_digits / len(username)) >= RANDOM_NUM_RATIO

def should_ban(username):
    return is_racist(username) or is_random(username)

def get_chill_message(username):
    return (
        f"🌿 Hey, just a heads-up: the username '{username}' looks a bit sus.\n"
        "If it's random or contains banned words, you might get autobanned.\n"
        "Feel free to chill and change it — the system will unban you automatically ✌️"
    )

# Example usage for testing
if __name__ == "__main__":
    test_names = ["n1gger420", "user9472", "peacefulstoner", "4fd83k93"]
    for name in test_names:
        if should_ban(name):
            print(f"[BAN] {name}")
            print(get_chill_message(name))
