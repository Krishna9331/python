print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:')
print('\n newlines and \t tabs.')
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""
print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formaula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formaula(start_point)

#remmember that this is another way of format a string
print("With the starting point of: {}".format(start_point))

#It is just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10
print("We can also do that in this way:")

formaula = secret_formaula(start_point)
#This is an easy way to apply  a list to format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formaula))
