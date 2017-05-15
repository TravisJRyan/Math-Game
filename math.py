"""Program 3 Programmed by Travis Ryan on April 11, 2016
Time Finished: 12:13 PM
CS 170 Section 2
Program generates math problems for children and tracks their progress as
they answer the problems."""

from graphics import *
from random import *
from time import *

def CreateWindow():
    window = GraphWin("Math Program",600,600)
    window.setBackground(color_rgb(96,196,230))
    return window

def GenerateNumber():
    return randrange(1,31)

def GenerateOperation():
    return randrange(1,5)

def VerifyOperation(num1,num2,operation):
    if operation == 1:
        answer = num1 + num2
    elif operation == 2:
        answer = num1 - num2
    elif operation == 3:
        answer = num1 * num2
    elif operation == 4:
        answer = num1 / num2
    if answer < 0 or answer > 100 or answer % 1 != 0:
        return False
    else:
        return True

def DisplayProblem(num1, num2, operation, window):
    T1 = Text( Point(200, 200), str(num1))
    T1.setSize(35)
    T2 = Text( Point(330, 200), (str(num2)+"  =  "))
    T2.setSize(35)
    T1.draw(window)
    T2.draw(window)
    if operation == 1:
        T3 = Text(Point(250, 200), "+")
        rightanswer = num1+num2
    elif operation == 2:
        T3 = Text(Point(250, 200), "-")
        rightanswer = num1-num2
    elif operation == 3:
        T3 = Text(Point(250, 200), "*")
        rightanswer = num1*num2
    elif operation == 4:
        T3 = Text(Point(250, 200), "/")
        rightanswer = num1/num2
    T3.setSize(35)
    T3.draw(window)
    entry1 = Entry(Point(400,200), 2)
    entry1.setSize(30)
    entry1.draw(window)
    window.getMouse()
    answer = entry1.getText()
    T1.undraw()
    T2.undraw()
    T3.undraw()
    entry1.undraw()
    circle1 = Circle( (Point(300,350)), 150)
    if answer == str(int(rightanswer)):
        circle1.setFill("green")
        circle1.draw(window)
        T6 = Text(Point(300, 350), "Correct!")
        T6.setSize(30)
        T6.draw(window)
        window.getMouse()
        circle1.undraw()
        T6.undraw()
        return 1
    else:
        circle1.setFill("red")
        circle1.draw(window)
        T7 = Text(Point(300, 350), "Wrong Answer!")
        T7.setSize(30)
        T7.draw(window)
        T8 = Text(Point(300,395), ("The correct answer was "+str(int(rightanswer))))
        T8.draw(window)
        window.getMouse()
        circle1.undraw()
        T7.undraw()
        T8.undraw()
        return 0

def DisplayStatistic(correct, window):
    percent = 100 * (correct/15)
    percent = int(percent)
    resultText = Text( (Point(300,300)), ("You got "+str(correct)+" problems correct out of 15!"))
    resultText.setSize(20)
    percentText = Text( (Point(300,350)), ("That's "+str(percent)+" percent!"))
    percentText.setSize(15)
    percentText.draw(window)
    resultText.draw(window)

def DisplayWindow(window):
    T4 = Text( Point(300, 50), "Answer the problems!")
    T4.setSize(35)
    T4.draw(window)
    T5 = Text( Point(300, 100), "Click to continue.")
    T5.setSize(20)
    T5.draw(window)
    correct = 0
    for i in range(15):
        T9 = Text( Point(100, 550), ("Problem "+str(i+1)) )
        T9.setSize(20)
        T9.draw(window)
        condition = False
        operationType = GenerateOperation()
        while condition == False:
            number1 = GenerateNumber()
            number2 = GenerateNumber()
            if VerifyOperation(number1, number2, operationType) == True:
                condition = True
        correct += DisplayProblem(number1, number2, operationType, window)
        T9.undraw()
    T4.undraw()
    T5.undraw()
    DisplayStatistic(correct, window)

def main():
    window = CreateWindow()
    DisplayWindow(window)
    
    window.getMouse()
    window.close()


main()

