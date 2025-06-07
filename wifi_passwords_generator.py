# wifi_passwords_generator.py
import random
import string

print("🔐 WiFi Password Generator 3000 🔐")
chars = string.ascii_letters + string.digits + "!@#$%"
for i in range(5):
    pwd = ''.join(random.choice(chars) for _ in range(12))
    print(f"Generated password #{i+1}: {pwd}")
