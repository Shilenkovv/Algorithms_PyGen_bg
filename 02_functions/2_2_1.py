def calculate(vars: str, values: list, exp: str) -> int:
    """_summary_
        Calculcates expression
    Args:
        vars (str): variabless list
        values (list): variable values
        exp (str): mathematical expression

    Returns:
        int: exp result
    """
    expression = exp

    for var in vars:
        if var in expression:
            expression = expression.replace(var, str(values[vars.find(var)]))
    return eval(expression)
