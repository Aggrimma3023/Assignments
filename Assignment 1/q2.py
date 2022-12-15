
print("Enter your gross salary")
gross_salary=int(input())
print("enter the number of dependents")
dependents=int(input())
taxable_income=gross_salary-10000-(dependents*3000)
print("Your taxable income is "+str (taxable_income) )
print ("your tax is "+ str(taxable_income*0.5))