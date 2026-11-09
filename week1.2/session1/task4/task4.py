# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both) # {'tomato'}

# Why does the following code diplay five items?

# Combines both sets together (merges any duplicates together)

food = fruit.union(vegetables) 
print(food)

# Add an item to fruit

fruit.add("banana")

# Remove an item from vegetables

vegetables.remove("potato")

# Find and display symmetric difference of the two sets

print(fruit.symmetric_difference(vegetables)) # everything not in the intersection