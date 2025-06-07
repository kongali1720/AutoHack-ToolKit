# email_spammer_fake.py
victim = input("Enter victim email: ")
message = input("Enter message: ")
print(f"📨 Simulating spam to {victim}")
for i in range(5):
    print(f"🧨 Spam #{i+1}: '{message}' sent (fake)")
print("🚫 Email server rejected your nonsense 😂")
