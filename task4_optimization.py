from pulp import LpMaximize, LpProblem, LpVariable

# Create model
model = LpProblem(name="profit-maximization", sense=LpMaximize)

# Variables
x = LpVariable(name="Product_A", lowBound=0)
y = LpVariable(name="Product_B", lowBound=0)

# Objective function
model += 20 * x + 30 * y

# Constraints
model += (2 * x + y <= 100)
model += (x + 2 * y <= 80)

# Solve
model.solve()

# Output
print(f"Product A = {x.value()}")
print(f"Product B = {y.value()}")
print(f"Max Profit = {model.objective.value()}")