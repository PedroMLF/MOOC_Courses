#### In-Video Quiz

**Q1:** You're creating a database to contain information about university records: students, courses, grades, etc. Should you use the relational model or XML?

> Relational

**Q2:** You're creating a database to contain information for a university web site: news, academic announcements, admissions, events, research, etc. Should you use the relational model or XML?

> XML

**Q3:** You're creating a database to contain information about family trees (ancestry). Should you use the relational model or XML?

> Either one is appropriate.

---

#### XML Quiz

**Q1:** We're interested in well-formed XML that satisfies the following conditions:
- It has a root element "tasklist"
- The root element has 3 "task" subelements
- Each of the "task" subelements has an attribute named "name"
- The values of the "name" attributes for the 3 tasks are "eat", "drink", and "play"

Select, from the choices below, the well-formed XML that meets the above requirements. 

Answer:

 ```
 <tasklist>
  <task name="eat"></task>
  <task name="drink"></task>
  <task name="play"></task>
 </tasklist>```

**Q2:** An XML document contains the following portion: 

```<INFO>
         <ADDR>101 Maple St.</ADDR>
         <PHONE>555-1212</PHONE>
         <PHONE>555-4567</PHONE>
     </INFO>```

Which of the following could be the INFO element specification in a DTD that the document matches?

> <!ELEMENT INFO (ADDR?,PHONE+)>

**Q3:** An XML document contains the following portion: 

```<EMP name = "Kermit">
    <ADDR>123 Sesame St.</ADDR>
    <PHONE type = "cell">555-1212</PHONE>
    </EMP>
```

 Which of the following could NOT be part of a DTD that the document matches? Note that there can be multiple ATTLIST declarations for a single element type; do not assume the only attributes allowed for an element type are the ones shown in the answer choice.

Answer:

<!ATTLIST EMP ssNo CDATA #REQUIRED> 

**Q4:** Here is a DTD: 
```<!DOCTYPE A [
    <!ELEMENT A (B+, C)>
    <!ELEMENT B (#PCDATA)>
    <!ELEMENT C (B?, D)>
    <!ELEMENT D (#PCDATA)>
]>```

Which of the following sequences of opening and closing tags matches this DTD? Note: In actual XML, opening and closing tags would be enclosed in angle brackets, and some elements might have text subelements. This quiz focuses on the element sequencing and interleaving specified by the DTD. 

> A B /B B /B C D /D /C /A

**Q5:**  Here is an XML DTD: 
```<!DOCTYPE meal [
    <!ELEMENT meal (person*,food*,eats*)>
    <!ELEMENT person EMPTY>
    <!ELEMENT food EMPTY>
    <!ELEMENT eats EMPTY>
    <!ATTLIST person name ID #REQUIRED>
    <!ATTLIST food name ID #REQUIRED>
    <!ATTLIST eats diner IDREF #REQUIRED dish IDREF #REQUIRED>
]>```

Which of the following documents match the DTD? 

Answer:

```<meal>
 <person name="Alice"/>
 <person name="Bob"/>
 <person name="Carol"/>
 <person name="Dave"/>
 <food name="salad"/>
 <food name="turkey"/>
 <food name="sandwich"/>
 <eats diner="Alice" dish="turkey"/>
 <eats diner="Bob" dish="salad"/>
 <eats diner="turkey" dish="Dave"/>
</meal>```

**Q6:** Study the following XML Schema specification: 
```<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="person">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="fname" type="xs:string"/>
        <xs:element name="initial" type="xs:string"
            minOccurs="0"/>
        <xs:element name="lname" type="xs:string"/>
        <xs:element name="address" type="xs:string"
            maxOccurs="2"/>
        <xs:choice>
          <xs:element name="major" type="xs:string"/>
          <xs:element name="minor" type="xs:string"
              minOccurs="2" maxOccurs="2"/>
        </xs:choice>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

Select, from the choices below, the XML that is valid according to the XML Schema specification above.

Answer:

```<person>
    <fname>John</fname>
    <initial>Q</initial>
    <lname>Public</lname>
    <address>123 Public Avenue, Seattle, WA 98001</address>
    <minor>Psychology</minor>
    <minor>History</minor>
  </person>```


---

#### DTD Exercises

**Q1:**

For [data](https://prod-c2g.s3.amazonaws.com/db/Winter2013/files/courses-noID.xml):

```<!ELEMENT Course_Catalog (Department*)>

<!ELEMENT Department (Title, Chair, Course+)>
<!ATTLIST Department Code ID #REQUIRED>

<!ELEMENT Title (#PCDATA)>

<!ELEMENT Chair (Professor)>

<!ELEMENT Course (Title?, Description?, Instructors?, Prerequisites?)>
<!ATTLIST Course Number ID #REQUIRED
                 Enrollment CDATA #IMPLIED>

<!ELEMENT Description (#PCDATA)>

<!ELEMENT Instructors (Lecturer | Professor)+>

<!ELEMENT Prerequisites (Prereq)+>

<!ELEMENT Lecturer (First_Name, Middle_Initial?, Last_Name)>

<!ELEMENT First_Name (#PCDATA)>
<!ELEMENT Middle_Initial (#PCDATA)>
<!ELEMENT Last_Name (#PCDATA)>

<!ELEMENT Prereq (#PCDATA)>

<!ELEMENT Professor (First_Name, Middle_Initial?, Last_Name)>```

