import numpy as np 

if "__main__" == __name__ :
    print("\nSteepest Descent")

    A = np.array([[3,2],[2,6]],dtype=np.float64)
    b = np.array([[2],[-8]])

    print(f"\nA\n{A}")
    print(f"\nb\n{b}")
    print(f"\nf(x) = xAxT - bTx + c")
    print("\n Ax = b")