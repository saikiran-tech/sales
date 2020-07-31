from django.db import models

# Create your models here.

region_choices = [
    ("Sub-Saharan Africa","Sub-Saharan Africa"),
    ("Europe","Europe"),
    ("Asia","Asia"),
    ("Middle East and North Africa","Middle East and North Africa"),
    ("Central America and the Caribbean","Central America and the Caribbean"),
    ("Australia and Oceania","Australia and Oceania"),
    ("North America","North America")
]


class Salesrecord(models.Model):
    Region = models.CharField("Region", max_length=100, choices=region_choices, default="Asia")
    Country = models.CharField("Country", max_length=100)
    Item_type = models.CharField("Item Type", max_length=100)
    Sales_channel = models.CharField("Sales Channel", max_length=100)
    Order_priority = models.CharField("Order Priority", max_length=30)
    Order_date = models.CharField("Order Date", max_length=30)
    Order_ID = models.IntegerField("Order ID", null=True)
    Ship_date = models.CharField("Ship Date", max_length=30)
    Units_sold = models.IntegerField("Units Sold", null=True)
    Unit_price = models.FloatField("Units Price", null=True)
    Unit_cost = models.FloatField("Unit Cost", null=True)
    Total_revenue = models.FloatField("Total Revenue", null=True)
    Total_cost = models.FloatField("Total Cost", null=True)
    Total_profit = models.FloatField("Total Profit", null=True)

    def __str__(self):
        return "Region:{0} Country: {1}".format(self.Region, self.Country)
