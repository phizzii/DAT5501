from datetime import datetime
import time

# use threading to make a background task that runs in a different thread to the main program
import threading

# class Pet with definitions
class Pet:

    # initialise pet attributes
    def __init__(self, name, birthdate):
        self.name = name              # name of the pet
        self.birthdate = birthdate    # birthdate as a datetime object (use it to calculate age later on)
        self.hunger = 100             # hunger level (100 = full, 0 = starving)
        self.energy = 100             # energy level (100 = full of energy, 0 = tired)
        self.is_sleeping = False      # check if the pet is sleeping
        self.is_bored = False         # check if the pet is bored
        self.is_full = False          # check if the pet is full from food
        self.interactions = []        # list to store past interactions (e.g., "fed", "exercised")
        self.last_interaction_time = time.time()  # track the time of the last interaction

        # start background thread to decrease hunger and energy over time
        self.start_timer()
        
    # function to start timer for decreasing stats
    def start_timer(self):
        def decrease_stats():
            while True:
                time.sleep(600)  # every 10mins stats decease
                self.decrease_hunger()
                self.decrease_energy()

        # create & start background thread
        timer_thread = threading.Thread(target=decrease_stats)
        timer_thread.daemon = True  # set to true to stop when the program terminates
        timer_thread.start()

    # function to decrease hunger
    def decrease_hunger(self):
        # if pet is not starving
        if self.hunger > 0:
            # decrease hunger by 1
            self.hunger = self.hunger - 1
        if self.hunger <= 30:
            print(self.name,"is starting to feel hungry!!")
        if self.hunger == 0:
            print(self.name,"is absolutely starvingggg !!!")

    # function to decrease energy
    def decrease_energy(self):
        # if pet is not completely exhausted
        if self.energy > 0:
            # decrease energy by 1
            self.energy = self.energy - 1
        if self.energy < 30:
            print(self.name,"is getting soooo tired, yawnnnn")

    # function to get the age of pet
    def get_age(self):

        # obtains current date & time
        today = datetime.now()

        # calculates birth year
        ageYear = today.year - birthdate.year

        # adjust if months & days don't work e.g., if born in December and it is currently March, you can't take away 12 from 3
        if ageYear == 0:
            if today.month <= birthdate.month:
                ageMonth = birthdate.month - today.month
            if today.month >= birthdate.month:
                ageMonth = today.month - birthdate.month
            if today.day <= birthdate.day:
                ageDay = birthdate.day - today.day
            if today.day >= birthdate.day:
                ageDay = today.day - birthdate.day
        else:
            print(self.name,"is",ageYear,"years,",ageMonth,"months and",ageDay,"days old!")
        if ageMonth == 0:
            if ageDay == 0:
                print(self.name,"is a wee newborn!")
            else:
                print(self.name,"is",ageDay,"days old!")

    # function to feed pet when hungry
    def feed(self):
        if self.hunger == 0:
            print(self.name,"is already full !!! don't be overfeeding")
            return

        # increase hunger by 30, not going over 100
        self.hunger = min(self.hunger + 30, 100)

        # pet is full if hunger == 100
        self.is_full = self.hunger == 100

        # append to list of interactions so user can see what they've done
        self.interactions.append("fed")
        print(self.name,"has been fed yayyyy!!")

    # function to check if pet is hungry
    def check_hunger(self):
        if self.hunger == 100:
            print(self.name,"is full :)")
        elif self.hunger > 70:
            print(self.name,"is not hungry yet >:(")
        elif self.hunger > 30:
            print(self.name,"is getting a lil hungry here!!!!")
        else:
            print(self.name,"is rEALLY hungryy!!!")

    # function to put pet to sleep (to increase energy levels)
    def sleep(self):
        if self.is_sleeping == True:
            print("woahhh there matey!!",self.name,"is already asleep!")
        else:
            # puts pet to sleep
            self.is_sleeping = True
            print(self.name,"is now asleep, zzZZ")

            # restores energy to max after going to sleep
            self.energy = 100

            # time for sleeping (20 mins)
            time.sleep(1200)
            print("huzzah",self.name,"has awoken now renewed")

    # function to wake up pet if it is asleep
    def wake_up(self):
        if self.is_sleeping == True:
            self.is_sleeping = False
            print(self.name,"has woken up!")
        else:
            print(self.name,"is already awake silly billy!!")

    # function to make pet do exercise
    def exercise(self):
        if self.energy > 30:
            
            # decrease energy by 30
            self.energy = self.energy - 30

            # decrease hunger after exercise not going past 0
            self.hunger = max(self.hunger - 20, 0)

            # adding exercise to list of past interactions
            self.interactions.append("exercised")
            print(self.name,"did some exercise")
        else:
            print(self.name,"is too tired to exercise :(( give them some rest")

    # function to check energy to see if pet is tired or has the required energy to do activities
    def check_energy(self):
        if self.energy <= 20:
            print(self.name,"is veryy tired and needs their sleep!!")
        else:
            print(self.name,"is full of energy and is ready for action!")

    # function to make pet do an activity from dictionary
    def random_activity(self):
        choice = input("Choose an activity for",self.name,"to do!!: \n")
        print("1. watch tv")
        print("2. play with toys")
        print("3. run around")
        print("4. explore the garden")
        print("5. jump on the trampoline")

        if choice in activity_options:
            activity_options.get(choice)
            print(self.name,"is bored and is now completing this activity: ",activity_options.get(choice))

            # reset boredom to false after activity
            self.is_bored = False

            # add to list of interactions that pet did certain activity
            self.interactions.append(self.name,"did",activity_options.get(choice))
        else:
            print(self.name,"doesn't understand that activity")

    # change behaviour if pet is well cared for :)
    def change_behavior(self):
        if self.hunger == 100 and self.energy == 100:
            print(self.name,"is happy and well cared for <3, awesome job!!")
        elif self.hunger > 70 or self.energy < 30:
            print(self.name,"seems a lil upset :(, maybe it's feeding time or bedtime...")
        else:
            print(self.name,"is doing ok but could be happier")

# main loop
def start_interaction():
    print("Welcome to Pet World!!! :3")
    
    # create a pet object with a name and birth date
    pet_name = input("What would you like to name your pet?: \n")
    birth_year = int(input("Enter the birth year of your pet (in format 'yyyy' e.g. 2004): \n"))
    birth_month = int(input("Enter the birth month of your pet (in format 'mm' e.g., 9): \n"))
    birth_day = int(input("Enter the birth day of your pet (in format 'dd' e.g. 5): \n"))

    # create a datetime object for birth date
    birthdate = datetime(birth_year, birth_month, birth_day)

    # creates an instance of pet with details provided by user
    pet = Pet(pet_name, birthdate)
    
    # dictionary of menu choices & corresponding functions
    menu_options = {
        "1": pet.feed,
        "2": pet.check_hunger,
        "3": pet.sleep,
        "4": pet.wake_up,
        "5": pet.exercise,
        "6": pet.check_energy,
        "7": pet.get_age,
        "8": lambda: print("Goodbye!")  # exit option
    }

    activity_options = {
        "1": "watch tv",
        "2": "play with toys",
        "3": "run around",
        "4": "explore the garden",
        "5": "jump on the trampoline"
    }
    
    # main loop to interact with the pet
    while True:
        print("\nWhat would you like to do?")
        print("1: Feed pet")
        print("2: Check if pet is hungry")
        print("3: Put pet to sleep")
        print("4: Wake pet up")
        print("5: Exercise pet")
        print("6: Check energy")
        print("7: Get pet's age")
        print("8: Exit")
        
        choice = input("What would you like to do next?: \n")
        
        if choice in menu_options:

            # call function according to choice inputted by user
            menu_options[choice]()
        else:
            print("Invalid choice, please try again.")

# start interaction loop
if __name__ == "__main__":
    start_interaction()