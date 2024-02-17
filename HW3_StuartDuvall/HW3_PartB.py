#region imports
import math
#endregion

#region functions
def tPDF(m, u):
    """Calculate the probability density function of the t-distribution."""
    return (gamma((m + 1) / 2) / (math.sqrt(m * math.pi) * gamma(m / 2))) * ((1 + (u ** 2) / m) ** (-(m + 1) / 2))

def gamma(m):
    """Calculate the gamma function."""
    if m == 1:
        return 1
    elif m == 0.5:
        return math.sqrt(math.pi)
    else:
        return (m - 1) * gamma(m - 1)

def main():
    try:
        m = float(input("Enter degrees of freedom (m): "))
        u_values = [float(input(f"Enter u value {i+1}: ")) for i in range(3)]

        for u in u_values:
            pdf = tPDF(m, u)
            print(f"For m = {m}, u = {u}, PDF = {pdf}")

    except ValueError:
        print("Invalid input. Please enter valid degrees of freedom and u values.")

if __name__ == '__main__':
    main()
#endregion