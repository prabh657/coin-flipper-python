import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def multiple_flips(n):
    heads = 0
    tails = 0
    for _ in range(n):
        if flip_coin() == "Heads":
            heads += 1
        else:
            tails += 1
    return heads, tails

if __name__ == "__main__":
    try:
        flips = int(input("Enter number of coin flips: "))
        h, t = multiple_flips(flips)
        print(f"\nAfter {flips} flips:")
        print(f"Heads: {h}")
        print(f"Tails: {t}")
    except ValueError:
        print("Please enter a valid number.")
