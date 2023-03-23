import streamlit as st
import numpy as np

st.title("Matrix Operations")

# Slider to adjust the size of the matrix
matrix_size = st.slider("Select the size of the matrix", 1, 10, 3)

# Input boxes for the elements of the matrices
matrix_1 = np.zeros((matrix_size, matrix_size))
matrix_2 = np.zeros((matrix_size, matrix_size))

st.write("Enter the elements of matrix 1:")
for i in range(matrix_size):
    for j in range(matrix_size):
        matrix_1[i, j] = st.number_input(f"Element {i+1},{j+1}", value=0.0, step=0.1, key=f"1-{i+1}-{j+1}")

st.write("Enter the elements of matrix 2:")
for i in range(matrix_size):
    for j in range(matrix_size):
        matrix_2[i, j] = st.number_input(f"Element {i+1},{j+1}", value=0.0, step=0.1, key=f"2-{i+1}-{j+1}")

# Display the two matrices
st.write("Matrix 1: ", matrix_1)
st.write("Matrix 2: ", matrix_2)

# Select the operation to perform
operation = st.selectbox("Select the operation to perform", ("Addition", "Subtraction", "Multiplication", "Transpose", "Inverse", "Eigenvalues and Eigenvectors", "Determinant"))

# Perform the selected operation
if operation == "Addition":
    result = matrix_1 + matrix_2
elif operation == "Subtraction":
    result = matrix_1 - matrix_2
elif operation == "Multiplication":
    result = np.matmul(matrix_1, matrix_2)
elif operation == "Transpose":
    result = np.transpose(matrix_1)
elif operation == "Inverse":
    try:
        result = np.linalg.inv(matrix_1)
    except np.linalg.LinAlgError:
        result = "Matrix is not invertible."
elif operation == "Eigenvalues and Eigenvectors":
    eig_values, eig_vectors = np.linalg.eig(matrix_1)
    result = f"Eigenvalues: {eig_values}\n\nEigenvectors:\n{eig_vectors}"
elif operation == "Determinant":
    result = np.linalg.det(matrix_1)

# Display the result
st.write("Result:")
