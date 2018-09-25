## Requirements
* Python 3.6 and up

## Git repository
```
git clone https://github.com/pplanutis/trip-sorter.git 
```

## Content
#### trip-sorter
The very simple usage of bubble sort algorithm, as it was my first thought that using this method will give me expected results.
After couple of tests I've came up with another approach.

Bubble sort algorithm is O(n^2).

#### trip-sorter2
Second approach. 
Since O(n^2) isn't really that good for this task , I've decided to use namedtuples (so it would be a bit different from what's in the bubble approach) and then just use what dicts offer, instead of hiring any real sorting algorithm here.  

This method is O(n).

## Usage
```
$ python trip-sorter.py
$ python trip-sorter2.py
```

## Testing
```
$ python tests.py
```
