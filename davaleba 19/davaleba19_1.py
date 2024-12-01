import json
import os

# საშუალო ხელფასის გამომთვლელი ფუნქცია

def average_salary(department):
    employees = department.get("employees", [])
    total_salary = 0
    count = 0
    for employee in employees:
        try:
            salary = float(employee["salary"])
            total_salary += salary
            count += 1
        except (ValueError, TypeError):
            continue
    return total_salary / count if count > 0 else 0

def main():
    input_file = "homework_1.json"
    output_file = "average_salary.json"

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return
    
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        return
    
    average_salaries = {}
    for department_key, department_value in data.items():
        average_salaries[department_value["name"]] = average_salary(department_value)
    
    print("Average salaries per department:")
    
    for dept, average_salary in average_salaries.items():
        print(f"{dept}: {average_salary:.2f}")
        
    try:
        with open(output_file, "w") as file:
            json.dump(average_salaries, file, indent=4)
        print(f"Average salaries written to '{output_file}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()