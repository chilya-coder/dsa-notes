# List notes

---

## Traversing

1. Traverse through list

```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```

2. Traverse through indexes

```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```

3. Traverse through index and value

```python
thislist = ["apple", "banana", "cherry"]
for idx, idx_word in enumerate(thislist):
  print(idx, idx_word)
```

4. Traverse reverse

```python
for i in range(len(nums) - 1, -1, -1): #start, stop, step
    print(i, nums[i])

for x in reversed(nums):
    print(x)
```

5. Slicing

```python
nums = [0, 1, 2, 3, 4, 5]

nums[1:4]  #[1, 2, 3]
nums[::-1]  # [5, 4, 3, 2, 1, 0]
nums[::2]   # [0, 2, 4]

```

6. Traverse two lists together

```python
for item1, item2 in zip(list1, list2):
    print(item1, item2)
```

## List Comprehension

E.g. tuple unpacking

```python
return [num for freq, num in heap]
```

## Append vs Extend

Useful for [Relative sorted array problem](https://neetcode.io/problems/relative-sort-array/question)

```python
res = []
# 1. append
res.append([2, 2, 2])
# res: [[2, 2, 2]]

# 2. extend
res = []
res.extend([2, 2, 2])
# res: [2, 2, 2]

```