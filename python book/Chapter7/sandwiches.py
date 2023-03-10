sandwich_orders = ['tuna', 'steak', 'vegie', 'chicken']
prepared_sandwiches = []
for sandwich in sandwich_orders:
    print(f"This {sandwich.title()} is not ready, hold on for five minutes")
print("----------------------------")
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    prepared_sandwiches.append(current_sandwiches)
for ready_sandwich in prepared_sandwiches:
    print(f"\nThis sandwich {ready_sandwich.title()} is ready.")