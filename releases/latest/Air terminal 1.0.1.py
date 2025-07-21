import os
import time
import sys
import random
import shutil
import requests
from colorama import init, Fore, Style
init(autoreset=True)
CURRENT_VERSION = "1.0.1"
UPDATE_JSON_URL = "https://raw.githubusercontent.com/mcsstudio/main/main/update_info.json"

def check_update():
    try:
        response = requests.get(UPDATE_JSON_URL, timeout=3)
        if response.status_code == 200:
            data = response.json()
            latest = data['latest_version']
            if latest != CURRENT_VERSION:
                print(f"\n\033[93m[New update] Version {latest} is avaible")
                print(f"Change: \n{data['changelog']}")
                print(f"Download at: {data['download_url']}\033[0m\n")
        else:
            print("Can't check for updates. Server returned status code:", response.status_code)
    except Exception as e:
        print(f"Error in update: {e}")



pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
print("Your link code:", pin)


# ========== ANSI COLOR ==========
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# ========== HACKER EFFECT ==========
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ========== TIỆN ÍCH ==========
def loading_bar(percent, total=30):
    filled = int(percent * total)
    empty = total - filled
    bar = '=' * filled + '-' * empty
    print(f"Status: [{bar}] {int(percent * 100)}%", end='\r')

# ========== FAKE HACK ==========
def fake_hack():
    print(f"{MAGENTA}Initializing Hackmode v1.0...{RESET}")
    time.sleep(1)
    steps = [
        "Establishing secure tunnel to mcs.hub.net...",
        "Encrypting connection using RSA-4096...",
        "Injecting bypass payload...",
        "Firewall breached.",
        "Locating entrypoint in system.core...",
        "Access granted. Control level: ROOT",
        "Injecting terminal virus...",
        "Planting backdoor in /brain/sys32...",
        "Spawning AI worm.exe...",
        "Transferring 2048-bit mind control signal...",
        "Hack complete. System compromised."
    ]
    for step in steps:
        print(f"{GREEN}{step}{RESET}")
        time.sleep(0.6)

    print(f"\n{RED}>>> MCS Studio System: You now control the terminal \U0001f608{RESET}")
    input("\nPress Enter to continue...")
    clear()
    terminal()

#Locking the terminal
def lock_terminal():
    print(f"{Fore.YELLOW}Terminal is locked. Enter PIN to unlock.{Style.RESET_ALL}")
    while True:
        command = input(">>> ").lower()
        if command == "1234":
            print(f"{GREEN}Terminal unlocked.{RESET}")
            break
        else:
            print(f"{RED}Invalid command. Terminal remains locked.{RESET}")

# ========== TERMINAL ==========
def terminal():
    clear()
    print(f"{CYAN}Terminal 1.3 - MCS Studio | Type '--help' for commands{RESET}")
    a = input(">>> ").lower()

    if a == "download --service":
        print(f"{GREEN}Downloading...{RESET}")
        time.sleep(0.3)
        print("Detected MCS Studio services")
        time.sleep(0.3)
        print("MCS Studio Copyright 2025.")
        time.sleep(0.5)
        print("Waiting from server...")
        time.sleep(0.75)
        print("Collecting data...")
        time.sleep(0.25)
        print("File detected")
        time.sleep(0.5)
        print("Downloading...")

        for i in range(31):
            percent = i / 30
            loading_bar(percent)
            if i == 29:
                time.sleep(10)
            else:
                time.sleep(0.1)
        print()
        print(f"{GREEN}Download completed successfully.{RESET}")
        time.sleep(0.5)
        again = input("Do you want to download again? [Y/N]: ").lower()
        if again == 'y':
            terminal()
        else:
            print("Exiting... See you soon!")
            time.sleep(0.5)
            sys.exit()

    elif a == "--exit":
        print(f"{YELLOW}Exiting terminal...{RESET}")
        time.sleep(0.5)
        sys.exit()

    elif a == "--debug":
        print(f"{MAGENTA}DEBUG MODE INITIATED...{RESET}")
        time.sleep(0.3)
        print("Running system check...")
        time.sleep(0.5)
        print("Analyzing memory...")
        time.sleep(0.5)
        print("Memory status: OK")
        print("Terminal log saved to debug.log")
        time.sleep(1)
        input("Press Enter to continue...")
        terminal()

    elif a == "--help":
        print(f"{YELLOW}Available Commands:{RESET}")
        print(f"  {GREEN}download --service{RESET}         : Download service")
        print(f"  {CYAN}--exit{RESET}                   : Exit the terminal")
        print(f"  {RED}--debug{RESET}                  : Enter debug mode")
        print(f"  {RED}--destroy{RESET}     : \u2620 system wipe")
        print(f"  {RED}--hackmode.net | mcs{RESET}       : \U0001f47e Initiate hack mode")
        print(f"  {RED}--duplicate{RESET}              : Duplicate terminal")
        print(f"  {RED}--?????????{RESET}              : \U0001f4a9 ????????? terminal")
        print(f"  {CYAN}--changepass{RESET}              : PIN change")
        input("\nPress Enter to return...")
        terminal()

    elif a == "--destroy":
        print(f"{RED}WARNING: Irreversible neural destruction initiated...{RESET}")
        time.sleep(0.5)
        print("Shutting down visual cortex...")
        time.sleep(1)
        print("Overloading hippocampus...")
        time.sleep(1.5)
        print(f"{RED}BOOM \U0001f4a5 Brain.exe has stopped responding.{RESET}")
        time.sleep(1)
        input("Press Enter to reboot consciousness...")
        terminal()

    elif a == "--hackmode.net | mcs":
        fake_hack()

    elif a == "--bsod":
        clear()
        print("\033[1;37;44m")
        print("A problem has been detected and Windows has been shut down to prevent damage")
        print("to your computer.\n")
        print("The problem seems to be caused by the following file: MCS_TERMINAL.SYS\n")
        print("PAGE_FAULT_IN_NONPAGED_AREA\n")
        print("If this is the first time you've seen this Stop error screen,")
        print("restart your computer. If this screen appears again, follow")
        print("these steps:\n")
        print("- Check to make sure any new hardware or software is properly installed.")
        print("- If this is a new installation, ask your hardware or software manufacturer")
        print("  for any Windows updates you might need.\n")
        print("Technical Information:")
        print("*** STOP: 0x00000050 (0xFFFFF880009AA000, 0x0000000000000000,")
        print("              0xFFFFF80002ED53F7, 0x0000000000000000)\n")
        print("Collecting data for crash dump ...")
        print("Initializing disk for crash dump ...")
        print("Beginning dump of physical memory.\n")
        print("Dumping physical memory to disk: 100")
        print("\nPress Enter to simulate reboot...", end='')
        input()
        terminal()
    elif a == "--duplicate":
        os.system("Airlauncher.py")
        exit
        lock_terminal()

    elif a == "--easteregg":
        print(f"{YELLOW}Easter Egg Terminal Activated!{RESET}")
        time.sleep(0.5)
        print("Welcome to the Easter Egg terminal!")
        print("This terminal is full of surprises and fun commands.")
        print("Type 'surprise' to see a random surprise!")
        while True:
            surprise = input(">>> ").lower()
            if surprise == "surprise":
                surprises = [
                    "🎉 Surprise! You found a hidden message!",
                    "🐱 Here's a cute cat picture: [cat image]",
                    "🎈 You win a balloon! 🎈",
                    "💻 Hacking into the mainframe... Just kidding, it's all fake!"
                ]
                print(random.choice(surprises))
            else:
                print(f"{RED}Unknown command in Easter Egg terminal.{RESET}")

    elif a == "--dev_tool: wipedata":
        print("Dev Tool: Wiping data...")
        time.sleep(0.5)
        print("Are you sure you want to wipe all data? This action cannot be undone.")
        confirm = input("Type 'yes' to confirm: ").lower()
        if confirm == 'yes':
            print("Wiping data...")
            time.sleep(1)
            print("Data wiped successfully. Terminal is now empty.")
            time.sleep(1)
            print("Exiting terminal...")
            sys.exit()
        else:
            print("Data wipe cancelled.")
            time.sleep(1)
            terminal()

    elif a == "--dev_tool: r/ d/ f/ all":
        print("Are you sure to use this command? That a hard command. (R/ = Reset, D/ = Delete, F/ = Format, All = all partitions of terminal), delete all temporary data and disable all lisenses keys. (Y/N)")
        confirm = input(">>> ").lower()
        if confirm == 'y':
            print("Resetting terminal...")
            time.sleep(1)
            print("Deleting temporary files...")
            time.sleep(1)
            print("Formatting all partitions...")
            time.sleep(1)
            print("Disabling all license keys...")
            print("Reset key to trial key.")
            time.sleep(1)

            # 💥 Reset pass về mặc định
            try:
                with open("pass.txt", "w") as f:
                    f.write("0000")
                print("Mã PIN đã được reset về mặc định: 0000")
            except Exception as e:
                print(f"{RED}Lỗi khi reset mã PIN: {e}{RESET}")

            print("All data has been reset. Terminal is now clean.")
            time.sleep(1)
            print("Exiting terminal...")
            sys.exit()
        else:
            print("Operation cancelled. Returning to terminal.")
            time.sleep(1)
            terminal()

    elif a == "--check_version":
        print(f"Version {CURRENT_VERSION} is currently installed.")

    elif a == "--lock":
        lock_terminal()

    elif a == "--changepass":
        try:
            with open("pass.txt", "r") as f:
                current_pass = f.read().strip()
        except FileNotFoundError:
            print(f"{RED}Không tìm thấy file 'pass.txt'. Đang tạo mã PIN mới...{RESET}")
            current_pass = ""

        entered_old = input("Nhập mật khẩu hiện tại: ").strip()
        if entered_old != current_pass:
            print(f"{RED}Sai mật khẩu hiện tại. Không thể đổi.{RESET}")
            time.sleep(1)
            terminal()

        new_pass = input("Nhập mật khẩu mới (4 chữ số): ").strip()
        if len(new_pass) != 4 or not new_pass.isdigit():
            print(f"{RED}Mã PIN không hợp lệ. Phải là 4 chữ số.{RESET}")
            time.sleep(1)
            terminal()

        with open("pass.txt", "w") as f:
            f.write(new_pass)

        print(f"{GREEN}Mật khẩu đã được cập nhật!{RESET}")
        time.sleep(1)
        terminal()
    else:
        print(f"{RED}Unknown command: '{a}' — try '--help'{RESET}")
        time.sleep(1)
        terminal()



if __name__ == '__main__':
    check_update()
    lock_terminal()
    terminal()