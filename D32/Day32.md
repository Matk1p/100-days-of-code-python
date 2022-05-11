# Day 32

Today we made a birthday wisher program where it checks if there is someone's birthday today and will send an automated email, wishing them a birthday message.
Initially, I managed to implement the program based on the required criteria in the [main](D32/birthday-wisher-extrahard-start/main.py) file where the checking of birthdays and sending email is completed,
but I was faced by a blocker - the names do not match the birthdays, when sending email. 

Took a few steps back and watched the solution from the course. Root of the problem is the use of the wrong data structure. 
Problem could have been avoided entirely by using dictionaries instead of lists. 

Had to re-visit the chapter on dictionary comprehension to refresh memory on how to use and apply that concept. 
But followed through with the solution in [new_main](D32/birthday-wisher-extrahard-start/new_main.py) where the solution is found.