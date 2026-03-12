# kisspy - Simple Python Scripting Helpers

This is a collection of simple helper methods and classes that I have found useful for data processing

## Usage

## Installation

### Prerequisites

Add them here

### Using In Projects

Installation:

````bash
    pip install kisspy
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

### Production

Add some stuff here, or leave out if Usage is added

Dependancies
------------
This project uses the following projects:

* none

Tests
-----
To run tests:

```bash
    python -m unittest discover -s tests/
```

Code Formatting
---------------
<p>Code formatting is done using BLACK. BLACK allows almost no customization to how code is formatted with the exception of line length, which has been set to 119 characters.
<p>Use the following to bulk format files:

```bash
    black . -l 119
```

Creating A New Release
----------------------
Please do the following when making a new release, most are documented above:
1. Run tests
1. Code format
1. Be sure to update the change log and _metadata.json with version and notes
1. git add, commit, and push changes
1. Build package by running the following command:

```bash
    python -m build
```
