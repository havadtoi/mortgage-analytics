#importing libraries used in the code
import matplotlib.pyplot as plt #Used for charting
import numpy as np

#Setting parameters for calculations
HousePrice = 500000         #Value of the house to be purchased
Deposit = 100000            #Initial downpayment for the mortgage
InterestRate = 0.036        #Annual interest rate on the Mortgage
Duration = 25               #Number of years of the mortgage contract

#Market Rates and estimates
HouseMarketRate = 0.0745      #Expected average house price index growth rate / UK Average is 7.45% for London Flats between '91 - '14
InvestmentRate = 0.1185      #Expected average investment growth rate / S&P500 Index average is 11.85% between '70 and 2017

#Performing basic calculations based on the given parameters
MortgageValue = HousePrice - Deposit                        #Mortgage contract value

#Calculating lists for each contracted year
Equity = [Deposit + MortgageValue / Duration * value for value in range(Duration + 1)]          #Amount of money paid in the house
MortgageBalance = [MortgageValue - Equity[value] + Deposit for value in range(Duration + 1)]    #Amount of money remaining to be paid to the bank
InterestToPay = [MortgageBalance[value] * InterestRate for value in range(Duration + 1)]        #Amount of interest paid to the bank each year
InterestPaid = [sum(InterestToPay[0:value]) for value in range(Duration + 1)]                   #Cumulative interest payment to the bank
HouseValue = [HousePrice * (1 + HouseMarketRate) ** value for value in range(Duration + 1)]     #House price appreciation
LoanToEquity = [Equity[value]/HouseValue[value] * 100 for value in range(Duration + 1)]         #Loan to Equity development
NetValueOwned = [HouseValue[value] - MortgageBalance[value] for value in range(Duration + 1)]   #Net value owned in the house at the estimated market price
HouseMtM_PnL = [HouseValue[value] - HousePrice for value in range(Duration + 1)]                #Profi&Loss on the house value
HouseNetPnL = [HouseMtM_PnL[value] - InterestPaid[value] for value in range(Duration + 1)]      #Profit&Loss on the whole project

#Cumulative alternative investment cost of the equity paid in to the house
AlternativeInvestmentCost = list([0 for value in range(Duration +1)])
for value in range(1, Duration +1) :
    AlternativeInvestmentCost[value] = AlternativeInvestmentCost[value-1] + AlternativeInvestmentCost[value-1] * InvestmentRate + Equity[value] * InvestmentRate

NetProfit = [HouseNetPnL[value] - AlternativeInvestmentCost[value] for value in range(Duration + 1)]

#Charting the final calculation
plt.plot(NetProfit, label = 'Net Mortgage P&L')

plt.title('Mortgage Analysis in an Ideal World')
plt.grid(True)
plt.ylabel('Currency')
plt.xlabel('Years')
plt.legend()
plt.show()



### 2nd Section



#Testing the whole calculation with randomized market movements
np.random.seed()

for x in range(10) :
    InvestmentRatesYearly = [np.random.triangular(-10,(InvestmentRate * 100),15) / 100 for value in range(Duration + 1)]
    HouseMarketRatesYearly = [np.random.triangular(-5,(HouseMarketRate * 100),10) / 100 for value in range(Duration + 1)]
    HouseValue = [HousePrice * (1 + HouseMarketRatesYearly[value]) ** value for value in range(Duration + 1)]     #House price appreciation using the random market rate generator
    LoanToEquity = [Equity[value]/HouseValue[value] * 100 for value in range(Duration + 1)]         #Loan to Equity development
    NetValueOwned = [HouseValue[value] - MortgageBalance[value] for value in range(Duration + 1)]   #Net value owned in the house at the estimated market price
    HouseMtM_PnL = [HouseValue[value] - HousePrice for value in range(Duration + 1)]                #Profi&Loss on the house value
    HouseNetPnL = [HouseMtM_PnL[value] - InterestPaid[value] for value in range(Duration + 1)]      #Profit&Loss on the whole project
    #Cumulative alternative investment cost of the equity paid in to the house
    AlternativeInvestmentCost = list([0 for value in range(Duration +1)])
    for value in range(1, Duration +1) :
        AlternativeInvestmentCost[value] = AlternativeInvestmentCost[value-1] + AlternativeInvestmentCost[value-1] * InvestmentRatesYearly[value] + Equity[value] * InvestmentRate #using the random market rate generator
    NetProfit = [HouseNetPnL[value] - AlternativeInvestmentCost[value] for value in range(Duration + 1)]
    #Charting the final calculation
    plt.plot(NetProfit, label = 'Net Mortgage P&L')


plt.title('Mortgage Analysis with some level of realism')
plt.grid(True)
plt.ylabel('Currency')
plt.xlabel('Years')
plt.show()

#ToDo: Create 3D graphics on the house market rate and investment rate affects

