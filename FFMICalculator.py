def ffmiCalculator(weight, bodyFat, height):
    weightKG = weight * 0.453592
    heightM = height * 0.0254

    LeanMass = weightKG * (1 - bodyFat / 100)
    ffmi = LeanMass / (heightM ** 2)

    return ffmi

def main():
    print("Hello")
    weight = float(input("Enter your weight in pounds: "))
    bodyFat = float(input("Enter your body fat percentage: "))
    height = float(input("Enter your height in inches: "))

    ffmi = ffmiCalculator(weight, bodyFat, height)

    print(ffmi)

if __name__ == "__main__":
    main()