fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]

print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

fruits[1] = "Kiwies"
print(f"\nModified list is: {fruits}")

fruits.append("Watermelon")  
print(f"\nList after adding 'Watermelon': {fruits}")

fruits.remove("Watermelon")  
print(f"List after removing 'Watermelon': {fruits}")

length = len(fruits)
print(f"\nLength of the list: {length}")

fruits.sort()  
print(f"\nSorted fruits list (ascending): {fruits}")

fruits.sort(reverse=True) 
print(f"Sorted fruits list (descending): {fruits}")
