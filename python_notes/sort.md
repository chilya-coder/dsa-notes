# Sorting in Python

1. By start

```python
some_list.sort()
```

2. Reverse lambda

```python
some_list.sort(key=lambda x:x[1])
```

3. Reverse In-place

```python
nums.sort(reverse=True)
```

4. Reverse Returns new list
```python
sorted_nums = sorted(nums, reverse=True)
```