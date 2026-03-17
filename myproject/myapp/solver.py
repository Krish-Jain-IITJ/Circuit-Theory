from turtle import clear

import numpy as np

def solve_circuit_network(R, C, L, n):

    w = 1  # angular frequency

    impedance = R + 1j*(L*w - 1/(w*(C+1e-6)))
    Y = 1/impedance
    result = []
    #impedance A matrix

    size = n*n
    A = np.zeros((size, size), dtype=complex)

    for row in range(n):
        for col in range(n):

            i = row*n + col

            # diagonal term
            A[i][i] = 4 * impedance

            # UP neighbour
            if row > 0:
                j = (row-1)*n + col
                A[i][j] = -impedance

            # DOWN neighbour
            if row < n-1:
                j = (row+1)*n + col
                A[i][j] = -impedance

            # LEFT neighbour
            if col > 0:
                j = row*n + (col-1)
                A[i][j] = -impedance

            # RIGHT neighbour
            if col < n-1:
                j = row*n + (col+1)
                A[i][j] = -impedance


    result.append(impedance)
    #current in each loop
    V = np.ones((n*n,1),dtype = complex)
    A_dsh = np.linalg.inv(A)
    I = A_dsh@V

    return result , A , I
    

#control algorithm

# def pid_control(I_ref, I_measured, kp=0.5, ki=0.1, kd=0.01):

#     error = I_ref - I_measured

#     integral = np.sum(error)
#     derivative = np.gradient(error.flatten())

#     control = kp*error + ki*integral + kd*derivative.reshape(error.shape)

#     return control


# def buck_converter_voltage(Vin, duty):

#     # simple buck relation
#     Vout = duty * Vin
#     return Vout


# # ------------------------
# # Simulation
# # ------------------------

# R = 10
# C = 0.01
# L = 0.001
# n = 2

# # reference currents
# Z, A, I_ref = solve_circuit_network(R, C, L, n)

# # change impedance
# R_new = 20
# Z2, A2, I_measured = solve_circuit_network(R_new, C, L, n)

# # PID controller
# control_signal = pid_control(I_ref, I_measured)

# # adjust voltage using buck converter idea
# Vin = 10
# duty_cycle = np.clip(np.real(control_signal),0,1)

# Vout = buck_converter_voltage(Vin, duty_cycle)

# print("Reference Current:\n", I_ref)
# print("Measured Current after impedance change:\n", I_measured)
# print("Control Signal:\n", control_signal)
# print("Adjusted Output Voltage:\n", Vout)

#control algorithm

def pid_control(I_ref, I_measured, prev_error, integral, kp=0.5, ki=0.1, kd=0.01):

    error = I_ref - I_measured

    integral = integral + error
    derivative = error - prev_error

    control = kp*error + ki*integral + kd*derivative

    return control, error, integral


# def buck_converter_voltage(Vin, duty):

#     Vout = duty * Vin
#     return Vout


# ------------------------
# Simulation
# ------------------------

R = 1
C = 0.01
L = 0.001
n = 2

# reference currents
Z, A, I_ref = solve_circuit_network(R, C, L, n)

# change impedance
R_new = 0
Z2, A2, I_measured = solve_circuit_network(R_new, C, L, n)

# Vin = 10

prev_error = np.zeros_like(I_ref)
integral = np.zeros_like(I_ref)

for step in range(100):   # iterative control

    control_signal, prev_error, integral = pid_control(
        I_ref, I_measured, prev_error, integral
    )

    # duty_cycle = np.clip(np.real(control_signal), 0, 1)

    # Vout = buck_converter_voltage(Vin, duty_cycle)

    # simulate new current after control
    I_measured = I_measured + 0.1*control_signal

print("Reference Current:\n", I_ref)
print("Final Controlled Current:\n", I_measured)
# print("Final Duty Cycle:\n", duty_cycle)
# print("Output Voltage:\n", Vout)

#accuracy
final_accuracy = (1 - np.linalg.norm(I_ref - I_measured) / np.linalg.norm(I_ref)) * 100

print(f"Final Accuracy: {final_accuracy:.2f}%")

