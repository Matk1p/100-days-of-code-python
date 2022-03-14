#RPS as in Rock Paper Scissors

def rps_printer(choice):
    if choice == 0:
        return ("rock " + '''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        ''')
    elif choice == 1:
        return ("paper " + '''
            _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        ''')
    elif choice == 2:
        return ("scissors " + '''
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        ''')