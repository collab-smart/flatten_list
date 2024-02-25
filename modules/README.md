# flattenList

## Description

flattenList(nestedList): This method is to be used as an util file for a higher level implementation to flatten an array 
of arbitrarily nested arrays containing some values into a flat array of all the values non-empty.

## Implementation approach

This function flattens  an array of arbitrarily nested arrays containing some values into a flat array of all the values 
non-empty using a recursive approach.

## How to use this

- Argument: A nested list that you are going to flatten
- Returns: A flat array of all the values non-empty

```python
# Examples:

>>> flattenList([['1', 2, [3]], 4])
['1', 2, 3, 4]

>>> flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])
['1', 2, 3, 4, 5]
```