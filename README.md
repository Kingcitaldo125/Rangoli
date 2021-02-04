# Rangoli

[Rangoli](https://en.wikipedia.org/wiki/Rangoli) ASCII art in Python.
A Rangoli is an indian art form that originated from southern India.
This repo will print out a more ASCII and command line friendly version of a Rangoli artwork.
I also have support for printing a diamond to the console window.
More below.

## Usage

### Diamond
There are three different types of command line input that the script can take in.
To run the script, simply type `python diamond.py ` followed by one or more of the options listed below
Each of these options require a certain order.
That order is displayed below:

1. A Size(int) ex. `3`
2. A String of letters to print(str) ex. `A` or `AS` or `ASDF` where each string is a valid ASCII string
3. A boolean of whether or not to override the existing letters in place of random ASCII(bool) ex. `True`

### Rangoli

To run the script, simply type `python Randgoli.py`.

## Output

### Diamond

Running with `python diamond.py 9 ASD` produces:

```
        A
       ASD
      ASDAS
     ASDASDA
    ASDASDASD
   ASDASDASDAS
  ASDASDASDASDA
 ASDASDASDASDASD
ASDASDASDASDASDAS
 ASDASDASDASDASD
  ASDASDASDASDA
   ASDASDASDAS
    ASDASDASD
     ASDASDA
      ASDAS
       ASD
        A
```

while running with `python diamond.py 9 ASD True` produces something like:

```
        (
       ###
      OOOOO
     '''''''
    /////////
   ]]]]]]]]]]]
  hhhhhhhhhhhhh
 iiiiiiiiiiiiiii
YYYYYYYYYYYYYYYYY
 ]]]]]]]]]]]]]]]
  yyyyyyyyyyyyy
   ggggggggggg
    +++++++++
     3333333
      JJJJJ
       (((
        '
```

### Rangoli

Running normally, with ``, produces:

```
cols 9
rows 5
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
```
