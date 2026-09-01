# Traffic Signal Control System

traffic = input("Enter traffic level (low/medium/high): ").lower()
emergency = input("Is an emergency vehicle detected? (yes/no): ").lower()

if emergency == "yes":
    print("Emergency vehicle detected!")
    print("Give priority: GREEN LIGHT")

elif traffic == "high":
    print("High traffic")
    print("Green light for 60 seconds")

elif traffic == "medium":
    print("Medium traffic")
    print("Green light for 40 seconds")

elif traffic == "low":
    print("Low traffic")
    print("Green light for 20 seconds")

else:
    print("Invalid traffic level")
