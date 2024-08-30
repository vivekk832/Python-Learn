password = "Pass@1234"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strenght = "Medium"
else:
    strenght = "Strong"

print("Password Strength is : ", strenght)