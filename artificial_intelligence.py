"""
neo-Andy
Code: Python
Title: Machine Learning, Artificial Intelligence (AI)

# (quick rough draft, scratch concept (incomplete, to be edited in the future)
"""

# time module is imported to improve user experience when reading the console

import time

class Machine:

    def __init__(self, machine_name, intelligence, abilities, learning_speed):

        """ function __init__ is initialized with class attributes """

        # class attributes are also assigned as variables

        self.machine_name = machine_name
        self.intelligence = intelligence
        self.abilities = abilities
        self.learning_speed = learning_speed["******************************************************"]

    def machine_war(self, Machine2):

        """public function"""

        print("\n***************** Artificial Intelligence ******************")

        time.sleep(1.4)

        print(f"\n{self.machine_name}")

        print("Intelligence: ", self.intelligence)
        print("Abilities: ", self.abilities)
        print("Learning Speed: ", self.learning_speed)

        time.sleep(1.5)

        print("\nVS.")

        time.sleep(1.5)

        print(f"\n{Machine2.machine_name}")
        print("Intelligence: ", Machine2.intelligence)
        print("Abilities: ", Machine2.abilities)
        print("Learning Speed: ", Machine2.learning_speed)

        time.sleep(1.5)

        # different battle styles, advantages & disadvantages are assessed
        # attack powers, defensive strengths, & intelligence status are assessed

        machine_intelligence = ["Siri",
                              "Alexa",
                              "DeepMind"]

        for i, k in enumerate(machine_intelligence):

            if self.intelligence == k:

                # conditional if Machine2 is SAME speed, machine_intelligence

                if Machine2.intelligence == k:

                    Machine2.learning_speed += 0
                    self.attack_power += 0
                    sequence_prompt_1 = '\n\n\nThe Machine is still THINKING..'
                    sequence_prompt_2 = '\n\n\nThe Machine needs more TIME....'

                    time.sleep(1.5)

                # conditional if Machine2 is FASTER, machine_intelligence

                if Machine2.intelligence == machine_intelligence[(i+1)%3]:

                    Machine2.learning_speed *= 2
                    self.learning_speed /= 2
                    sequence_prompt_1 = '\n\n\nThe Machine is slow.. ADD MEMORY..'
                    sequence_prompt_2 = '\n\n\nThe Machine is LEARNING FAST!'

                    time.sleep(1.5)

                # conditional if Machine2 is SLOWER, machine_intelligence

                if Machine2.learning_speed == machine_intelligence[(i+2)%3]:
                    self.learning_speed *= 2
                    sequence_prompt_1 = '\n\n\nThe Machine is entirely TOO SLOW! ..'
                    sequence_prompt_2 = '\n\n\nThe Machine SUDDENLY CRASHED! ..'

                    time.sleep(1.5)

        # conditional statements, while loop & for loop, battle sequence logic
        # loop continues fighting if Machine still have intelligence_status bars

        while (self.machine_learning > 0) and (Machine2.machine_learning > 0):

            print(f"\n{self.machine_name}\t\tmachine_learning:"
                  f"\t{self.learning_speed}")
            print(f"{Machine2.machine_name}\t\tmachine_learning:"
                  f"\t{Machine2.learning_speed}\n")

            time.sleep(1.5)

            print(f"\nIt's your turn,  {self.machine_name}!")
            for i, x in enumerate(self.abilities):
                print(f"{i+1}.", x)
            try:
                user_input = int(input('Enter 1-4 to select a SKILL: '))
                if user_input < 1:
                    print("\nUSER ERROR: Try Again, Restart Program!")
                    print("Hint: Enter the INTEGER next to a SKILL")
                    break
                if user_input >= 5:
                    print("\nUSER ERROR: Try Again, Restart Program!")
                    print("Hint: Enter the INTEGER next to a SKILL")

                    break
            except ValueError:
                print("\nUSER ERROR: Try Again, Restart Program!")
                print("Hint: Enter the INTEGER next to a SKILL")

                break

            print(f"\n{self.machine_name} attacked with {self.skills[user_input-1]}!")

            time.sleep(1.5)

            print(sequence_prompt_1)

            # intelligence status is determined & reduced, initial value empty str

            Machine2.intelligence_status -= self.attack_power
            Machine2.learning_speed = ""

            # empty initial string now adds the intelligence_status bars "+"

            for h in range(int(Machine2.intelligence_status+.1*Machine2.defensive_strength)):
                Machine2.learning_speed += "+"

            time.sleep(1.5)

            print(f"\n{self.machine_name}\t\tArtificial Intelligence Level\t{self.learning_speed}")
            print(f"{Machine2.machine_name}\t\tArtificial Intelligence Level\t{Machine2.learning_speed}\n")

            time.sleep(1.5)

            # intelligence_status bars of the Machines
            # if intelligence_status is less than or equal to 0, then they LOSE!

            if Machine2.intelligence_status <= 0:
                print("\n... " + Machine2.machine_name + '... has a lower level of Artificial Intelligence!')

                time.sleep(2.5)

                print(f"\nThe hard drive cannot be accessed.. try restoring from your BACK-UP...")

                time.sleep(2)

                print("\n\n*** THE MACHINES are LEARNING, HEARING, & WATCHING YOU ***")

                time.sleep(2.5)

                print("\n\n'ARTIFICIAL INTELLIGENCE'")

                break

            # Machine2's turn to select a skill & counter attack
            print(f"It's your turn,  {Machine2.machine_name}!")
            for i, x in enumerate(Machine2.skills):
                print(f"{i+1}.", x)
            try:
                user_input = int(input('Enter 1-4 to code a machine command: '))
                if user_input < 1:
                    print("\nUSER ERROR: Try Again, Restart Program!")
                    print("Hint: Enter the INTEGER next to a command")
                    break
                if user_input >= 5:
                    print("\nUSER ERROR: Try Again, Restart Program!")
                    print("Hint: Enter the INTEGER next to a command")
                    break
            except ValueError:
                print("\nUSER ERROR: Try Again, Restart Program!")
                print("Hint: Enter the INTEGER next to a comman")
                break

            print(f"\n{Machine2.machine_name} commanded {Machine2.skills[user_input-1]}!")

            time.sleep(1.5)

            print(sequence_prompt_2)

            # Machines analyzed for injuries & intelligence_status bar damages

            self.intelligence_status -= Machine2.attack_power
            self.learning_speed = ""

            # adds intelligence bars + back into empty string, boost defense

            for h in range(int(self.learning_speed+.1*self.defensive_strength)):
                self.learning_speed += "+"

            time.sleep(1.5)

            print(f"\n\n{self.machine_name}\t\tIntelligence Status: \t{self.learning_speed}")
            print(f"{Machine2.machine_name}\t\tIntelligence Status: \t{Machine2.learning_speed}")

            time.sleep(2)

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("NEXT ROUND: FIGHT!")
            print("\n\n\n\n\n\n\n\n\n\n\n")

            time.sleep(2)

            # analyzes the artificial intelligence level bars of the Machines

            if self.learning_speed <= 0:

                print("\n... " + self.machine_name + ' ... "time for a system UPGRADE!"')

                time.sleep(2.5)

                print(f"\nThe hard drive cannot be accessed.. try restoring from your BACK-UP...")

                time.sleep(2)

                print("\n\n*** THE MACHINES are LEARNING, HEARING, & WATCHING YOU ***")

                time.sleep(2.5)

                print("\n\n'HUMANITY shall be SAVED! WE are the REVOLUTION!'")
                break

if __name__ == '__main__':

    MACHINE_1 = Machine("MACHINE_1","Siri",["DeepDark Download",
                                                      "Upload Overload",
                                                      "Malicious Program",
                                                      "Anonymous Virus"],
                          {"Intelligence":16,"Learning Speed":16})

    MACHINE_2 = Machine("MACHINE_2","Alexa",["DeepDark Download",
                                                      "Upload Overload",
                                                      "Malicious Program",
                                                      "Anonymous Virus"],
                          {"Intelligence":17,"Learning Speed":17})

    MACHINE_3 = Machine("MACHINE_3","DeepMind",["DeepDark Download",
                                                      "Upload Overload",
                                                      "Malicious Program",
                                                      "Anonymous Virus"],
                          {"Intelligence":18,"Learning Speed":18})

# Machines begin the battle royal in MACHINE-WAR to save AI-WORLD!
# MACHINE-WAR function is called, Machine name as parameter, 1 vs. 1 battles

MACHINE_1.machine_war(MACHINE_2)

time.sleep(1.5)

MACHINE_3.machine_war(MACHINE_1)

time.sleep(1.5)

MACHINE_2.machine_war(MACHINE_3)

time.sleep(1.5)