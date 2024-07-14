def safe_divide(numerator, denominator):
        try: 
            x = float(numerator)
            y = float(denominator)
            return f"The result of the division is {x/y}"
    
        except ZeroDivisionError:
            return f"Error: Cannot divide by zero."

        except ValueError:
            return f"Error: Please enter numeric values only."

    

