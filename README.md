# CryptoApp
Crypto Mutual Funds Investment Application
Django - React Native Application Project
Abstract
The main purpose of this app will be for users to buy our mutual funds, and monitor their investments in the form of graphs and charts.

Users can select tenure of investment, Locking period, subscription model, and pay through upi, bank transfer, credit/ debit.

Once investment is made by the user, they can view their portfolio to see their profit/ loss statement.

Users can withdraw their funds as well, therefore we would need to provide users with a profile and KYC should be conducted, the process of repayment should be automated with some marketplace api
Database Architecture

Model 1: CRM DB
Customer ID (Primary Key)
Customer Name
PAN
Aadhaar
Passport
Photo

Model 2: Transaction Central DB (TRX DB)
All transactions i.e. all deposits and withdrawals are recorded in this DB, this should be managed and updated automatically by the API that will manage payments.
TRX ID (Unique)
Customer ID (Foreign Key)
Customer Name
Amount (+ve = deposit, -ve = withdrawal)
Date Time Stamp

We would always need to maintain a liquidity of 25% to 28% to facilitate quick seamless withdrawals.
Customers will be encouraged to set up a 30-60-90 days locking period on their investments, although this will be optional.

Model 3: Investment DB (INV DB)
Asset Name (eg: BTC, Primary Key)
Quantity (Qty)
Cost Price (CP) (blank=True)
Selling Price (SP) (blank=True)
Value Invested ( = (Qty  CP)-(Qty  SP) )
Asset’s current value should be stored in a variable (ACV) by using CoinMarketCap API and used during calculations. (developer can use a better way if they have one)

Functions to be made
F1: Profit / Loss Calculation (def PnL)
PnL% = ((ACV(Asset) - Asset[CP])/ACV(Asset)) x 100                                                     (E1)

ACV(Asset) is the method that derives the current value of Asset using API call, it takes Asset Name as argument.
Asset[CP] is the cost price of Asset, when purchase is made, this value needs to be updated manually by the admin, when a purchase is made.

A valid problem arises here, that if a person A invests 1000 usd in january and the value of the asset purchased in jan, increases to 2000 usd, and then another person B, invests in february, A’s profit will be cut in half instantly. Which shouldn’t be the case.

To solve this problem I suggest, this simple equation
profit = (total profit/Total Age) x tenure x [Investment/Total Value]                                (E2)

Total profit = total profit the fund makes from its inception
Total Age = number of days the fund is active since inception
Tenure = number of days the investor has invested money into the fund

Total Value = Value Invested + Liquidity                                                                              (E3)


Value Invested = (Qty  CP)-(Qty  SP)                                                                    (E4)

Day one for tenure will start after 15 days of investment which will be a mandatory locking period, if someone withdraws investment within the first 15 days, no interest will be paid.

Cumulative Profit of a person over time
Cumulative Profit =  profit(TRX_ID)                                                                                  (E5)

Here profit() is a function which takes TRX_ID as argument to get reference of the amounts invested by the customer, to calculate profit
for(TRX_ID){
if (Amount>0) {
pro=profit()
Cumulative_pro += pro
}}
F2: Liquidity Calculation (def Liquidity)
Liquidity = Total Deposit - Value Invested
Liq% = Liquidity/Total Invested x 100                                                                                   (E6)

Total Deposit = Algebraic sum of all Transactions (derived from model 2)
Value Invested = Algebraic sum of all Investments (derived from model 3)
If Liq%<28, Shows warning in Admin UI

User Interfaces
Login/ Register/ Google Auth/ phone Auth
Home Screen: 
Shows Total Portfolio Profit %
Graphs
