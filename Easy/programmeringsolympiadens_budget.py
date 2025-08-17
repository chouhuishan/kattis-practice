n = int(input())
budget_proposal = {}

for _ in range(n):
    budget_item = input()
    budget_price = int(input())
    budget_proposal[budget_item] = budget_price


total_revenue_spending = sum(list(budget_proposal.values()))
total_revenue_spending = sum(budget_proposal.values())


if total_revenue_spending > 0:
    print("Usch, vinst")
elif total_revenue_spending < 0:
    print("Nekad")
elif total_revenue_spending == 0:
    print("Lagom")
else:
    print("None")
