import numpy as np

def solve_circuit_network(R, C, L, n):

    w = 1  # angular frequency

    impedance = R + 1j*(L*w - 1/(w*(C+1e-6)))
    result = []
    #impedance A matrix
    A = np.zeros((n*n, n*n), dtype=complex)
    for i in range(n*n):
        for j in range(n*n):
            if i == j : A[i][j] = 4*impedance
            else:
                #down loop
                if i+1<n*n : 
                    A[i+1][j] = -impedance
                    A[j][i+1] = -impedance
                #up loop
                if i-1 >= 0:
                    A[i-1][j] = -impedance
                    A[j][i-1] = -impedance
                
                #right loop
                if i < n*n and j+1<n*n: 
                    A[i][j+1] = -impedance
                    A[j+1][i] = -impedance
                #left loop
                if i < n*n and j-1>=0: 
                    A[i][j-1] = -impedance
                    A[j-1][i] = -impedance
    for i in range(n*n):
        for j in range(n*n):
            if i == j : A[i][j] = 4*impedance
   
    result.append(impedance)
    #current in each loop
    V = np.ones((n*n,1),dtype = complex)
    A_dsh = np.linalg.inv(A)
    I = A_dsh@V

    return result , A , I
    


# for n there will be nxn loops in total
# (n+1)^2 nodes in total
# 2n(n+1) horizontal wires









# def convert_to_graph(R, C, L ,N):
#     vector<vector<pair<int,int>>>& adj;
    
