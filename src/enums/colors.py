"""
    A collection of color codes for the Printer class.

    This class provides color codes that can be used for displaying colored messages
    with the Printer class.It includes predefined color codes for red, green, and yellow.

    Usage:
        You can access the color codes as attributes of the Colors class, e.g., Colors.RED.

    Example:
        Printer.success(f"{Colors.GREEN}Success message{Colors.RESET}")

    Available color codes:
        - Colors.RED: Red color code
        - Colors.GREEN: Green color code
        - Colors.YELLOW: Yellow color code
"""

class Colors:
    """
    A collection of color codes for the Printer class.
    """
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
