# This is a program of PC builder where the user can select the components for their custom PC.
# Owner: May Thu Htun(T0333024)

import time
import os
import math


# creating a file to store finalized PC
def createFile():
    try:
        if (os.path.isfile("PC.txt")):
            print("Let's GO!")
        else:
            print("Let's G0!")
            file = open("PC.txt", "x")
            file.close()
    except:
        print("File cannot be written in your device.")


# options of CPU
def cpu():
    print("\n" + "Options for CPU:")
    # code modified from https://youtu.be/wa1XcMSBWdA (Bro Code, 2020)
    # date accessed 5 November 2022
    cpu = {"Intel core i9 12900K": "609.00",
           "AMD Ryzen 9 5900X": "509.99"}
    for keys in cpu:
        print(keys, "")
        # code modified from https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/ (dhimanthakuria97, 2022)
        # date accessed 27 October 2022
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        cpuClick = input(
            "Enter the name of the processor that you want to know the details from the list mentioned above: ")
        while cpuClick not in cpu:
            print("Your choice must be from the list mentioned above!!")
            cpuClick = input(
                "Enter the name of the processor that you want to know the details from the list mentioned above: ")

        if cpuClick == "Intel core i9 12900K":
            # code modified from https://www.w3schools.com/python/gloss_python_multi_line_strings.asp (w3schools, n.d.)
            # date accessed 29 October 2022
            print("""
Brand               Intel
Manufacturer        Intel
CPU speed           3.2 GHz
CPU socket          LGA 1700
Item model number   BX8071512900K
Dimensions          13.5 x 14 x 16.5cm; 430g
Price               £609.00
            """)

        elif cpuClick == "AMD Ryzen 9 5900X":
            print("""
Brand               AMD
Manufacturer        AMD
CPU speed           3.7 GHz
CPU socket          AM4
Item model number   AMD Ryzen 9 5900X
Dimensions          4 x 4 x 0.6cm; 79.38g
Price               £509.99
            """)

        # asking if they want to see the details of another model until they want to continue
        again = input("Do you want to look at other processor? Press 'y' to look at other processor details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            cpuChoice = input("Choose your preference processor from the list mentioned above: ")
            while cpuChoice not in cpu:
                print("Your choice must be from the list mentioned above!!")
                cpuChoice = input("Choose your preference processor from the list mentioned above: ")
            else:
                PC[0] = cpuChoice  # for easier replacement list is used
                cpuPrice = float(cpu[cpuChoice])
                cost[0] = cpuPrice  # for easier replacement list is used


# options of GPU
def gpu():
    print("\n" + "Options for GPU: ")
    gpu = {"NVIDIA GeForce RTX 3090": "1245.00",
           "AMD Radeon RX 6900XT": "999.00"}
    for keys in gpu:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        gpuClick = input("Enter the name of the GPU that you want to know the details from the list mentioned above: ")
        while gpuClick not in gpu:
            print("Your choice must be from the list mentioned above!!")
            gpuClick = input(
                "Enter the name of the GPU that you want to know the details from the list mentioned above: ")

        if gpuClick == "NVIDIA GeForce RTX 3090":
            print("""
Brand                    NVIDIA
Manufacturer             NVIDIA
Graphics co-processor    NVIDIA GeForce RTX 3090
Graphics RAM size        24 GB
Graphics card interface  PCI-Express
Video output interface   HDMI
Dimensions               30.48 x 15.24 x 7.62cm; 0.28g
Price                    £1245.00
            """)

        elif gpuClick == "AMD Radeon RX 6900XT":
            print("""
Brand                    MSI
Manufacturer             MSI COMPUTER
Graphics co-processor    AMD Radeon RX 6900XT
Graphics RAM size        16 GB
GPU clock speed          2425 MHz
Graphics card interface  PCI-Express 
Video output interface   HDMI
Dimensions               32.4 x 14.1 x 5.5cm; 2.3kg
Price                    £999.00
            """)

        again = input("Do you want to look at other GPU? Press 'y' to look at other GPU details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            gpuChoice = input("Choose your preference GPU from the list mentioned above: ")
            while gpuChoice not in gpu:
                print("Your choice must be from the list mentioned above!!")
                gpuChoice = input("Choose your preference GPU from the list mentioned above: ")
            else:
                PC[1] = gpuChoice
                gpuPrice = float(gpu[gpuChoice])
                cost[1] = gpuPrice


# options of Motherboard
def motherboard():
    print("\n" + "Options for Motherboard: ")
    motherboard = {"ASUS TUF Gaming X570-Plus(WiFi) ATX Motherboard": "273.99",
                   "Gigabyte B660M DS3H Micro ATX Motherboard": "121.99"}
    for keys in motherboard:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        motherboardClick = input(
            "Enter the name of the motherboard that you want to know the details from the list mentioned above: ")
        while motherboardClick not in motherboard:
            print("Your choice must be from the list mentioned above!!")
            motherboardClick = input(
                "Enter the name of the motherboard that you want to know the details from the list mentioned above: ")

        if motherboardClick == "ASUS TUF Gaming X570-Plus(WiFi) ATX Motherboard":
            print("""
Brand               ASUS
Manufacturer        ASUS
CPU socket          AM4
Memory technology   DDR4
Memory clock speed  4400 MHz
Dimension           30.5 x 24.4 x 5.5cm; 400g
Price               £273.99
            """)

        elif motherboardClick == "Gigabyte B660M DS3H Micro ATX Motherboard":
            print("""
Brand               Gigabyte
Manufacturer        Exertis(UK) Limited
CPU socket          LGA 1700
Memory technology   DDR4
Memory clock speed  3200 MHz
Dimension           60 x 60 x 85cm; 700g
Price               £121.99
            """)

        again = input("Do you want to look at other motherboard? Press 'y' to look at other motherboard details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            motherboardChoice = input("Choose your preference motherboard from the list mentioned above: ")
            while motherboardChoice not in motherboard:
                print("Your choice must be from the list mentioned above!!")
                motherboardChoice = input("Choose your preference motherboard from the list mentioned above: ")
            else:
                PC[2] = motherboardChoice
                motherboardPrice = float(motherboard[motherboardChoice])
                cost[2] = motherboardPrice


# options of RAM
def ram():
    print("\n" + "Options for RAM: ")
    ram = {"16 GB DDR4": "58.99",
           "32 GB DDR4": "112.99",
           "64 GB DDR4": "279.99"}
    for keys in ram:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        ramClick = input("Enter the name of the RAM that you want to know the details from the list mentioned above: ")
        while ramClick not in ram:
            print("Your choice must be from the list mentioned above!!")
            ramClick = input(
                "Enter the name of the RAM that you want to know the details from the list mentioned above: ")

        if ramClick == "16 GB DDR4":
            print("""
Brand                Corsair
Manufacturer         Corsair
Memory speed         3200 MHz
Dimension            15.49 x 8.99 x 0.99cm; 90.72g
Price                £58.99
            """)

        elif ramClick == "32 GB DDR4":
            print("""
Brand                Corsair
Manufacturer         Corsair
Memory speed         3200 MHz
Dimension            13.51 x 0.71 x 3.35cm; 18g
Price                £112.99
            """)

        elif ramClick == "64 GB DDR4":
            print("""
Brand                Corsair
Manufacturer         Corsair
Memory speed         3200 MHz
Dimension            13.51 x 0.71 x 3.35cm; 100g
Price                £279.99
            """)

        again = input("Do you want to look at other RAM? Press 'y' to look at other RAM details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            ramChoice = input("Choose your preference RAM from the list mentioned above: ")
            while ramChoice not in ram:
                print("Your choice must be from the list mentioned above!!")
                ramChoice = input("Choose your preference RAM from the list mentioned above: ")
            else:
                PC[3] = ramChoice
                ramPrice = float(ram[ramChoice])
                cost[3] = ramPrice


# options of Power Supply Unit
def psu():
    print("\n" + "Options for Power Supply Unit: ")
    psu = {"Corsair TX-M Series 650 Watt 80 Plus Gold Certified PSU(UK) Hybrid Modular Power Supply Unit": "79.99",
           "Corsair RMX Series 750 Watt 80 Plus Gold Certified PSU(UK) Fully Modular Power Supply": "290.96",
           "Corsair RMX White Series RM850x 850 Watt 80 Plus Gold Certified PSU(UK) Fully Modular Power Supply": "189.99"}
    for keys in psu:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        psuClick = input(
            "Enter the name of the power supply unit that you want to know the details from the list mentioned above: ")
        while psuClick not in psu:
            print("Your choice must be from the list mentioned above!!")
            psuClick = input(
                "Enter the name of the power supply unit that you want to know the details from the list mentioned above: ")

        if psuClick == "Corsair TX-M Series 650 Watt 80 Plus Gold Certified PSU(UK) Hybrid Modular Power Supply Unit":
            print("""
Brand                Corsair
Manufacturer         Corsair
Output wattage       650 watt
Cooling method       Air
Power Supply Design  Semi Modular
Dimension            15 x 14 x 8.6cm; 1.7kg
Price                £79.99
            """)

        elif psuClick == "Corsair RMX Series 750 Watt 80 Plus Gold Certified PSU(UK) Fully Modular Power Supply":
            print("""
Brand                Corsair
Manufacturer         Corsair
Output wattage       750 watt
Cooling method       Air
Power Supply Design  Full Modular
Dimension            17.98 x 8.59 x 14.99cm; 1.93kg
Price                £290.96
            """)

        elif psuClick == "Corsair RMX White Series RM850x 850 Watt 80 Plus Gold Certified PSU(UK) Fully Modular Power Supply":
            print("""
Brand                Corsair
Manufacturer         Corsair
Output wattage       850 watt
Cooling method       Air
Power Supply Design  Full Modular
Dimension            16 x 15.01 x 8.61cm; 1.6kg
Price                £189.99
            """)

        again = input(
            "Do you want to look at other power supply unit? Press 'y' to look at other power supply unit details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            psuChoice = input("Choose your preference power supply unit from the list mentioned above: ")
            while psuChoice not in psu:
                print("Your choice must be from the list mentioned above!!")
                psuChoice = input("Choose your preference power supply unit from the list mentioned above: ")
            else:
                PC[4] = psuChoice
                psuPrice = float(psu[psuChoice])
                cost[4] = psuPrice


# options of case
def case():
    print("\n" + "Options for Case: ")
    case = {"Corsair 4000D Airflow Tempered Glass Mid-Tower ATX Case": "99.99",
            "Corsair Carbide Series SPEC-05 Mid-Tower Gaming Case": "56.98",
            "MSI MAG VAMPIRIC 100R Mid Tower Gaming Computer Case": "49.99"}
    for keys in case:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        caseClick = input(
            "Enter the name of the case that you want to know the details from the list mentioned above: ")
        while caseClick not in case:
            print("Your choice must be from the list mentioned above!!")
            caseClick = input(
                "Enter the name of the case that you want to know the details from the list mentioned above: ")

        if caseClick == "Corsair 4000D Airflow Tempered Glass Mid-Tower ATX Case":
            print("""
Brand                Corsair
Manufacturer         Corsair
Fan size             120mm
Dimension            45.3 x 23 x 46.6cm; 7.85kg
Price                £99.99
            """)

        elif caseClick == "Corsair Carbide Series SPEC-05 Mid-Tower Gaming Case":
            print("""
Brand                Corsair
Manufacturer         Corsair
Fan size             120mm
Dimension            48.3 x 19.8 x 43.4cm; 4kg
Price                £56.98
            """)

        elif caseClick == "MSI MAG VAMPIRIC 100R Mid Tower Gaming Computer Case":
            print("""
Brand                MSI
Manufacturer         MSI 
Fan size             120mm
Dimension            33.5 x 20 x 44cm; 4.7kg
Price                £49.99
            """)

        again = input("Do you want to look at other case? Press 'y' to look at other case details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            caseChoice = input("Choose your preference case from the list mentioned above: ")
            while caseChoice not in case:
                print("Your choice must be from the list mentioned above!!")
                caseChoice = input("Choose your preference case from the list mentioned above: ")
            else:
                PC[5] = caseChoice
                casePrice = float(case[caseChoice])
                cost[5] = casePrice


# options of hard drive
def hardDrive():
    print("\n" + "Options for Hard Drive: ")
    hardDrive = {"Sabrent 512GB Rocket NVMe PCle M.2 Internal SSD High Performance": "79.99",
                 "Corsair Force Series MP600 1TB M.2 NVMe PCle SSD": "120.54",
                 "Samsung 970 EVO Plus 500 GB PCle NVMe M.2 Internal SSD": "76.99"}
    for keys in hardDrive:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        hardDriveClick = input(
            "Enter the name of the hard drive that you want to know the details from the list mentioned above: ")
        while hardDriveClick not in hardDrive:
            print("Your choice must be from the list mentioned above!!")
            hardDriveClick = input(
                "Enter the name of the hard drive that you want to know the details from the list mentioned above: ")

        if hardDriveClick == "Sabrent 512GB Rocket NVMe PCle M.2 Internal SSD High Performance":
            print("""
Brand                   Sabrent
Manufacturer            Sabrent
Hard disk size          512 GB
Hard disk description   Solid state hard drive
Dimension               800.1 x 2.18 x 0.28cm; 5.7g
Price                   £79.99
            """)

        elif hardDriveClick == "Corsair Force Series MP600 1TB M.2 NVMe PCle SSD":
            print("""
Brand                   Corsair
Manufacturer            Corsair
Hard disk size          1 TB
Hard disk description   Solid state hard drive
Dimension               8 x 2.3 x 1.5cm; 34g
Price                   £120.54
            """)

        elif hardDriveClick == "Samsung 970 EVO Plus 500 GB PCle NVMe M.2 Internal SSD":
            print("""
Brand                   Samsung
Manufacturer            Samsung
Hard disk size          500 GB
Hard disk description   Solid state hard drive
Dimension               8.15 x 2.21 x 0.2cm; 8g
Price                   £76.99
            """)

        again = input("Do you want to look at other SSD? Press 'y' to look at other SSD details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            hardDriveChoice = input("Choose your preference SSD from the list mentioned above: ")
            while hardDriveChoice not in hardDrive:
                print("Your choice must be from the list mentioned above!!")
                hardDriveChoice = input("Choose your preference SSD from the list mentioned above: ")
            else:
                PC[6] = hardDriveChoice
                hardDrivePrice = float(hardDrive[hardDriveChoice])
                cost[6] = hardDrivePrice


# options for optical drives
def opticalDrive():
    print("\n" + "Options for Optical Drive: ")
    opticalDrive = {"USB 3.0 External CD DVD Drive": "20.99",
                    "USB 3.0 Blu-Ray External Optical Drive": "103.49"}
    for keys in opticalDrive:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        opticalDriveClick = input(
            "Enter the name of the optical drive that you want to know the details from the list mentioned above: ")
        while opticalDriveClick not in opticalDrive:
            print("Your choice must be from the list mentioned above!!")
            opticalDriveClick = input(
                "Enter the name of the optical drive that you want to know the details from the list mentioned above: ")

        if opticalDriveClick == "USB 3.0 External CD DVD Drive":
            print("""
Brand                           Vlio
Manufacturer                    Vlio
Hardware interface              USB, CD-R, CD-RW
Hardware platform               Laptop, PC
Optical storage write speed     24x, 8x, 4x, 2.4x
Dimensions                      16.6 x 16 x 2.6cm; 100g
Price                           £20.99
            """)

        elif opticalDriveClick == "USB 3.0 Blu-Ray External Optical Drive":
            print("""
Brand                           Sutinna
Manufacturer                    Sutinna
Hardware interface              USB, CD-R, CD-RW, DVD-R, DVD-RW
Hardware platform               Laptop, PC
Optical storage write speed     24x
Dimensions                      14.7 x 14.2 x 1.4cm; 460g
Price                           £103.49
            """)

        again = input("Do you want to look at other optical drive? Press 'y' to look at other optical drive details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            opticalDriveChoice = input("Choose your preference optical drive from the list mentioned above: ")
            while opticalDriveChoice not in opticalDrive:
                print("Your choice must be from the list mentioned above!!")
                opticalDriveChoice = input("Choose your preference optical drive from the list mentioned above: ")
            else:
                PC[7] = opticalDriveChoice
                opticalDrivePrice = float(opticalDrive[opticalDriveChoice])
                cost[7] = opticalDrivePrice


# options for second hard drive
def hdd():
    print("\n" + "Options for HDD: ")
    hdd = {"1 TB Internal Hard Drive HDD": "45.90",
           "2 TB Internal Hard Drive HDD": "59.90"}
    for keys in hdd:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        hddClick = input("Enter the name of the HDD that you want to know the details from the list mentioned above: ")
        while hddClick not in hdd:
            print("Your choice must be from the list mentioned above!!")
            hddClick = input(
                "Enter the name of the HDD that you want to know the details from the list mentioned above: ")

        if hddClick == "1 TB Internal Hard Drive HDD":
            print("""
Brand                   Seagate
Manufacturer            Seagate
RAM size                6 GB
Hard drive size         1 TB
Wattage                 5.3
Dimensions              14.71 x 10.19 x 2.01cm; 449g
Price                   £45.90
            """)

        elif hddClick == "2 TB Internal Hard Drive HDD":
            print("""
Brand                   Seagate
Manufacturer            Seagate
RAM size                6 GB
Hard drive size         2 TB
Wattage                 3.7
Dimensions              10.11 x 2.01 x 14.61cm; 449g
Price                   £59.90
            """)

        again = input("Do you want to look at other HDD? Press 'y' to look at other HDD details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            hddChoice = input("Choose your preference HDD from the list mentioned above: ")
            while hddChoice not in hdd:
                print("Your choice must be from the list mentioned above!!")
                hddChoice = input("Choose your preference HDD from the list mentioned above: ")
            else:
                PC[8] = hddChoice
                hddPrice = float(hdd[hddChoice])
                cost[8] = hddPrice


# options for monitor
def monitor():
    print("\n" + "Options for Monitor: ")
    monitor = {"Dell 24 Inch Full HD Monitor": "124.99",
               "Samsung Odyssey G5 27 Inch Curved Gaming Monitor": "299.99",
               "ASUS TUF 28 Inch Gaming Monitor": "349.99"}
    for keys in monitor:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        monitorClick = input(
            "Enter the name of the monitor that you want to know the details from the list mentioned above: ")
        while monitorClick not in monitor:
            print("Your choice must be from the list mentioned above!!")
            monitorClick = input(
                "Enter the name of the monitor that you want to know the details from the list mentioned above: ")

        if monitorClick == "Dell 24 Inch Full HD Monitor":
            print("""
Brand                   Dell
Manufacturer            Dell Computers
Display size            1920 x 1080 Pixels
Dimensions              4.98 x 55.27 x 33.17cm; 3.18kg
Price                   £124.99
            """)

        elif monitorClick == "Samsung Odyssey G5 27 Inch Curved Gaming Monitor":
            print("""
Brand                   Samsung
Manufacturer            Samsung
Display size            2560 x 1440 Pixels
Dimensions              18.78 x 24.25 x 10.71cm; 4.5kg
Price                   £299.99
            """)

        elif monitorClick == "ASUS TUF 28 Inch Gaming Monitor":
            print("""
Brand                   ASUS
Manufacturer            ASUS
Display size            3840 x 2160 Pixels
Dimensions              9.06 x 25.16 x 21.65cm; 7.6kg
Price                   £349.99
            """)

        again = input("Do you want to look at other monitor? Press 'y' to look at other monitor details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            monitorChoice = input("Choose your preference monitor from the list mentioned above: ")
            while monitorChoice not in monitor:
                print("Your choice must be from the list mentioned above!!")
                monitorChoice = input("Choose your preference monitor from the list mentioned above: ")
            else:
                PC[9] = monitorChoice
                monitorPrice = float(monitor[monitorChoice])
                cost[9] = monitorPrice


# options for sound card
def soundCard():
    print("\n" + "Options for Sound Card: ")
    soundCard = {"Sound Blaster Audigy Fx Sound Card": "34.99",
                 "Sound Blaster Audigy Rx Sound Card": "59.99"}
    for keys in soundCard:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        soundCardClick = input(
            "Enter the name of the sound card that you want to know the details from the list mentioned above: ")
        while soundCardClick not in soundCard:
            print("Your choice must be from the list mentioned above!!")
            soundCardClick = input(
                "Enter the name of the sound card that you want to know the details from the list mentioned above: ")

        if soundCardClick == "Sound Blaster Audigy Fx Sound Card":
            print("""
Brand                   CREATIVE
Manufacturer            Creative Labs (Europe) Limited
Audio output mode       Stereo
Dimensions              30.6 x 18 x 6.9cm; 260g
Price                   £34.99
            """)

        elif soundCardClick == "Sound Blaster Audigy Rx Sound Card":
            print("""
Brand                   CREATIVE
Manufacturer            Creative Labs (Europe) Limited
Audio output mode       Surround
Dimensions              14.5 x 11.99 x 1.8cm; 120g
Price                   £59.99
            """)

        again = input("Do you want to look at other sound card? Press 'y' to look at other soundCard details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            soundCardChoice = input("Choose your preference sound card from the list mentioned above: ")
            while soundCardChoice not in soundCard:
                print("Your choice must be from the list mentioned above!!")
                soundCardChoice = input("Choose your preference sound card from the list mentioned above: ")
            else:
                PC[10] = soundCardChoice
                soundCardPrice = float(soundCard[soundCardChoice])
                cost[10] = soundCardPrice


# options for mouse
def mouse():
    print("\n" + "Options for Mouse: ")
    mouse = {"Wired Mouse": "6.99",
             "Wireless Mouse": "22.99"}
    for keys in mouse:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        mouseClick = input(
            "Enter the name of the mouse that you want to know the details from the list mentioned above: ")
        while mouseClick not in mouse:
            print("Your choice must be from the list mentioned above!!")
            mouseClick = input(
                "Enter the name of the mouse that you want to know the details from the list mentioned above: ")

        if mouseClick == "Wired Mouse":
            print("""
Brand                     Logitech
Manufacturer              Logitech
Connectivity technology   USB
Voltage                   5 Volts
Dimensions                6.2 x 3.8 x 11.3cm; 90g
Price                     £6.99
            """)

        elif mouseClick == "Wireless Mouse":
            print("""
Brand                     Logitech
Manufacturer              Logitech
Connectivity technology   USB
Voltage                   1.5 Volts
Dimensions                9.9 x 6 x 3.9cm; 75.2g
Price                     £22.99
            """)

        again = input("Do you want to look at other mouse? Press 'y' to look at other mouse details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            mouseChoice = input("Choose your preference mouse from the list mentioned above: ")
            while mouseChoice not in mouse:
                print("Your choice must be from the list mentioned above!!")
                mouseChoice = input("Choose your preference mouse from the list mentioned above: ")
            else:
                PC[11] = mouseChoice
                mousePrice = float(mouse[mouseChoice])
                cost[11] = mousePrice


# options for keyboard
def keyboard():
    print("\n" + "Options for Keyboard: ")
    keyboard = {"Wired Keyboard": "28.49",
                "Wireless Keyboard": "52.99"}
    for keys in keyboard:
        print(keys, "")
        time.sleep(0.3)
    # to ask the user input until the valid data is entered
    Loop = True
    while Loop == True:
        keyboardClick = input(
            "Enter the name of the keyboard that you want to know the details from the list mentioned above: ")
        while keyboardClick not in keyboard:
            print("Your choice must be from the list mentioned above!!")
            keyboardClick = input(
                "Enter the name of the keyboard that you want to know the details from the list mentioned above: ")

        if keyboardClick == "Wired Keyboard":
            print("""
Brand                     Kensington
Manufacturer              Kensington
Connectivity technology   USB
Dimensions                0.45 x 0.18 x 0.03cm; 800g
Price                     £28.49
            """)

        elif keyboardClick == "Wireless Keyboard":
            print("""
Brand                     Kensington
Manufacturer              Kensington
Connectivity technology   Wireless
Dimensions                18.9 x 44.9 x 3.4cm; 820g
Price                     £52.99
            """)

        again = input("Do you want to look at other keyboard? Press 'y' to look at other keyboard details ")
        if again == "y":
            Loop = True
        else:
            Loop = False
            keyboardChoice = input("Choose your preference keyboard from the list mentioned above: ")
            while keyboardChoice not in keyboard:
                print("Your choice must be from the list mentioned above!!")
                keyboardChoice = input("Choose your preference keyboard from the list mentioned above: ")
            else:
                PC[12] = keyboardChoice
                keyboardPrice = float(keyboard[keyboardChoice])
                cost[12] == keyboardPrice

            # to add optional items


def addItems():
    Loop = True
    oItems = ["optical drive", "hdd", "monitor", "sound card", "mouse", "keyboard"]
    while Loop == True:
        add = input("\n" + "Do you want to add optional items to your PC? Type 'y' to add: ").lower()
        if add == "y":
            print("You can add these items:")
            for x in oItems:
                print(x, "")
                time.sleep(0.3)
            add = input("Which item do you want to add? ").lower()
            # to ask the user input until the valid data is entered
            while add not in oItems:
                add = input("Which item do you want to add? ")
            if add == "optical drive":
                opticalDrivePrice = opticalDrive()
                cost[7] = opticalDrivePrice
                Loop = True
            elif add == "hdd":
                hddPrice = hdd()
                cost[8] = hddPrice
                Loop = True
            elif add == "monitor":
                monitorPrice = monitor()
                cost[9] = monitorPrice
                Loop = True
            elif add == "sound card":
                soundCardPrice = soundCard()
                cost[10] = soundCardPrice
                Loop = True
            elif add == "mouse":
                mousePrice = mouse()
                cost[11] = mousePrice
                Loop = True
            elif add == "keyboard":
                keyboardPrice = keyboard()
                cost[12] = keyboardPrice
                Loop = True
        else:
            Loop = False


# check the compatiblity of the PC's components
def check():
    aa = True
    while aa == True:
        changeItem = input(
            "\n" + "Do you want to change your selection before finalizing? Type 'y' to change items ").lower()
        if changeItem == "y":
            change()
            aa = True
        else:
            aa = False
            a = ["c", "m"]
            b = ["m", "g"]
            # checking the compatibility of the component and make the user change the item
            while (PC[0] == "Intel core i9 12900K" and PC[2] == "ASUS TUF Gaming X570-Plus(WiFi) ATX Motherboard") or (
                    PC[0] == "AMD Ryzen 9 5900X" and PC[2] == "Gigabyte B660M DS3H Micro ATX Motherboard"):
                print("You cannot use " + PC[0] + " together with " + PC[2])
                replace = input("Type 'c' to change CPU or 'm' to change Motherboard: ").lower()
                while replace not in a:
                    replace = input("Type 'c' to change CPU or 'm' to change Motherboard: ").lower()
                if replace == "c":
                    cpu()
                elif replace == "m":
                    motherboard()

            # checking the compatibility of the component and make the user change the item
            while (PC[2] == "ASUS TUF Gaming X570-Plus(WiFi) ATX Motherboard" and PC[1] == "NVIDIA GeForce RTX 3090"):
                print("You cannot use " + PC[2] + " together with " + PC[1])
                replace = input("Type 'm' to change Motherboard or 'g' to change GPU: ").lower()
                while replace not in b:
                    replace = input("Type 'm' to change Motherboard or 'g' to change GPU: ").lower()
                if replace == "m":
                    motherboard()
                elif replace == "g":
                    gpu()
            print("You have finalized your customized PC.")
            # code modified from https://www.geeksforgeeks.org/precision-handling-python/
            # date accessed 30 October 2022
            # code modified from https://www.geeksforgeeks.org/sum-function-python/#:~:text=Python%20provides%20an%20inbuilt%20function,of%20numbers%20in%20the%20iterable.
            # Date accessed 3 November 2022
            total = math.fsum(cost)
            total = round(total, 3)
            PC[13] = total
            print("Your customized PC costs £", total)


# changing the selected items before finalizing
def change():
    items = ["cpu", "gpu", "motherboard", "ram", "psu", "case", "hard drive", "optical drive", "hdd", "monitor",
             "sound card", "mouse", "keyboard"]
    print("\n" + "Which item do you want to change? ")
    for x in items:
        print(x, "")
        time.sleep(0.3)
    itemChange = input("Type the item that you want to change: ").lower()
    # to ask the user input until the valid data is entered
    while itemChange not in items:
        itemChange = input("Type the item that you want to change: ").lower()
    if itemChange == "cpu":
        cpu()
    elif itemChange == "gpu":
        gpu()
    elif itemChange == "motherboard":
        motherboard()
    elif itemChange == "ram":
        ram()
    elif itemChange == "psu":
        psu()
    elif itemChange == "case":
        case()
    elif itemChange == "hard drive":
        hardDrive()
    elif itemChange == "optical drive":
        opticalDrive()
    elif itemChange == "hdd":
        hdd()
    elif itemChange == "monitor":
        monitor()
    elif itemChange == "sound card":
        soundCard()
    elif itemChange == "mouse":
        mouse()
    elif itemChange == "keyboard":
        keyboard()


# write file
def writeFile():
    file = open("PC.txt", "a")
    file.write(str(PC) + "\n")
    file.close


# main
PC = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
cost = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
print(
    "This is a PC builder system. For convenient usage, it is recommended to copy and paste the model of the components that you like." + "\n")
createFile()
cpu()
gpu()
motherboard()
ram()
psu()
case()
hardDrive()
addItems()
check()
writeFile()
