def employee_details(name, emp_id, department, salary):
  result = (
    f"Employee Name: {name}\n"
    f"Employee Id: {emp_id}\n"
    f"Department: {department}\n"
    f"Salary: {salary}"
  )
  return result

if __name__ == "__main__":
  name = "Vinayak"
  emp_id = "E1101"
  department = "Software"
  salary = "110000"
  print(employee_details(name, emp_id, department, salary))
