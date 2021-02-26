def lcs(X, Y, m, n,memo = {}): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
  
  
# Driver program to test the above function 
X = "AGGTABASWDQASCDSRDDSAWSASW"
Y = "GXTXAYBNBSEDAWDSRASRDASWASAS"
print("Length of LCS is ", lcs(X , Y, len(X), len(Y))) 