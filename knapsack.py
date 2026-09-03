def knapsack(weights, values, capacity):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If current item's weight is less than
            # or equal to current capacity
            if weights[i - 1] <= w:

                # Maximum of:
                # 1. Excluding the item
                # 2. Including the item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weights:")
for i in range(n):
    weights.append(int(input()))

print("Enter values:")
for i in range(n):
    values.append(int(input()))

capacity = int(input("Enter knapsack capacity: "))

# Calculate maximum value
result = knapsack(weights, values, capacity)

print("Maximum value =", result)