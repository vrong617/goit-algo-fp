def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        while total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [0] * (budget + 1)

    for i in range(n):
        item, info = item_list[i]
        cost = info['cost']
        calories = info['calories']
        for w in range(cost, budget + 1):
            dp[w] = max(dp[w], dp[w - cost] + calories)

    total_calories = dp[budget]
    selected_items = []
    w = budget

    while w > 0:
        for i in range(n):
            item, info = item_list[i]
            cost = info['cost']
            calories = info['calories']
            if w >= cost and dp[w] == dp[w - cost] + calories:
                selected_items.append(item)
                w -= cost
                break

    selected_items.reverse()
    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Greedy Algorithm:")
selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Selected items: {selected_items}, Total calories: {total_calories}")

print("Dynamic Programming:")
selected_items, total_calories = dynamic_programming(items, budget)
print(f"Selected items: {selected_items}, Total calories: {total_calories}")
