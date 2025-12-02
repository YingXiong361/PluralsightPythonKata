# Collections

## Built-in containers data types

1. List: ordered in **sequence**, mutable, random access by index
2. Dictionary: key value pairs. Keys are unique
3. Tuples: ordered, **immutable**
4. Set: unordered, store **unique** objects

### 1. Lists

List operations

![shallow copy of a list](copyOfList.png)

![list comprehensions provide a faster way than loop to create a list plus transformation and filtering ](listComprehensions.png)

![in operator](searchInList.png)

![sort in place](sortList_I.png)

![sort to return a new object](sortList_II.png)

![reverse in place](reverseList.png)

![+ to concatenate 2 list and * operator to repeat an element](listConcatRepeat.png)

![list of list, used to create matrix](nestedList.png)

![string join function](listToString.png)

![max and min](maxMinList.png)

![sum](sumList.png)

![all, any](allAnyList.png)

![unpack elements in the list into variables](listUnpack.png)

![too many values to unpack. # of elements in the list is greater than the number of variables.](listUnPackError.png)

![To fix the too many values error when unpack, use *details，variable position arguments as a placeholder for the rest of elements in the list](fixListUnPackError.png)

![*args have 2 usages: to unpack the iterable objects when invoke a function; to accept variable number of parameters in the definition of a function](variablePositionArguments.png)

**Overwrite the elements in the lists.**

![overwrite elements inside list](overwriteList.png)

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = [number for number in lst if number % 2 == 0]
```

**iterate both the index and the elements using enumerate function.**

```python
for i, number in enumerate([1, 2, 3, 4, 5]):
    print(f"Element at position {i} is {number}")
```

Using list

1\ Prototyping and Education

Lists are excellent for educational purposes and prototyping due to their simplicity and the intuitive way they map to a real-world concept of a sequence.

2\ 10 most recent logs

```python
recent_events = event_logs[-10:]
```

### 2. Dictionary

![what is dictionary: a collection of key value pairs. The keys are unique and associated with values](dictionaryDef.png)

Update elements and merge dictionaries

![when merge dictionary and same key exists, the right most dictionary values will dominate](updateAndMergeDics.png)

Remove elements
![remove key-value in dictionary can use the del keyword or pop method. Pop method can provide default value if key doesn't exist](removeDic.png)

check key existence
![check if key exist in dictionary using in operator](checkKeyInDic.png)

**Dictionary comprehensions using curly bracket.**

![dictionary comprehension](dicComprehension.png)

**shallow copy and deep copy.**

```python
dic = {"name": "python", "age": 32}
copied_dic = dic.copy()

import copy

deeply_copied_dic = copy.deepcopy(dic)
```

**setdefault method.**
![it's similar to GetOrCreate](setdefault_dic.png)

**Sorting dictionaries.**
![sort dictionary](sortDict.png)

![using sorted function to sort dictionary](sortDicUsingSorted.png)

Using dictionary

Since keys are unique so dictionary is optimal for quick look up of information.

![store configuration](storeConfigUsingDict.png)

![function dispatch table, command parser](functionDispatchTable.png)

![use dic as a cache to avoid duplicated calculation. e.g fibonacci recursive solution](memoizationUsingDic.png)

![use dictionary as counter / frequency table. Use dictionary to count and group elements](freqencyTableUsingDict.png)

![kwargs is of type dictionary](keyWordArgumentFuncParameters.png)

![use kwargs to represent html tag's attributes](kwargs.png)

### 3. Tuples

1. ordered sequence, immutable, fixed number of elements
2. create list using brackets `[]` while create tuple use  parenthesis `()` .

![tuple](tuple.png)

### 4. Set

## Improve efficiency with advanced dictionaries

## Using specialized collection classes

## Customizing built-in data types
