from time import sleep
import ctypes


def title(codee):
    ctypes.windll.kernel32.SetConsoleTitleW(
        f"RTX4090 | {codee}/{len(list)} |")

try:
    with open("combolist.txt","r", errors='ignore', encoding='utf-8') as f:
        list = f.readlines()
        code = 0
        if len(list) > 0:

            savefile = open("userpass.txt", "a", errors='ignore', encoding='utf-8')

            for combo in list:

                try:
                    user = combo.split("\n")[0].split("@")[0].strip()
                    password = combo.split("\n")[0].split(":")[1].strip()
                    savefile.write("{}:{}\n".format(user, password))
                    code += 1
                    title(code)
                except Exception:
                    pass

        else:
            print("\n [!] Empty File...")
            sleep(1)
            exit()

except Exception:
    print("\n [!] Can not find the file...")
    sleep(1)
    exit()
