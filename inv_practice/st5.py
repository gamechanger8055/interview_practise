'''
/***
 * At Stripe we keep track of where the money is and move money between bank accounts to make sure their balances are not below some threshold.
 * This is for operational and regulatory reasons, e.g. we should have enough funds to pay out to our users, and we are legally required to separate our users' funds from our own.
 * This interview question is a simplified version of a real-world problem we have here.
 * Let's say there are at most 500 bank accounts, some of their balances are above 100 and some are below.
 * How do you move money between them so that they all have at least 100?
 * Just to be clear we are not looking for the optimal solution, but a working one.
 *
 * Example input:
 * - AU: 80
 * - US: 140
 * - MX: 110
 * - SG: 120
 * - FR: 70
 * Output:
 * - from: US, to: AU, amount: 20
 * - from: US, to: FR, amount: 20
 * - from: MX, to: FR, amount: 10
 *
 * followup1：反过来问，假设给你一系列transfer，问最后account balance是否满足条件。假设所给account balance无论如何也无法做到每个account>=100，问所给的transfer是不是best effort？
 * followup2：如何得到最优解？这里你需要问面试官如何定义最优解。面试官说转账次数越少越好。这样和LC0465就很像了
 */ there are few follow ups in different language also convert to english and then provide code.

 Follow-up 1: Given a series of transfers, determine whether the final account balances satisfy the condition
 that each account balance is >= 100. If the account balances can never meet the condition of every account having
  a balance >= 100, determine if the given transfers represent the best effort.

Follow-up 2: How to get the optimal solution? Here, you need to ask the interviewer how to define the optimal solution. The interviewer says that the optimal solution is to minimize the number of transfers.
'''
import heapq
from collections import defaultdict, deque


def redistribute_balances(accounts):
    deficit_account=[]
    surplus_account=[]
    for acc in accounts:
        balance=accounts[acc]
        if balance>100:
            heapq.heappush(surplus_account,[-(balance-100),acc])
        if balance<100:
            heapq.heappush(deficit_account,[100-balance,acc])
    print(surplus_account,deficit_account)
    transfers=[]
    while surplus_account and deficit_account:
        amount,acc=heapq.heappop(surplus_account)
        amount=-amount
        transfer_amt=0
        #while deficit_account:
        deficit_amount, deficit_acc = heapq.heappop(deficit_account)
        if deficit_amount>amount:
            transfer_amt = amount
            deficit_amount-=amount
            heapq.heappush(deficit_account,[deficit_amount,deficit_acc])
        elif deficit_amount<amount:
            transfer_amt=deficit_amount
            amount-=deficit_amount
            heapq.heappush(surplus_account,[-amount,acc])
        transfers.append({
            'from': acc,
            'to': deficit_acc,
            'amount': transfer_amt
        })
        print(deficit_account)
        print(surplus_account)
        #

    print(transfers)
    #part 2: validating the transfers
    acc_copy=accounts.copy()
    for transfer in transfers:
        from_acc = transfer['from']
        to_acc = transfer['to']
        amount = transfer['amount']
        print(acc_copy)
        acc_copy[from_acc]-=amount
        acc_copy[to_acc]+=amount
    print(acc_copy)
    return all(balance>=100 for balance in acc_copy.values())
    #return transfers

#part 3
def minTransactions(transfers):
    balances=defaultdict(int)
    for transfer in transfers:
        from_acc = transfer['from']
        to_acc = transfer['to']
        amount = transfer['amount']
        balances[from_acc]-=amount
        balances[to_acc]+=amount

    debts=[balance for balance in balances.values() if balance!=0]
    if not debts:
        return 0

    def backtrack(start):
        while start < len(debts) and debts[start] == 0:
            start += 1
        if start == len(debts):
            return 0

        min_trans = float('inf')
        for i in range(start + 1, len(debts)):
            if debts[start] * debts[i] < 0:  # Only consider transactions that can settle debt
                # Try to settle debts[start] with debts[i]
                debts[i] += debts[start]
                min_trans = min(min_trans, 1 + backtrack(start + 1))
                debts[i] -= debts[start]  # Backtrack

        return min_trans

    return backtrack(0)

    '''def bfs(debts):
        q=deque([debts])
        visited=set()
        visited.add(tuple(debts))
        depth = 0

        while q:
            for i in range(len(q)):
                current_debts=q.popleft()
                if all(debt==0 for debt in current_debts):
                    return depth

                for i in range(len(current_debts)):
                    if current_debts[i]==0:
                        continue
                    for j in range(len(current_debts)):
                        if i!=j and current_debts[j]*current_debts[i]<0:
                            new_debts = current_debts[:]
                            new_debts[j] += new_debts[i]
                            new_debts[i] = 0
                            new_tuple = tuple(new_debts)
                            if new_tuple not in visited:
                                visited.add(new_tuple)
                                q.append(new_debts)
            depth+=1'''





accounts = {
    'AU': 80,
    'US': 140,
    'MX': 110,
    'SG': 120,
    'FR': 70
}

print(redistribute_balances(accounts))



