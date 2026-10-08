# FFMI Calculator

A basic Python program that calculates **Fat-Free Mass Index (FFMI)** using a person's weight, body fat percentage, and height.

## Description

The program asks the user to enter:

* Weight in pounds
* Body fat percentage
* Height in inches

It then converts the weight and height to metric units, calculates lean body mass, and uses that value to calculate FFMI.

### FFMI Formula

The program calculates lean body mass using:

```text
Lean Mass = Weight × (1 - Body Fat Percentage / 100)
```

It then calculates FFMI using:

```text
FFMI = Lean Mass (kg) / Height (m)²
```

## How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python script.py
```

The program will prompt you for your information:

```text
Hello
Enter your weight in pounds: 180
Enter your body fat percentage: 15
Enter your height in inches: 70
```

The program will then display your calculated FFMI.

## Example

For a person who weighs 180 pounds, has 15% body fat, and is 70 inches tall, the program calculates an FFMI of approximately:

```text
21.97
```

## Functions

### `ffmiCalculator()`

Takes three inputs:

* `weight` — weight in pounds
* `bodyFat` — body fat percentage
* `height` — height in inches

The function converts the measurements, calculates lean mass, calculates FFMI, and returns the FFMI value.

### `main()`

Handles the user interaction by collecting the user's weight, body fat percentage, and height. It then calls `ffmiCalculator()` and prints the result.

## Requirements

* Python 3.x
