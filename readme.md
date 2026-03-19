# kisspy - Simple Python Scripting Helpers

This is a collection of simple helper methods and classes that I have found useful for data processing

## Usage

The package offers simple methods that I found I was reusing frequently.

### Converters

Numeric Converter

````python
    from kisspy import toNumeric, returnTxt,raiseValExc

    def rtnMsg(*args):
        return "Can't Convert '{}' To A Number".format(args[0])

    alphaVal = "55"
    numVal = toNumeric(alphaVal)
    print(isinstance(numVal, int))

    alphaVal = "88 ft"
    numVal = toNumeric(alphaVal)
    print(numVal)

    numVal = toNumeric(alphaVal, onFail=returnTxt)
    print(numVal)

    numVal = toNumeric(alphaVal, onFail=rtnMsg)
    print(numVal)

    numVal = toNumeric(alphaVal, onFail=raiseValExc)

>>  True
>>  None
>>  88 ft
>>  Can't Convert '88 ft' To A Number
>>  Traceback (most recent call last):
>>  File "C:\Files\code\python\projects\kisspy\examples\converters.py", line 26, in <module>
>>      numVal = toNumeric(alphaVal, onFail=raiseValExc)
>>  File "C:\Files\code\python\projects\kisspy\kisspy\converters\numericConverter.py", line 32, in toNumeric
>>      return onFail(val,verr)
>>  File "C:\Files\code\python\projects\kisspy\kisspy\converters\numericConverter.py", line 5, in raiseValExc
>>      raise args[1]
>>  File "C:\Files\code\python\projects\kisspy\kisspy\converters\numericConverter.py", line 27, in toNumeric
>>      val = float(val)
>>  ValueError: could not convert string to float: '88 ft'
>>  The Value '88 ft' Could Not Be Converted To A Numeric Value
````

Spreadsheet Converters

````python
    from kisspy.converters.excelHelpers import fromExcelCol, toExcelCol

    col = "C"
    print(fromExcelCol(col))

    col = "AF"
    print(fromExcelCol(col))

    num = 2
    print(toExcelCol(num))

    num = 33
    print(toExcelCol(num))

>>  3
>>  32
>>  B
>>  AG
````

The elements in decorators and metaclasses modules speak for themselves.

There are a number of Python "extensions" that do stuff you would have wanted anyways:

Unique Appending To Lists:

````python
    from kisspy import appendUnique

    vl = [2, 4, 6, 8]
    if appendUnique(vl, 4):
        print("Added 4 Again: {}".format(vl))

    if appendUnique(vl, 10):
        print("Added 10: {}".format(vl))

>>  Added 10: [2, 4, 6, 8, 10]
````

Asserting One Record: Returns the one record, with options:
````python
    from kisspy import assertOne
    from kisspy.exceptions import TooManyRecordsException, ZeroRecordsException


    def thrwZeroRecordsEx(*args, **kwargs):
        raise ZeroRecordsException()


    vl = [2, 4, 6, 8]
    print(assertOne([]))
    print(assertOne([44]))

    try:
        oneValue = assertOne(vl)
    except TooManyRecordsException as err:
        print(err.toStrWithTyp())

    try:
        print(assertOne([], onZeroRcds=thrwZeroRecordsEx))
    except ZeroRecordsException as err:
        print(err.toStrWithTyp())

>>  None
>>  44
>>  TooManyRecordsException: 4 Records Returned, 1 Were Expected
>>  ZeroRecordsException: Zero (0) Records Returned, > 0 Were Expected
````

Nested Dicts:

````python
    from kisspy import setValueOfPath, getValueOfPath

    vd = {"animals": {"dog": {"whippet": "fast", "lab": "slower"}}}

    wv = getValueOfPath(vd, keyPath="animals/dog/lab")
    print(wv)

    cv = getValueOfPath(vd, keyPath="animals/cat/tabby")
    print(cv)

    setValueOfPath(vd, "animals/dog/golden", "silly")
    print(vd)

>>  slower
>>  None
>>  {'animals': {'dog': {'whippet': 'fast', 'lab': 'slower', 'golden': 'silly'}}}
````

## Installation

### Using In Projects

Installation:

````bash
    pip install kisspy-python
````

### Cloning For Development

<p>Set up a virtual environment. Once an environment is set up, run the command below to:

* validate the environment variable
* activate the environment (if not already activated) 
* install all of the necessary packages into the local environment

```bash
    pip install -U -r requirements/dev.txt
```

<p>The dev.txt file includes:

* BLACK, a code formatter, see notes at the bottom of this file for details

## Dependancies

This library depends on the following projects:

* unidecode

## Tests

To run tests:

```bash
    python -m unittest discover -s tests/
```

## Code Formatting

Code formatting is done using BLACK. BLACK allows almost no customization to how code is formatted with the exception of line length, which has been set to 119 characters.

Use the following to bulk format files:

````bash
    black . -l 144
````

## Creating A New Release

Please do the following when making a new release, most are documented above:

1. Run tests
1. Code format
1. Be sure to update the change log and _metadata.json with version and notes
1. git add, commit, and push changes
1. run the following code to generate a wheel:

````bash
    python -m build
````
