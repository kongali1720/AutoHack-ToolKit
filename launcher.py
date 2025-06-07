# launcher.py
import os
import sys

TOOLS = {
    "1": ("WiFi Cracker Simulator", "wifi_cracker_simulator.py"),
    "2": ("Email Spammer Fake", "email_spammer_fake.py"),
    "3": ("DDoS Attack Simulator", "ddos_attack_simulator.py"),
    "4": ("WiFi Password Generator", "wifi_passwords_generator.py"),
    "5": ("Fake Root Access", "fake_root_access.py"),
    "0": ("Keluar dari Matrix", None)
}

def menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("🛠️  AutoHack-ToolKit vLOL 🤡")
    print("="*33)
    for key, (name, _) in TOOLS.items():
        print(f"[{key}] {name}")
    print("="*33)

def main():
    while True:
        menu()
        choice = input("🔥 Pilih tool anda: ")
        if choice not in TOOLS:
            print("❌ Pilihan tidak valid. Coba lagi, bos!")
            input("Tekan Enter untuk lanjut...")
            continue
        if choice == "0":
            print("👋 Keluar dari dunia tipu-tipu...")
            sys.exit()
        tool_name, script = TOOLS[choice]
        print(f"\n🚀 Menjalankan: {tool_name}")
        print("="*33)
        try:
            with open(script, 'r') as file:
                exec(file.read())
        except FileNotFoundError:
            print("⚠️ Script belum tersedia. Cek dulu bos.")
        input("\n⏳ Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
