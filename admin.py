from django.contrib import admin
from hospital_app.models import Company,Medicine,MedicalDetails,AdminLogin,Employee,Customer,Bill,EmployeeSalary,BillDetails,BillDetails,CustomerRequest,CompanyAccount,ComapnyBank,EmployeeBank,Doctor,Patient,Appointment

# Register your models here.
admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(AdminLogin)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(ComapnyBank)
admin.site.register(EmployeeBank)

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)