def Cholesky(Aaug):
    """
    This function finds the solution to a matrix equation Ax=b by the Colesky method
    :param Aaug: An augmented matrix
    :return: the solution vector x, L and Ltrans as a tuple
    """
    pass

def SymPosDef(A):
    """
    This function first finds the transpose of A and then compares all elements of A to Atrans.
    If I pass that test, I create a vector x with random numbers and perform xtrans*A*x to see if>0.
    :param A: a nxn matrix
    :return: True if symmetric, positive definite
    """
    pass

def Transpose(A):
    """
    This function finds the transpose of a square matrix
    :param A: an nxn matrix
    :return: the transpose of A
    """
    pass

def main():
    """
    Step 1:  I need to first define the matrices given in part a) of HW3_2024.
    Step 2:  pass a matrix to SymPosDef to tell if it is symmetric, positive definite
    Step 3:  based on result of Step 2, use either the Doolittle or Cholesky method to solve
    Steo 4:  check my answer by multiplying A*x to see if I get b
    Step 4:  print the solution vector and which method was used to the cli
    """
    pass

if __name__ == "__main__":
    main()