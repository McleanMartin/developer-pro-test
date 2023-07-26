from django.db import models

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name =("Department")
        verbose_name_plural =("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now=False)
    address = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=50)
    total_employees = models.IntegerField()
    cell = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    departments = models.OneToOneField(Department, verbose_name=("departments"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    def __str__(self):
        return self.name

class Employee(models.Model):
    role = (
        ('manager','manager'),
        ('accountant','accountant'),
        ('security','security')
        )
    emp_id = models.CharField(max_length=50,unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.CharField(choices=role, max_length=50)

    class Meta:
        verbose_name =("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})


