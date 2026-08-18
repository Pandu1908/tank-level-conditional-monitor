level = int(input("Enter tank level (0-100): "))

if level >= 90:
    print("🔴 Tank is FULL")
    print("⚠️ Turn OFF the water pump.")
elif level <= 20:
    print("🟡 Water level is LOW")
    print("💧 Turn ON the pump.")
else:
    print("🟢 Water level is NORMAL")
