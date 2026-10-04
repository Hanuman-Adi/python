# Challenge: print  3 -> 2 -> 1 -> Liftoff!  on a single line

# Version 1: sep
print(3, 2, 1, "Liftoff!", sep=" -> ")

# Version 2: end
print("3 ->", end=" ")
print("2 ->", end=" ")
print("1 ->", end=" ")
print("Liftoff!")
