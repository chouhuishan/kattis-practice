number_available_flights = int(input())
potential_flights = []

for _ in range(number_available_flights):
    price = int(input())
    potential_flights.append(price)

# most_expensive = max(potential_flights)
# cheapest = min(potential_flights)

amount_reimbursed = max(potential_flights) / 2

if amount_reimbursed > min(potential_flights):
    print(0)
elif amount_reimbursed < min(potential_flights):
    minimum_amount = min(potential_flights) - amount_reimbursed
    print(int(minimum_amount))
