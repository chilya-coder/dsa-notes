# Dict notes

---

Get value from dict without ```KeyError```:

```python
dict.get(char,0)
```

Create dict with character counts (from list):

```python
freq_map = Counter(char)
```

If key doesn't exist - set [] value, else return existing value

```python
key_to_words.setdefault(sorted_s, [])
```

However, it's more common to use this to avoid KeyError

```python
test_dict = defaultdict(list)
```
