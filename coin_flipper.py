import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

if __name__ == "__main__":
    result = flip_coin()
    print("Coin Result:", result)
