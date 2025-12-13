# Harjoitus 4: Lämpötilan luokittelu - RATKAISU

# 1. Kysy käyttäjältä lämpötila
lampotila = float(input("Anna lämpötila (°C): "))

# 2-3. Luokittele lämpötila ja tulosta neuvo
if lampotila > 25:
    print("Helteinen - Muista juoda vettä!")
elif lampotila >= 15:
    print("Lämmin - Hyvä sää kävelylle!")
elif lampotila >= 5:
    print("Viileä - Ota takki mukaan")
elif lampotila >= -5:
    print("Kylmä - Pukeudu lämpimästi")
else:
    print("Hyytävä - Ulkoilu ei suositeltavaa!")
