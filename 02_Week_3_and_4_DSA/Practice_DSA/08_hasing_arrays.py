# ======================
# Hashing Introduction
# ======================

# Hashing is a data structure technique that helps find a data item directly in an array.

# It allows constant-time access → O(1) complexity in average case.

# Compared to:

# Linear search → O(n)

# Binary search → O(log n) (requires sorted data)

# ✅ Hashing is faster and more efficient than linear or binary search for lookup operations.

# ======================
# Hashing Collision
# ======================

# A collision occurs when two items are assigned to the same place in the hash table.

# In other words, after applying the hash function, an item’s calculated index is already occupied by another item.

# Example with animals:

# animals = ["cat", "dog", "rat"]
# size = 3

# # Simple hash: sum of ASCII values % size
# # "cat" → 0
# # "dog" → 2
# # "rat" → 0  (collision with "cat")


# Visual: Hash Table

# Index	Elements
# 0	cat, rat
# 1	None
# 2	dog
# ======================
# Collision Resolution
# ======================

# Closed Addressing (Chaining)

# Each index stores a linked list or tree of elements.

# New items are added to the list at the collided index.

# Open Addressing

# Find another free slot in the table.

# Methods include:

# Linear Probing → check next slots sequentially

# Quadratic Probing → check slots using quadratic function

# Double Hashing → use another hash function to find next slot

# ======================
# Load Factor & Table Resizing
# ======================

# Load Factor (α) =

# 𝛼
# =
# Number of elements
# Size of hash table
# α=
# Size of hash table
# Number of elements
# 	​


# Tells us how full the hash table is.

# High load factor (>0.7) → more collisions → slower access in open addressing.

# 🔹 When to Increase the Size of the Array

# In open addressing, if the table gets too full (high load factor), we increase the array size and rehash all elements.

# This ensures O(1) average lookup is maintained.

# 🔹 Example

# Original size = 7

# Insert elements → table 80% full → many collisions during linear probing

# Solution: increase size to 14, then rehash all elements → fewer collisions

# 💡 Key Insight:

# Hashing = fast access

# Collisions = natural challenge

# Load factor monitoring & resizing = keeps hash table efficient

