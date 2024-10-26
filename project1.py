def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    return weight / pow(height, 2)

def get_bmi_rating(bmi):
    """Return the BMI rating category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "You are healthy"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight, height, age, sex):
    """Calculate BMR based on weight, height, age, and sex."""
    if sex.lower() == 'm':
        return 66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    else:
        return 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

def calculate_calories(bmr):
    """Calculate daily caloric needs based on activity level."""
    activity_multipliers = {
        1: 1.2,    # Sedentary
        2: 1.375,  # Light exercise
        3: 1.55,   # Moderate exercise
        4: 1.725,  # Heavy exercise
        5: 1.9     # Very active
    }
    
    calories = {level: round(bmr * multiplier, 0) for level, multiplier in activity_multipliers.items()}
    
    print("To maintain your weight, follow these guidelines:")
    for level, cal in calories.items():
        print(f"{level}: Activity level {level} - you need {cal} k/calories")
    
    return calories

def main():
    print("Welcome to the BMI and BMR Tracker!")

    # Collect all user inputs
    weight = float(input("What is your weight in kg: "))
    height_m = float(input("What is your height in meters: "))
    age = float(input("What is your age: "))
    sex = input("What is your sex (m/f): ")
    height_cm = height_m * 100  # Convert height to cm for BMR calculation

    # Calculate and display BMI
    bmi = calculate_bmi(weight, height_m)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(get_bmi_rating(bmi))
    
    # Calculate and display BMR
    bmr_value = calculate_bmr(weight, height_cm, age, sex)
    print(f"\nYour BMR is: {bmr_value:.2f}")
    
    # Calculate and display calorie requirements
    calculate_calories(bmr_value)

if __name__ == "__main__":
    main()