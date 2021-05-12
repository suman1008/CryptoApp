from django.db import models

# Create your models here.

#class Employee(models.Model):
#    Positions = [('TRADER',), ('HR',), ('ANALYST',), ('ADMIN',)]
#    Employee_Id = models.AutoField(primary_key=True)
#    Employee_Name = models.CharField(max_length=70, unique=False, blank=False)
#    Position = models.Choices(Positions)
#    UserName = models.CharField(max_length=70, unique=False, blank=False)
 #   Password = models.CharField(max_length=70, unique=False, blank=False)

class ASSETS(models.Model):
    Asset_Name = models.CharField(max_length=10, unique=True, blank=False, primary_key=True)
    def __str__(self):
        return self.Asset_Name

class CustomerDetails(models.Model):
    C_ID = models.CharField(max_length=10, unique=True, blank=False, primary_key=True)
    Customer_Name = models.CharField(max_length=50, unique=False, blank=False)
    PAN = models.CharField(max_length=10, unique=True, blank=True)
    Adhaar = models.CharField(max_length=50, unique=True, blank=True)
    Passport = models.CharField(max_length=50, unique=True, blank=True)
    Residential_Address = models.TextField(max_length=500, unique=False, blank=True)
    Phone = models.IntegerField(unique=True, blank=True)
    Email = models.CharField(max_length=100, unique=True, blank=True)
    Birth_Date = models.DateField(default=00 - 00 - 0000)

    def __str__(self):
        return self.Customer_Name, self.C_ID

class TRX_CENTRAL(models.Model):
    TRX_ID = models.CharField(max_length=70, unique=True, blank=False)
    customer_ID = models.ForeignKey(CustomerDetails, on_delete=models.PROTECT, related_name='CID')
    Name = models.CharField(max_length=50, unique=False, blank=True)
    Amount_USD = models.FloatField(unique=False, blank=False)
    IN_OUT = models.CharField(max_length=7, unique=False, blank=False)
    Date_Time_Stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name, self.Amount_USD, self.Date_Time_Stamp

class INV_DB(models.Model):
    auto_id = models.AutoField(primary_key=True)
    Asset_Name = models.ForeignKey(ASSETS, on_delete=models.PROTECT, related_name='ASSETS')
    Qty = models.FloatField(unique=False, blank=False)
    CP = models.FloatField(unique=False, blank=True, default=0)
    SP = models.FloatField(unique=False, blank=True, default=0)


    def __str__(self):
        return self.Asset_Name, self.Qty, self.CP, self.SP
    # def ValueInvested(self):
    # Value_Invested = sum(Qty*CP)-sum(Qty*SP);

