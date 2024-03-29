from Clean Code A Handbook of Agile Software Craftsmanship,
Robert C. Martin

## names

leave the camp ground cleaner than you found it

intention-revealing names - what is in the list? significance of values?

avoid container type in names

class -> nouns , methods -> verbs

avoid : xyz_controller...handler |
xyz_controller...definer | useless for name completion
xyz_controller...storage |

pronounceable names

not l, not o (1 or 0)

searchable names (not i, a1, a2, ....)

## functions

assert_equals(expected, actual) -> convention

the less parameters, the better (f(a1, a2, a3...) -> prefer container )

small, do only one thing

if function changes the state of one thing, it must be the owning object:
not change(a), better a.change()

don't repeat, don't duplicate

## comments

they are not maintained

they can be:

- legal
- informative (format (e.g. hh:mm), type, what it returns)
- explanation of intent (attempt to merge...)
- clarification (syntax)
- warning of consequence (long to execute...)
- TODOS
- amplification of importance

not all functions should be commented, prefer good names

do not comment old code, remove it

## formatting

blank line : new concept

no useless comment to separate concepts

variable declaration close to their usage

dependant functions vertically close

not :

var1 int 1 |
var2 int 2 | all attached, otherwise, tend to look at names, not types
a str "1" |  
b bool False |

var1 int 1  
var2 int 2  
a str "1"  
b bool False

## objects and data structures

no getters and setters, expose only public variables

objects : expose behavior and hide data

- hard to add behavior (must be added to all objects)
- easy to add object

data structures : expose data and have no significant behavior

- easy to add behavior
- hard to add data structure (e.g. add an argument to a function when refactoring)

## errors handling

checked exception : can be managed (e.g. wrong input)

unchecked exceptions : need to be logged, stop execution, important...

## test driven development

not write more tests than sufficient to fail

not write more code than sufficient to pass the tests

tests and code written together, tests a few seconds before code

tests must change if code changes

1 assert or 1 concept per test function

FIRST : fast, independant, repeatable, self-validity, timely (just before prod)

## classes

small

SRP : single responsibility principle

name of the class : responsibility it fullfills

1 class, 1 responsibility, 1 reason to change

## systems

separate construction for use

remove details, particularities, location...
not: tokyostockexchange
prefer: stockexchange

## concurrency

keep concurrency-related code separately

limit access to the data that might be shared

## smells and heuristics

encapsulate conditionals
prefer : should_be_deleted(x)
than : if x>0 and ... then...

avoid negative conditional

##

##

##
