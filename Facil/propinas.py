menu ={"pizza": 3.00,
       "nachos": 4.50,
       "palomitas": 6.00,
       "papas": 2.50,
       "pretzel": 3.50,
       "refresco": 3.00,
       "limonada": 4.25}

cart = []
total = 0

print("------ Menu ------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------------------")

while True:
    food = input("elige un objeto: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------Your Bill----------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total}")