#Print is Your Friend

# the issue here is the "==" sign used to assign word_per_page variable
# "==" sign is only used to compare the values, not assign
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# # investigate using print
# # see if we are right
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# print(f"page number: {pages}")
# print(f"words per page: {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)

# fixed:
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)