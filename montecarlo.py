import random
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

simnum = 10000
trades = 200

#winner = 31.25
#loser = 62.5
winner = 200
loser = 400
r = winner/loser
winrate = 1 / (1+r)

maxdrawdown = 2000
target = 3000

passed = 0;
failed = 0;

simulations = []

for i in range(simnum):
    profit = 0
    series = [];
    high = 0;
    incomplete = True;

    for j in range(trades): 
    
        roll = random.randrange(0,1000)
        #if roll > (winrate * 1000):
        #    profit = profit - loser;
        #else:
        #    profit = profit + winner;
        
        if roll < 333:
            profit = profit - 250
        elif roll < 547:
            profit = profit - 62.5
        elif roll < 691:
            profit = profit + 93.75
        elif roll < 757:
            profit = profit + 187.5
        else:
            profit = profit + 312.5
        
        
        series.append(profit);
        if high < profit:
            high = profit
        
        if profit >= 3000:
            passed += 1
            break;
        
        drawdown = high - profit
        if drawdown >= maxdrawdown:
            failed += 1
            break;
            
    simulations.append(series)
    
tradenum = list(range(0,trades))

percent = round(((passed / (passed + failed)) * 100), 2)
print(f'R-factor:{r} Winrate:{winrate}')
print(f'Passed:{passed}')
print(f'Failed:{failed}')
    
#graph it
plt.title(f'Funded Trader Monte Carlo Simualtion. R={r} \n Pass rate: {percent}%')
plt.xlabel('Trades')
plt.ylabel('Profit')
#plt.figure(figsize=(10,6))
for sim in simulations:
    tradenum = list(range(0,len(sim)))
    plt.plot(tradenum, sim, alpha=.1, linewidth=.1, color='k')
    
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
