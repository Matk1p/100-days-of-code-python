from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Charmander", "Fire"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Bulbasaur", "Grass"])

# or another way is
another_table = PrettyTable()
another_table.add_column("Pokemon Name", ["Pikachu", "Treecko", "Nidoking"])
another_table.add_column("Type", ["Electric", "Grass", "Posion, Ground"])

# changing the alignment to left aligned
table.align = "l"


print(table)
print(another_table)