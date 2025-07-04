'''
🔹 5. Set Operations (Mathematics Style)
i. ✴️ Union (combine sets) ==> a|b
ii. ✴️ Intersection (common items)  ==> a&b
iii. ✴️ Difference (items in a but not in b)   
iv. ✴️ Symmetric Difference 
(items in either, but not both (don't show common values in both set show only uncommon))
'''
#==================Union=====================#
a = {1,2,3}
b = {2,4,5,6}
a_union_b = a | b
print(a_union_b)
print(a)

#==================Intersection===============#
a_intersectio_b = a.intersection(b)
print(a_intersectio_b)

#==================Difference=================#
a_difference_b = a.difference(b) 
print(a_difference_b)

#==================Symmetric Difference=================#
a_SymmetricDifference_b = a.symmetric_difference(b)
print(a_SymmetricDifference_b)


'''🔹 6. Set Comparison
| Method         | Meaning            |
| -------------- | ------------------ |
| `issubset()`   | a ⊆ b              |==> Is one set inside another?
| `issuperset()` | a ⊇ b              |==> Does one set contain another?
| `isdisjoint()` | No common elements |==> Do the sets have nothing in common?
'''



















