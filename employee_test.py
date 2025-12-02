from employee import employee_details
def test_employee_details():
  expected_output = (
    "Employee Name: Vinayak\n"
    "Employee Id: E1101\n"
    "Department: Software\n"
    "Salary: 110000"
  )
  assert employee_details("Vinayak", "E1101", "Software", 110000) == expected_output
