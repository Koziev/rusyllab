# rusyllab
Simple Python package for breaking Russian words into syllables

## Installation

Type in console:

```
pip install git+https://github.com/Koziev/rusyllab
```

## API

Function *split* splits a word aand returns a list of syllables. 

## Usage


Example:

```
import rusyllab

syllables = split(u"спросил")
print(u"|".join(sx))
```

Result:

```
спро|сил
```
