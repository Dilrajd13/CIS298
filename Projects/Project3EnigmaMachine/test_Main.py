from unittest import TestCase, main
from Main import EnigmaMachine, Rotor, Reflector, PlugBoard


class TestRotor(TestCase):

    def test_forward_substitution(self):
        # Arrange: Create a rotor with known wiring and starting position 0.
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)

        # Act: Substitute the letter 'A'
        result = rotor.substitution("A")

        # Assert: With no rotation, 'A' should map to 'E'
        self.assertEqual(result, "E")

    def test_reverse_substitution(self):
        # Arrange: Create the same rotor with starting position 0.
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)

        # Act: Reverse substitute the letter 'E'
        result = rotor.reverse_substitution("E")

        # Assert: With no rotation, the reverse mapping of 'E' should be 'A'
        self.assertEqual(result, "A")


class TestReflector(TestCase):

    def test_application(self):
        # Arrange: Create a reflector instance.
        reflector = Reflector()

        # Act: Apply the reflector mapping to letter 'A'
        result = reflector.application("A")

        # Assert: Based on its wiring, 'A' should map to 'Y'
        self.assertEqual(result, "Y")


class TestPlugBoard(TestCase):

    def test_plugboard_bidirectional(self):
        # Arrange: Create a plugboard with a simple mapping.
        pb = PlugBoard({"A": "Z"})

        # Act: Map letter 'A' and letter 'Z' through the plugboard.
        result_forward = "".join(pb.message_to_plugboard(list("A")))
        result_reverse = "".join(pb.message_to_plugboard(list("Z")))

        # Assert: 'A' maps to 'Z' and 'Z' maps to 'A'
        self.assertEqual(result_forward, "Z")
        self.assertEqual(result_reverse, "A")


class TestEnigmaMachine(TestCase):

    def setUp(self):
        # Arrange: Create an Enigma machine with three rotors and a plugboard mapping.
        self.machine = EnigmaMachine(
            r1=1, r1p=0,
            r2=2, r2p=0,
            r3=3, r3p=0,
            plugset={"A": "B"}
        )
        self.machine.new_rotor_config(1, "rotor1", 0)
        self.machine.new_rotor_config(2, "rotor2", 0)
        self.machine.new_rotor_config(3, "rotor3", 0)
        self.machine.plug_board = PlugBoard({"A": "B"})

    def test_new_rotor_config(self):
        # Act: Retrieve rotor1's configuration and starting position.
        config = self.machine.rotor1.rotoconfig
        start = self.machine.rotor1.rotostartpos

        # Assert: Rotor1 should use the standard alphabet and start at 0.
        self.assertEqual(config, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(start, 0)

    def test_encrypt_decrypt_cycle(self):
        # Arrange: Define the original message.
        original = "HELLO"

        # Act: Encrypt the message.
        encrypted = self.machine.encryption(original)

        # Reset rotor positions before decryption.
        self.machine.rotor1.rotostartpos = self.machine.r1p
        self.machine.rotor2.rotostartpos = self.machine.r2p
        self.machine.rotor3.rotostartpos = self.machine.r3p

        # Decrypt the message.
        decrypted = self.machine.decryption(encrypted)

        # Assert: The decrypted message should match the original.
        self.assertEqual(decrypted, original)


if __name__ == "__main__":
    main()
