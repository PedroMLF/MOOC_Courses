# Design-of-Computer-Programs
Implementations of the Udacity course, Design of Computer Programs by Peter Norvig

---

## Keynotes from Lesson 2

### Concepts to keep

* List comprehension
* Generator expression
* Generator function
* Polymorphism 
* Star args
* Regular expressions
* Future imports
* cProfile
* Lambda functions

### Specifics to keep

* is vs ==
* isinstance()
* yield
* maketrans + translate
* eval

### Ideas to keep

* Functions are first class objects 
* Aspect oriented programming:

    Separate this fundamental parts as much as possible on your code:

    * Correct
    * Efficiency
    * Debug

* Law of Diminishing Returns
* Divide and Conquer
* Spliting with regex as a tool
* Time and count calls

---

## Keynotes from Lesson 3

### Concepts to keep

* Decorator
* Memoization
* Try -> except -> finally
* Parsing

### Specifics to keep

* Regex examples:
    * **x\*** matches any length of x's
    * **x?** matches only x or nothing
    * **.** matches everything except nothing
    * **^x** matches anything starting by x
    * **x$** matches anything finishing in x

* update_wrapper
* trace

### Ideas to keep

* Notions of:
    * Language
    * Grammar
    * Compiler vs Interpreter
    * Language as a design tool
* Compiler - pattern gets called with text as argument
* Interpreted - function gets called with pattern and text as arguments
* Induction - Reducing the input while making recursive calls
* While refactoring keep in mind if the change is _backward compatible_ (everything affected by changes still works) and if the change is _internal_ or _external_.

---

## Keynotes from Lesson 4

### Concepts to keep

* Combinatorial complexity

### Specifics to keep

* Doctest
* Frozensets

### Ideas to keep

* Combinatorial optimization -> Search
* Test the code!
* re-use tools -> generalize!
* Do a inventory of everything you will use on your program and choose a way to define it in terms of code

---

## Keynotes from Lesson 5

### Concepts to keep

* None

### Specifics to keep

* namedtuple

### Ideas to keep

* Dependency injection
* Search with uncertainty
* Utility
* Game theory 
* Simulation vs Enumeration
* Be careful with the types of returns in python functions

---

## Keynotes from Lesson 6

### Concepts to keep

* Regression tests

### Specifics to keep

* None

### Ideas to keep

* None

---

Last Commit: 30/September 2017
