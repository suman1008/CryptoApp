
from .models import CustomerDetails, INV_DB, ASSETS, TRX_CENTRAL


def Temp(name):
    query = INV_DB(Asset_Name=ASSETS(Asset_Name=name))
    print(query)


import datetime


def TotalAge(startDate):
    age = datetime.datetime.now() - startDate
    Age = int(age.days)
    print(Age)
    return Age

def TotalProfit():
    B = INV_DB.objects.all
    m = B.objects.count()
    Summ = 0
    for j in range(0, m + 1):
        CP = B[j].CP
        SP = B[j].SP
        Qty = B[j].Qty
        if (SP > 0):
            Summ = Summ + ((SP-CP)*Qty)
    TP = Summ
    return TP


def InvestedValue():
    A=INV_DB.objects.all
    m=A.objects.count()
    Sum1=0
    Sum2=0
    Sum3=0
    for j in range(0, m + 1):
        CP = A[j].CP
        SP = A[j].SP
        Qty = A[j].Qty
        Sum1 = Sum1 + (CP*Qty)
        Sum2 = Sum2 + (SP * Qty)
        if(SP>0):
            Sum3 = Sum3 + ((SP-CP)*Qty)
    Val_Inv = Sum1-Sum2+Sum3
    return Val_Inv

def main():
    startDate = datetime.datetime(2021, 4, 21, 12, 0, 0)
    TotalAge(startDate)
    CID = int(input("Enter Customer ID: "))
    investment = TRX_CENTRAL.objects.filter(customer_ID__exact=CID)
    tenure = TRX_CENTRAL.objects.filter(customer_ID__exact=CID)
    n = tenure.objects.count()
    CumulativeProfit=0
    for i in range(0,n+1):
        Tenure = int((datetime.datetime.now()-tenure[i].Date_Time_Stamp).days)
        if(investment[i].IN_OUT=="IN"):
            Investment = investment[i].Amount_USD
            profit = (TotalProfit()/TotalAge(startDate))*Tenure*(Investment/InvestedValue())
            CumulativeProfit += profit

    print("Cumulative Profit is ", CumulativeProfit)



if __name__ == '__main__':
    main()