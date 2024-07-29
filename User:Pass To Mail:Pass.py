from time import sleep
from os import system


class Settings:
    name = input("\n [?] Combolist Name (Must be in the same folder) : ")
    if len(name) == 0:
        print("\n [!] Wrong Input the Combolist Name")
        sleep(1)
        exit()
    mrx = input(
        "\n [?] Mail Types --> [@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, "
        "@outlook.com.tr, @icloud.com, @edu.com] : ")
    if len(mrx) == 0:
        print("\n [!] Wrong Input the Mail Type")
        sleep(1)
        exit()
    izinli_karakterler = (
        '@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, @outlook.com.tr, @icloud.com, @edu.com ')


class Permissions:
    for mails in Settings.izinli_karakterler:
        if mails in Settings.mrx:
            print("\n [+] Success, Loading...")
            sleep(2)
            system("cls")
            break
        else:
            break


class MainProgress:
    try:
        with open(Settings.name, errors="ignore", encoding="utf-8") as file:

            if len(file.readlines()) > 0:

                savefile = open(f"{Settings.mrx}--pass.txt", "a")

                for combo in file.readlines():

                    try:
                        user = combo.split("\n")[0].split(":")[0].strip() + Settings.mrx
                        password = combo.split("\n")[0].split(":")[1].strip()
                        savefile.write("{}:{}\n".format(user, password))
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
