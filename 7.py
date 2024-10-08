import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sum_counts[roll_sum] += 1

    probabilities = {k: (v / num_rolls) * 100 for k, v in sum_counts.items()}

    return probabilities, sum_counts


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs)
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Імовірність (%)')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.show()


def main():
    num_rolls = 100000

    probabilities, sum_counts = monte_carlo_simulation(num_rolls)

    print(f"Кількість кидків: {num_rolls}")
    print("Сума\tІмовірність (%)\tКількість появ")
    for sum_val in range(2, 13):
        print(f"{sum_val}\t{probabilities[sum_val]:.2f}%\t\t{sum_counts[sum_val]}")

    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
