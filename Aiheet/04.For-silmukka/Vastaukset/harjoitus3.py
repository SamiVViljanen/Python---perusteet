# Harjoitus 3: Listan läpikäynti - RATKAISU

# 1. Luo lista
hedelmät = ["omena", "banaani", "appelsiini", "päärynä"]

# 2-3. Käy lista läpi ja tulosta numeroidusti
for index, hedelmä in enumerate(hedelmät):
    print(f"{index + 1}. {hedelmä}")
