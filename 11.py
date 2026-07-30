def solve_linear_system(a, b, c, d, e, f, tol=1e-9):
    """
    Solve the 2x2 linear system:
        a*x + b*y = c
        d*x + e*y = f

    Returns:
        (x, y) if there is a unique solution
        None if there are infinitely many solutions
        "No solution" if the system is inconsistent
    """
    det = a * e - b * d

    if abs(det) > tol:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det
        return x, y

    # det == 0: either infinite solutions or no solution
    if abs(a * f - c * d) < tol and abs(b * f - c * e) < tol:
        return None  # infinite solutions
    return "No solution"

def main():
    print("请输入方程组系数 a,b,c 和 d,e,f，表示：")
    print("  a*x + b*y = c")
    print("  d*x + e*y = f")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
    e = float(input("e = "))
    f = float(input("f = "))

    result = solve_linear_system(a, b, c, d, e, f)
    if result == "No solution":
        print("该方程组无解。")
    elif result is None:
        print("该方程组有无穷多解。")
    else:
        x, y = result
        print(f"唯一解：x = {x}, y = {y}")

if __name__ == "__main__":
    main()