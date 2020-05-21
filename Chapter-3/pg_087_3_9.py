# Financial application: Payroll !!!numbers not formatted

empName = input("Enter employee's name: ")

weekHours = eval(input("Enter number of hours worked in a week: "))

payRate = eval(input("Enter hourly pay rate: "))

fedTaxRate= eval(input("Enter federal tax withholding rate: "))

stateTaxRate = eval(input("Enter state tax withholding rate: "))

grossPay = weekHours * payRate

fedTaxAmount = grossPay * fedTaxRate

stateTaxAmount = grossPay * stateTaxRate

totalDeductions = fedTaxAmount + stateTaxAmount

netPay = grossPay - totalDeductions

print("Employee Name: ", empName)
print("Hours Worked: ", weekHours)
print("Pay Rate: ", payRate)
print("Gross Pay: ", grossPay)
print("Deductions: \n"
"\t", "Federal Withholding (20.0%): ", fedTaxAmount, "\n"
"\t", "State Withholding (9.0%): ", stateTaxAmount, "\n"
"\t", "Total Deductions: ", totalDeductions)
print("Net Pay: ", netPay)