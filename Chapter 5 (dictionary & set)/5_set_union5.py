s1 = {1,2,3,4}
s2 = {3,45,34,4}

print(s1.union(s2)) # prints all the value from two sets only one time 

print(s1.intersection(s2)) #prints the same value in two sets 

print({1,2}.issubset(s1)) #subset of s1

print(s1.issuperset({1,2})) #superset