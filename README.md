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
| Evaluation | Trade Engine met its primary objectives by allowing users to manage stock portfolios, account balances, and trading strategies. Testing confirmed that the core functionality worked reliably. Although some planned features, the project successfully demonstrated the use of object-oriented design and fulfilled most requirements.
 |


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
| ------------------|--------------------------------------------------------------------------------------------------------------------|
| Account           | Holds methods and variables that apply to a user                                                                   |
| Portfolio         | Contains the buy, sell and evaluate methods that is called by each user                                            |
| TradingStrategy   | Defines the check_signal() and check_strategy() methods, where check_strategy() then runs the appropriate subclass |
| RandomStrategy    | Reimplements the check_signal() method to choose between buying, selling, or holding                               |
| ThresholdStrategy | Chooses whether to buy, sell, or hold, based up the value of the stock of any listed company                       |

---

## Objects
List examples of objects that will be created from your classes.

| Class | Object |
|---|---|
| Account| User|
| Portfolio | p |
| TradingStrategy | RandomStrategy, ThresholdStrategy
| RandomStrategy | result, Ts
| ThresholdStrategy | result |
---

## OOP Principles Used

### Encapsulation
How does your program group data and behaviour together?
Portofilo tracks data, trading strategy enacts logic based on user input, main while true loop is the public interface that interacts with users.

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
# look at main program flow and just convert to psudo code, and expand upon the main program flow to include what the strategies actually do.
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

 - [ Stock prices fluctuate dynamically, but the fluctuations are randomly generated rather than based on realistic market conditions ]
---

## Features Planned but Not Completed

- [ Change the price of each stock dynamically based on some external factor ]
- [ Save user accounts and portfolios between program runs ]
- [ Use real or simulated market data instead of random price changes ]
- [ Add additional trading strategies ]
- [ Create a graphical user interface ]
- [ Improve error handling and validation for all user inputs ]

---

# Testing and Evaluation

Testing and evaluation are essential parts of software engineering.  
This section documents how the project was tested, debugged and evaluated throughout development.

---

## Testing Overview

### Purpose of Testing

Explain why testing is important for your project.

There are multiple reasons why testing is important for the quality of the project. Without testing the output of the program against the expected output, then there would be no way of
knowing if the program logic is working correctly. This testing must occur multiple times and with varying cases to ensure that the code written is reliable, if the project is only
tested once, then the code may be unreliable. The output must also be clear and readable to ensure that the user can interpret the information outputed.

---

## Testing Strategy

### Types of Testing Used

Tick the testing methods used during development.

- [x] Normal / Typical Testing
- [x] Boundary Testing
- [x] Invalid Input Testing
- [ ] User Testing
- [ ] Method / Class Testing
- [x] Integration Testing

---

### Testing Process

Describe how you tested your program during development.
During development I tested when each new method was introduced to ensure that it's logic behaved correctly. Included in this was the validation of the output of the program to ensure
the right data was affected in each stage of execution.

---

## Test Cases

### Functional Testing

#what inputs is it accepting. (numbers where there should be strings, strings where there should be numbers

| Test Case | Input / Action | Expected Result | Actual Result | Pass / Fail |
|---|---|---|---|---|
| 1 | Name: "Alice" | New user created with 120 account balance | As expected | Pass |
| 2 | Action: "buy", Company: "SNPS", Amount: 10 | 120 balance reduced by 10 × stock price, holdings updated to 50 SNPS | As expected | Pass |
| 3 | Action: "sell", Company: "SNPS", Amount: 5 | around 50 added to balance depending on stock price, holdings reduced to 45 SNPS | As expected | Pass |
| 4 | Action: "evaluate", Company: "HLIX" | Stock evaluation output displayed correctly | As expected | Pass |
| 5 | Action: "strategy", Company: "any", Strategy: "random" | Random strategy chooses buy/sell/hold and updates holdings accordingly | As expected | Pass |

---

### Boundary and Invalid Data Testing

# boundary test buying negative stock
# invalid test ; balnk name
# edge case ; Outline how I making sure that I can only purhcase / sell the amount of stock that is allowed for my acccount balance ; line 159 
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
| No new users could be created | All users were defined in the program explicitly  | The users are now based on user input |
| When purchasing or selling a stock, no amount of money was exchanged | There was no definition of a bank account | A cash balance was implemented, which gets added to or subtracted from when buying or selling a stock |
| The user could not complete more than one operation before the program exited | The actions were accepted through command line arguments | The program now uses the python input() function to get the requested action from the user |

---

# Code Evaluation

## Functionality

How effectively does your program meet the intended requirements?

The program allows users to buy and sell stocks of a variety of companies. This adds or removes the stock from their stock list, and also adds and deducts from the users cash balance. The value of stocks fluctuate to imitate a real stock market, as well as when a user buys and sells a stock. The program accurately displays the information of the stock that the user holds, and the stock the user can purchase. Each operation behaves the same way each time it is ran regardless of which stock is selected.

---

## Object-Oriented Design

Evaluate the effectiveness of your object-oriented design.

Trade Engine effectively demonstrates object-oriented principles:
Classes are separated by their function where Account handles user funds and holdings, Portfolio handles transactions, and TradingStrategy with RandomStrategy and ThresholdStrategy subclasses handle decision-making logic.
Data and it's related methods are grouped inside of classes. User balances and holdings are encapsulated Account, trading actions in Portfolio.
RandomStrategy and ThresholdStrategy inherit from the abstract base TradingStrategy, and reuse the check_strategy method template.
The check_signal method behaves differently depending on the strategy class, demonstrating runtime polymorphism.
Methods are modular and logically organized, making the code easier to extend (e.g., adding new strategies).

---

## Readability and Code Quality

The code is for the most part, readable and understandable:
Class names are clear and descriptive (Account, Portfolio, RandomStrategy), but some variable names could be improved (such as the similarity between stock_price and stock_value).
There are a few useful inline comments explaining complex logic like price adjustments during buy/sell operations.
Code is indented and organised consistently, though there are some long methods (like buy and sell) that could be broken into smaller functions for clarity.
The code follows logical flow, separating classes from the main program loop, making it easier to navigate and debug.

---

## Testing Effectiveness

How effective was your testing process?

The testing process is reasonable but could be improved:

Testing caught issues with stock purchase limits, cash balance updates, and the creation of users.
Bugs such as inability to create new users and missing fund adjustments were successfully resolved.
Functional and boundary testing were considered, but more systematic edge case testing could increase consumer confidence.
Classes were tested together to ensure the program logic works correctly, such as Portfolio methods affecting Account balances accurately.

---

# Reflection

## Challenges Encountered

Describe difficulties experienced during development and testing.

During development and testing, several challenges arose:
Implementing fluctuating stock prices required careful handling to ensure purchases and sales correctly updated both user holdings and stock values.
Ensuring RandomStrategy and ThresholdStrategy worked correctly with Portfolio and Account methods needed testing and debugging, particularly for edge cases like insufficient funds or attempting to sell more stock than owned.
Handling unexpected or invalid inputs (like non-numeric amounts or nonexistent company names) was challenging.
Some methods, like buy and sell, became long and complex, making them harder to read and adapt.

---

## What You Learned

Explain what skills or concepts you improved during this task.

I Implemented classes, inheritance, polymorphism, and encapsulation effectively to structure the program logically, which are all components of Object Oriented Programming.
I also learned to translate real-world actions (buy/sell stocks) into program logic, and to implement different trading strategies.
My ability in testing for functional correctness, boundary cases, and error handling, has also improved over the course of this project.
Throughout the development of Trade Engine, as it is much more of a complex project than what I have made in the past, I have had to break complex methods into smaller, manageable functions and documenting convoluted logic with comments.

---

## Future Improvements

If you continued this project, what would you improve or add?

If continuing the project I could make the following enhancements:

I could implement more sophisticated algorithms for stock price changes that better reflect real markets.
Trading strategies of greater complexity and realism beyond random and threshold-based logic, could be introduced.
Adding stricter input handling and improving the amount of error messages help to reduce invalid user actions.
I could also store user accounts and holdings in a file or database to retain their data between sessions.

---

# Final Statement

Summarise the overall success of your project.

Trade Engine successfully allows multiple users to buy and sell stocks, maintains cash balances and stock holdings, and implements trading strategies using a clear object-oriented design.
Core functionality works reliably, and testing helped identify and fix key issues.
The project met its main objectives and provided valuable experience in OOP, program design, and debugging, with opportunities for future enhancements such as improved input validation and persistent storage.

---
