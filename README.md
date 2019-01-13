# rusyllab
Simple Python package for breaking Russian words into syllables.

## Installation

Type in console:

```
pip install git+https://github.com/Koziev/rusyllab
```

## API

Function *split_word* splits a word aand returns a list of syllables. 

Function *split_words* processes the list of words and return the list of syllables and spaces for word separation.

## Usage


Example:

```
import rusyllab

sx = rusyllab.split_words(u"Голодная кошка ловит мышку".split())
print('|'.join(sx))
```

Result:

```
Го|лод|на|я| |кош|ка| |ло|вит| |мыш|ку
```
