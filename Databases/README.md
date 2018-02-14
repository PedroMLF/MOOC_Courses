#Database Courses

Implementations of the courses on [Databases](https://lagunita.stanford.edu/courses/Home/Databases/Engineering/about) by Jennifer Widom, hosted on Stanford Lagunita.

Mini-courses:

- Introduction and Relational Databases
- XML Data (ongoing)

---

### Mini-course 1 - Introduction and Relational Databases

- Characterized by being Massive, Persistent, Safe, Multi-user, Convenient (physical data independence and high level query languages), Efficient (perfomance) and Reliable (must be acessible 99.999% of the time).

**The relational model:**

- A database is a set of named _relations_ (or tables).

- Each relation has a set of nammed _attributes_ (or columens).

- Each _tuple_ (or row) has a value for each attribute.

- Each _attribute_ has a type (or domain).

- _Schema_ is the description of the strucutre of relations in the database.

- _Instance_ refers to the contents at some point in time.

- _NULL_ is used for undefined values. These values don't appear even if queried by a OR that satisfies all conditions for a certain attribute.

- _Key_ is an attribute whose value is unique in each tuple (row). May occur in set of attributes.

- Example of how to create tables:

```sql

Create Table Student(ID, name, GPA, photo)

Create Table College
    (name string, state char(2), enrollment integer)

```

**Querying relational databases:**

- Steps to create and use relational database:
    - Design schema, creating using DDL;
    - Load the inital data;
    - Repeatedly query and modify the database;

- Ad-hoc queries mean that the queries may be made as we think of them and do not require extensive coding.

- Queries easy to pose are not necessarily easy to perfom efficiently.

- The query language may have _closure_, when you get back the same type of the object that you query. It has _compositionality_ when we may query on top of the answers of previous queries.

- Two query languages examples: Relational Algebra (formal) and SQL (implemented language).

---

### Mini-course 2 - XML Data

- Extensible markup language.

- Tags describe the content.

- Basic constructs
    - Tagged elements
    - Attributes
    - Text

|                |    Relational    |          XML         |
|:--------------:|:----------------:|:--------------------:|
|    Structure   |      Tables      |  Hierarchical (Tree) |
|     Schema     | Fixed in advance |       Flexible       |
|     Queries    |      Simple      |        Tricky        |
|    Ordering    |       None       |        Implied       |
| Implementation |      Native      | Add-on to Relational |

- "Well" formed XML
    - Single root element
    - Matched tags, proper nesting
    - Unique atributes within elements

- A XML parser is responsible to check if a given XML document is well-formed.

- It may be displayed by being translated to HTML by languages as CSS (cascading style sheet language) oor XSL (extensible style sheet language).

- A XML document is sent to CSS/XSL interpreter (with rules) which output an HTML doc.

**DTDs, IDs & IDREFs:**

- Document Type Descriptor (DTD).

- Now the XML parser also receives a DTD or XSD to verify that the XML document also complies with the content specific specifications.

- DTD:
    - Grammar like language that specifies elements, attributes, nesting, ordering and number of occurrences
    - Allow IDs or IDREFs

- Pros of using DTD:
    - Programs can assume structure
    - CSS/XSL can assume structure
    - Allow to define specifications
    - Makes documentation of data easier

- Cons of using DTD:
    - Less flexibility to change format, etc.
    - If data is irregular it may be hard to specify structure

**XML Schema:**

_continue_
