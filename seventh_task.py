import random
import matplotlib.pyplot as plt


def roll_dice(n):
    count_sums = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        count_sums[roll_sum] += 1

    return count_sums


def calculate_probabilities(count_sums, n):
    probabilities = {sum_val: count / n for sum_val, count in count_sums.items()}
    return probabilities


def simulate_dice_rolls(n):
    counts = roll_dice(n)
    probabilities = calculate_probabilities(counts, n)

    sum_values = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sum_values, probs, color="blue")
    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірність суми двох кубиків за методом Монте-Карло")
    plt.xticks(sum_values)
    plt.show()

    return probabilities


# Симуляція 1 мільйона кидків
n = 1_000_000
simulated_probabilities = simulate_dice_rolls(n)

# Вивід результатів
for sum_val, prob in simulated_probabilities.items():
    print(f"Сума {sum_val}: Ймовірність = {prob:.2%}")
