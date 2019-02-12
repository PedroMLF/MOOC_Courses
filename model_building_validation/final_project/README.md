## Final Project: Find hacking attempts from network data

#### Project description

The goal of this project is for you to create a program that examines log data of net flow traffic, and produces a score, from 1 to 10, describing the degree to which the logs suggest a brute force attack is taking place on a server. [Source](https://classroom.udacity.com/courses/ud919/lessons/3610088757/concepts/35982786900923#)

#### Data description

Net flow data refers to the following. A flow is a captured conversation between two elements on a computer network. It describes who its from, who its headed to, and attributes of the back-and-forth, such as number of bytes transmitted.

Specifically a flow record has the following format:

source ip-address | destination ip-address | protocol | source port | destination port | # packets | bytes | flags | site | time

[source](https://classroom.udacity.com/courses/ud919/lessons/3610088757/concepts/35982786900923#)

