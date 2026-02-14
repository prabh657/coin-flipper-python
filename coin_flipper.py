import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def multiple_flips(n):
    heads = 0
    tails = 0

    for _ in range(n):
        result = flip_coin()
        if result == "Heads":
            heads += 1
        else:
            tails += 1

    return heads, tails

def calculate_probability(count, total):
    return (count / total) * 100

if __name__ == "__main__":
    try:
        flips = int(input("Enter number of coin flips: "))

        if flips <= 0:
            print("Please enter a number greater than 0.")
        else:
            heads, tails = multiple_flips(flips)

            heads_prob = calculate_probability(heads, flips)
            tails_prob = calculate_probability(tails, flips)

            print("\n--- Results ---")
            print(f"Total flips: {flips}")
            print(f"Heads: {heads} ({heads_prob:.2f}%)")
            print(f"Tails: {tails} ({tails_prob:.2f}%)")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
