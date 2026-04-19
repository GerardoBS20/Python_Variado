import random

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌──────────┐"
"│          │"
"│          │"
"│          │"
"└──────────┘"

dice_art = {
    1: ["┌──────────┐"
        "│          │"
        "│     ●    │"
        "│          │"
        "└──────────┘"],
    2: ["┌──────────┐"
        "│  ●       │"
        "│          │"
        "│      ●   │"
        "└──────────┘"],
    3: ["┌──────────┐"
        "│  ●       │"
        "│    ●     │"
        "│      ●   │"
        "└──────────┘"],
    4: ["┌──────────┐"
        "│  ●   ●   │"
        "│          │"
        "│  ●   ●   │"
        "└──────────┘"],
    5: ["┌──────────┐"
        "│  ●   ●   │"
        "│    ●     │"
        "│  ●   ●   │"
        "└──────────┘"],
    6: ["┌──────────┐"
        "│  ●   ●   │"
        "│  ●   ●   │"
        "│  ●   ●   │"
        "└──────────┘"]
}


# Pide el número de dados
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

# Lanza los dados
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))



# Imprime los dados horizontalmente
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

# Calcula el total
for die in dice:
    total += die
print(f"Total: {total}")