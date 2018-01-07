set1 = set(["a","b","c","d","e"])
set2 = set(["d","c","e","x","z"])

in_both = set1 & set2
in_set1_only = set1 - set2

print in_both
print in_set1_only
