# Software Engineering Task 2 – Object-Oriented Application Project
This README should be updated progressively throughout development and used as evidence of planning, implementation, testing, and evaluation.

## Student Details

| Field | Information |
|---|---|
| Student Name | Lucas Clarke |
| Class | 11 Software Engineering |
| Teacher | A. Pike |
| Due Date | 10.6.26 |

---

# Project Overview

## Project Title
Trade Engine

---

## Problem Definition

### What Problem or Need Does This Software Address?
Stock prices can be unpredictable, but Trade Engine collates data to assist in observing historical trends.

---

## Intended Users
Who is this software designed for?

Examples:
- Commerce and Economics Students interested in observing market trends.

---

## Purpose of the Program
Explain what the program is intended to do.
To predict fictional market trends, and subsequently when to buy, sell, or hold stocks.

---

# Software Development Planning

## Software Development Life Cycle (SDLC)

Briefly explain how your project followed these stages:

| SDLC Stage | Notes |
|---|---|
| Problem Identification | For economic and commerce students, who want to understand market trends, Trade Engine is a simple utility that presents historical data in a readable manner. |
| Requirements Specification | A user must be able to buy and sell stocks of a company, these stocks must be added or deducted from their stock portfolio, and the appropriate funds added or subtracted from their bank accounts. The prices of these stocks must adapt in some way dynamically.|
| Design | There will be a portfolio class that has the buy sell and evaluate methods. A list of set companies will be specified with stock prices that vary. Each user will be able to purchase and sell stocks, and this will be tracked in their own personal stock list, along with their account balance. |
| Development | The project has shifted from using command line arguments to determine the behaviour of the program, to running in a continuous loop which prompts the user before each action is taken. An account class has been added, which shares methods that are common to any user of the system.|
| Testing and Debugging | When implementing the different trading strategies, the output of the program needed to be tested to ensure that the strategy was working as intended. For example when the 'random' strategy was implemented I had to ensure that the output of the choices was "random". This did not seem to be the case in one instance, where after specifying any company with the threshold strategy, the program chose to hold the VCTR stock three times in a row, however it did choose another option the fourth time. |
| Evaluation | |

---

# Requirements

## Functional Requirements
What must the program be able to do?

### Requirements List
- [ Take an action (buy, sell, or evaluate ]
- [ Take a company for that action to apply ]
- [ Take a quantity of purchased or sold stock ]
- [ Receive an updated stock list after each action occurs ]
- [ The program should run continuously and allow for multiple actions to occur ]

---

## Non-Functional Requirements
What qualities should the program demonstrate?

Examples:
- Easy to use
- Readable code
- Reliable output
- Fast response time

### Requirements List
- [ The program must work every time it is run and complete all functional requirements consistently ]
- [ The program should have a fast response time after each action is ran ]
- [ Multiple users each with their own accounts and stock lists]

---

# Object-Oriented Design

## Classes and Responsibilities

| Class Name        | Purpose / Responsibility                                                                                           |
| Account           | Holds methods and variables that apply to a user                                                                   |
| Portfolio         | Contains the buy, sell and evaluate methods that is called by each user                                            |
| TradingStrategy   | Defines the check_signal() and check_strategy() methods, where check_strategy() then runs the appropriate subclass |
| RandomStrategy    | Reimplements the check_signal() method to choose between buying, selling, or holding                               |
| ThresholdStrategy | Chooses whether to buy, sell, or hold, based up the value of the stock of any listed company                       |

---

## Objects
List examples of objects that will be created from your classes.

| Object | Class |
|---|---|
| | |
| | |

---

## OOP Principles Used

### Encapsulation
How does your program group data and behaviour together?

---

### Abstraction
How does your program simplify complex processes for the user?
Logic that is frequent throughout different parts of the program are grouped into methods that make it easier to call. These methods are then grouped into classes where need be, to group common tasks together.

---

### Inheritance (If Used)
Describe any parent and child class relationships.
The TradingStrategy class outlines logic based upon which strategy is called by the user. This then calls either the RandomStrategy or ThresholdStrategy subclasses.

---

### Polymorphism (If Used)
Describe any methods or behaviours that work differently in different classes.
In the RandomStrategy class, the check_signal() method randomly selects between the choices of buy, sell, and hold. Whereas in the ThresholdStrategy class, buy is selected if the value of the selected stock is less than 25, hold is selected if the value is between 25 and 50, and sell is chosen if the value is above 50.

---

# Algorithm Planning

## Main Program Flow

Describe the major steps of your program.

1. Ask who the user is
2. Ask for an action (either buy, sell, evaluate, strategy, or exit)
3. Ask for a company the action is going to apply to
4. If the action was not "strategy" then ask for an amount, then complete the action
5. If the action was "strategy" ask for which strategy, then execute the code for that strategy
6. Repeat until the user enters "exit" as the action

---

## Pseudocode / Algorithms

### Example Algorithm

```text
START
INPUT user choice
IF choice is valid THEN
    process choice
ELSE
    display error
END IF
STOP
```

Add your own algorithms below.

---

# Implementation Progress

## Features Completed

- [ Buy and sell methods implemented ]
- [ Account class created ]
- [ Random and threshold strategies integrated ]
- [ Finished making the program run continuously until the user asks to exit ]

---

## Features Partially Completed

- [ Stub made for evaluate method, but need to implement fully ]

---

## Features Planned but Not Completed

- [ Change the price of each stock dynamically based on some external factor ]

---

# Testing and Evaluation

Testing and evaluation are essential parts of software engineering.  
This section documents how the project was tested, debugged and evaluated throughout development.

---

## Testing Overview

### Purpose of Testing

Explain why testing is important for your project.

Consider:
- correctness
- reliability
- user experience
- error prevention

---

## Testing Strategy

### Types of Testing Used

Tick the testing methods used during development.

- [ ] Normal / Typical Testing
- [ ] Boundary Testing
- [ ] Invalid Input Testing
- [ ] User Testing
- [ ] Method / Class Testing
- [ ] Integration Testing

---

### Testing Process

Describe how you tested your program during development.

Examples:
- Testing after each feature was added
- checking outputs against expected results
- debugging methods separately before integration

---

## Test Cases

### Functional Testing

| Test Case | Input / Action | Expected Result | Actual Result | Pass / Fail |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

### Boundary and Invalid Data Testing

| Test Case | Input | Why This Test Was Important | Result |
|---|---|---|---|
| Boundary Test | | | |
| Invalid Test | | | |
| Edge Case | | | |

---

## Debugging Log

Record problems found during testing and how they were fixed.

| Issue Found | Cause | Solution Applied |
|---|---|---|
| | | |
| | | |
| | | |

---

# Code Evaluation

## Functionality

How effectively does your program meet the intended requirements?

Consider:
- features implemented
- correctness of outputs
- reliability of the program

---

## Object-Oriented Design

Evaluate the effectiveness of your object-oriented design.

Consider:
- class structure
- organisation of methods
- encapsulation
- maintainability

---

## Readability and Code Quality

Evaluate the readability of your code.

Consider:
- naming conventions
- comments
- formatting
- organisation

---

## Testing Effectiveness

How effective was your testing process?

Consider:
- whether errors were identified
- whether bugs were fixed successfully
- whether important cases were tested

---

# Reflection

## Challenges Encountered

Describe difficulties experienced during development and testing.

---

## What You Learned

Explain what skills or concepts you improved during this task.

---

## Future Improvements

If you continued this project, what would you improve or add?

---

# Final Statement

Summarise the overall success of your project.

---
