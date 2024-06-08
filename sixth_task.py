def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if budget >= details["cost"]:
            budget -= details["cost"]
            total_calories += details["calories"]
            chosen_items.append(item)
            if budget == 0:
                break

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    costs = [item["cost"] for item in items.values()]
    calories = [item["calories"] for item in items.values()]
    n = len(costs)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(list(items.keys())[i - 1])
            w -= costs[i - 1]

    chosen_items.reverse()
    return chosen_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

# Використання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

# Використання алгоритму динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)
print("Алгоритм динамічного програмування:")
print("Обрані страви:", dp_result)
print("Сумарна калорійність:", dp_calories)
