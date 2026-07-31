"""
Topic: Variable Scope
Description: Demonstrates global variables, local variables, and the global keyword.
Author: Suryansh
"""

# ============================================
# Global Variable
# ============================================

x = 100


def display_global():
    """Accesses the global variable."""

    print(x)

    return x


display_global()


# ============================================
# Local Variable
# ============================================

def display_local():
    """
    A local variable exists only inside the function.
    It does not affect the global variable.
    """

    x = 50

    print(x)

    return x


display_local()


# ============================================
# Using the global Keyword
# ============================================

def modify_global():
    """
    The global keyword allows modifying
    the global variable.
    """

    global x

    x = 40

    print(x)

    return x


modify_global()


# ============================================
# Accessing the Updated Global Variable
# ============================================

def display_updated_global():
    """Displays the updated global variable."""

    global x

    print(x)

    return x


display_updated_global()