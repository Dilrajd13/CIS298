

class EnigmaMachine:
    def __init__(self, r1=0, r1p=0, r2=0, r2p=0, r3=0, r3p=0, plugset=dict()):

        self.r1 = r1
        self.r1p = r1p

        self.r2 = r2
        self.r2p = r2p

        self.r3 = r3
        self.r3p = r3p

        self.ro1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ro2 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.ro3 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        self.ro4 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        self.ro5 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"

        self.rotor1 = None
        self.rotor2 = None
        self.rotor3 = None

        self.msg = None
        self.plugset = plugset
        self.plug_board = None

        self.ref_number_one = Reflector()
        print("constructed")
        print(r1)

    def new_rotor_config(self, rotor, rot_name, start_pos):
        if rotor == 1:
            setattr(self, rot_name, Rotor(self.ro1, start_pos))
        elif rotor == 2:
            setattr(self, rot_name, Rotor(self.ro2, start_pos))
        elif rotor == 3:
            setattr(self, rot_name, Rotor(self.ro3, start_pos))
        elif rotor == 4:
            setattr(self, rot_name, Rotor(self.ro4, start_pos))
        elif rotor == 5:
            setattr(self, rot_name, Rotor(self.ro5, start_pos))
        else:
            print("invalid rotor number")

    def pr(self):
        print(self.r1)
        print(self.plugset)

    def getmsg(self, msg):
        self.msg=msg
    def rotate_roters(self):
        self.rotor1.rotostartpos = (self.rotor1.rotostartpos + 1) % 26
        self.rotor1.rot_count += 1

        if self.rotor1.rot_count % 26 == 0:
            self.rotor2.rotostartpos = (self.rotor2.rotostartpos + 1) % 26
            self.rotor2.rot_count += 1

            if self.rotor2.rotation_count % 26 == 0:
                self.rotor3.rotostartpos = (self.rotor3.rotostartpos + 1) % 26
    def send_through_rotors_and_transform_word(self, jor):
        for i in range(len(jor)):
            self.rotate_roters()

            if self.plug_board:
                lett = self.plug_board.message_to_plugboard([jor[i]])[0]
            else:
                lett = jor[i]


            lett = self.rotor1.substitution(lett)
            lett = self.rotor2.substitution(lett)
            lett = self.rotor3.substitution(lett)

            lett = self.ref_number_one.application(lett)

            lett = self.rotor3.reverse_substitution(lett)
            lett = self.rotor2.reverse_substitution(lett)
            lett = self.rotor1.reverse_substitution(lett)

            if self.plug_board:
                lett = self.plug_board.message_to_plugboard([lett])[0]

            jor[i] = lett
        return jor


    def encryption(self,message):
        # print("sending to plugboard")
        journey = list(message.upper())
        # print(f'{journey} AFTER PLUGBOARD')

        # print("Sending To Rotors")
        journey = self.send_through_rotors_and_transform_word(journey)
        # print(f'{journey} AFTER ROTORS')

        encrypted_message = "".join(journey)
        print(f"Encrypted Message: {encrypted_message}")
        return encrypted_message


    def decryption(self, encrypted_message):
        print("RESETTING ROTORS FOR DECRYPTION")

        self.rotor1.rotostartpos = self.r1p
        self.rotor2.rotostartpos = self.r2p
        self.rotor3.rotostartpos = self.r3p

        print("DECRYPTING MESSAGE")
        journey = list(encrypted_message.upper())

        journey = self.send_through_rotors_and_transform_word(journey)

        decrypted_message = "".join(journey)
        print(f"Decrypted Message: {decrypted_message}")
        return decrypted_message
class Rotor:
    def __init__(self, rotoconfig="", rotostartpos=0):
        self.rotoconfig = rotoconfig
        self.rotostartpos = rotostartpos
        self.msg = None
        self.rot_count = 0

        # purpose is to take a msg and substitute each letter in msg with corresponding wiring in a rotor
    # basically it need to first map the corresponding letter and swap
    # then it needs to increase the starting pos by 1
    # function take a letter and gets the letter it will swap with
    def substitution(self, letter):
        english_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = english_alphabet.index(letter)
        index = (index+self.rotostartpos) % 26
        letter = self.rotoconfig[index]

        return letter

    def reverse_substitution(self, letter):
        english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = self.rotoconfig.index(letter)
        original_index = (index - self.rotostartpos) % 26
        return english_alphabet[original_index]
class Reflector:
    def __init__(self):
        self.ref_maping = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def application(self,letter):
        index = self.alphabet.index(letter)
        return self.ref_maping[index]
class PlugBoard:
    def __init__(self, plug_board=None):
        self.plug_board = {}

        if plug_board:
            for key, value in plug_board.items():
                self.plug_board[key] = value
                self.plug_board[value] = key

        print("Plugboard Updated Successfully")
        print(self.plug_board)

# take msg and convert each letter based on plugboard switches.
    def message_to_plugboard(self, msg):
        for i in range(len(msg)):

            if msg[i] in self.plug_board:
                msg[i] = self.plug_board[msg[i]]

        return msg

if __name__ == '__main__':
    while True:

        choice = int(input("""WILLKOMMEN BEI DER NAZI ENIGMA MACHINE
        1.CONFIGURE ENIGMA MACHINE SETTINGS
        2.ENCRYPT Message
        3.DECRYPT Message
        4.EXIT
        """))
        if choice == 1:
            print("SETTING")
            one = EnigmaMachine()

            one.r1 = int(input("Enter first rotor"))
            one.r1p = int(input("Enter first rotor position"))
            one.new_rotor_config(one.r1, "rotor1", one.r1p)

            print("Rotor1 configuration:", one.rotor1.rotoconfig)
            print("Rotor1 start position:", one.rotor1.rotostartpos)

            one.r2 = int(input("Enter second rotor"))
            one.r2p = int(input("Enter second rotor position"))
            one.new_rotor_config(one.r2, "rotor2", one.r2p)

            print("Rotor2 configuration:", one.rotor2.rotoconfig)
            print("Rotor2 start position:", one.rotor2.rotostartpos)

            one.r3 = int(input("Enter third rotor"))
            one.r3p = int(input("Enter third rotor position"))
            one.new_rotor_config(one.r3, "rotor3", one.r3p)

            print("Rotor3 configuration:", one.rotor3.rotoconfig)
            print("Rotor3 start position:", one.rotor3.rotostartpos)

            count = 0
            while True:
                count += 1
                if int(input("If you want to add plugboard pairs press 1 to exit press 2")) == 1 and count < 4:
                    print("Enter a letter then enter the letter you want to connect ")
                    key = input("Mapping ").upper()
                    val = input("TO ").upper()

                    if key != val:
                        one.plugset[key] = val
                        one.plugset[val] = key
                    else:
                        print("cant map to yourself")

                else:
                    print("max pairs reached or User Exit")
                    break

            # if plugset does not equal empty dic then transfer plugboard settings.
            if one.plugset != {}:
                plug = PlugBoard(one.plugset)

        elif choice == 2:
            print("ENCRYPT")
            message = input("Please Enter a Message to Encrypt.").upper()
            encrypted_text = one.encryption(message)
            # print(f'{encrypted_text} ORIGINAL MESSAGE')



        elif choice == 3:
            print("DECRYPT")
            encrypted_message = input("Please Enter a Message to Decrypt: ").upper()
            decrypted_text = one.decryption(encrypted_message)

        elif choice == 4:
            print("EXIT")
            break

