def knapsack_recursive(W,weights,values,n):
    if n==0 or W==0:
        return 0
    if weights[n-1]<=W:
        return max(values[n-1]+knapsack_recursive(W-weights[n-1],weights,values,n-1),knapsack_recursive(W,weights,values,n-1))
    return knapsack_recursive(W,weights,values,n-1)
N = 3
W = 50
profit= [60, 100, 120]
weight= [10, 20, 30]
print(knapsack_recursive(W,weight,profit,N))