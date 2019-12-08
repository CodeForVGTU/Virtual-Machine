import os
import binascii # Convert between binary and ASCII
import array as arr
from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem, FunctionItem

pos = 0
counter = 1
text_f = open("q1_encr.txt")
all_text = text_f.read()
text_f.close()
regs = arr.array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # B is data type of unsigned char
flag_eof = 0  # flag register (on or off)

def vm_menu():
    menu = ConsoleMenu("Virtual Machine", "Created with Python")

    submenu = ConsoleMenu("About Us")
    submenu.prologue_text = "This is Virtual Machine. Created by Vilnius Gediminas " \
    						"Technical University PRIfs 18/6 student - Rimvydas Kanapka." \
                            " This program is created for Architecture of Computers and Computer Networks."

    menu.append_item(FunctionItem("Start VM", main))  # First menu item
    menu.append_item(SubmenuItem("About Us", submenu, menu=menu))  # Second menu item
    menu.show()

def command_list(code, value, file_name):
	x = int(value[1:2], 16)
	y = int(value[:1], 16)
	yx = int(value, 16)
	# Byte in Java is represented by signed int in range (-128, 127), Byte Python is represented by unsigned int in range(0, 255). So I need to convert the 8-bit byte in python to signed int to make comparison done.
	if yx > 127:  # if hex value is higher than 127 after conversation, we calculate
		yx = (256 - yx) * (-1)
	global flag_eof
	global counter
	global all_text

	if code == "01":  # Registrą x padidina vienetu.
		regs[x] = regs[x] + 1
	elif code == "02":  # Registrą x sumažina vienetu.
		regs[x] = regs[x - 1]
	elif code == "03":  # Kopijuoja registro y turinį į registrą x.
		regs[x] = regs[y]
	elif code == "04":  # Kopijuoja baito konstantą į registrą R0
		regs[0] = yx
	elif code == "05":  # Registro x postūmis į kairę per vieną bitą.
		regs[x] = regs[x] << 1
	elif code == "06":  # Registro R x postūmis į dešinę per vieną bitą.
		regs[x] = regs[x] >> 1
	elif code == "07":  # Šuolis santykiniu adresu pridedant konstantą su ženklu prie komandų skaitiklio.
		counter += yx / 2
	elif code == "08":  # Šuolis santykiniu adresu pridedant konstantą su ženklu prie komandų skaitiklio, jeigu yra nulio požymis (angl. flag on).
		if flag_eof == 0:
			counter += yx / 2
	elif code == "09":  # "Šuolis santykiniu adresu pridedant konstantą su ženklu prie komandų skaitiklio, jeigu nėra nulio požymio (angl. flag off).
		if flag_eof != 0:
			counter += yx / 2
	elif code == "0a":  # Šuolis santykiniu adresu pridedant konstantą su ženklu prie komandų skaitiklio, jeigu yra failo pabaigos požymis (IN).
		if flag_eof == 1:
			counter += yx / 2
	elif code == "0b":  # Virtuali mašina baigia darbą.
		vm_menu() # work finished, back to menu
	elif code == "0c":  # SUDĖTIS tarp registrų: x = x + y
		regs[x] = regs[x] + regs[y]
	elif code == "0d":  # ATIMTIS tarp registrų: x = x − y
		regs[x] = regs[x] - regs[y]
	elif code == "0e":  # IŠIMTINIO ARBA operacijų tarp registrų: x = x ⨁ y
		regs[x] = regs[x] ^ regs[y]
	elif code == "0f":  # ARBA operacija tarp registrų: x = x ∨ y
		regs[x] = regs[x] | regs[y]
	elif code == "10":  # Skaito vieną baitą iš duomenų failo (priskiria Rx ) ir nustato failo pabaigos požymį jeigu pasiekta failo pabaiga.
		global pos

		try:
			symbol = all_text[pos] # symbol which we need
			pos += 1 # position of that symbol increases
			regs[x] = ord(symbol)  # char to int
		except IndexError:
			flag_eof = 1
	elif code == "11":  # Registro x turinį išveda į failą."
		f = open(file_name, "a")
		f.write(chr(regs[x]))
		f.close()


def read_binary():
   print("Enter a binary file name (with type).\n")
   file_name = "none"

   while not os.path.isfile(file_name):
    file_name = input()

    if not os.path.isfile(file_name):
        print("File " + file_name + " doesn't exist!")

    with open(file_name, "rb") as f: # reading binary file
        buff = f.read()
    f.close()

    line = binascii.hexlify(buff)
    hex_string = [line[i:i+2] for i in range(0, len(line), 2)]

    it = iter(hex_string)
    data = {}

    x = 1  # x will be position of Virtual Command in dictionary
    for simb in it:
        command_code = str(simb)[2:4]
        command_value = str(next(it))[2:4]
        data[x] = [command_code, command_value]
        x += 1

    return data

def main():
	global counter
	commands = read_binary()

	file_name = input("Enter a output file name (with type).\n")

	while True:
		temp = counter
		try:
			command_list(commands[counter][0], commands[counter][1], file_name)  # [0] - command, [1] - command's code
		except KeyError:
			break
		if temp == counter:
			counter += 1

vm_menu()