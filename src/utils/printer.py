"""
Printer Module

This module provides a utility class for printing
standardized messages with different colors and formatting
to indicate success, warning, or error.

Usage:
    from utils.printer import Printer

    # Regular message
    Printer.message("This is a regular message.")

    # Success message
    Printer.success("This is a success message.")

    # Warning message
    Printer.warning("This is a warning message.")

    # Error message
    Printer.error("This is an error message.")
"""

try:
    from enums.colors import Colors
except ImportError:
    from ..enums.colors import Colors

class Printer:
    """
    A utility class for printing standardized messages.
    """

    @staticmethod
    def _printer(message: str) -> None:
        """
        Internal method to print a message.

        Args:
            message (str): The message to be printed.
        """
        print(message)

    @staticmethod
    def message(message: str) -> None:
        """
        Print a regular message.

        Args:
            message (str): The message to be printed.
        """
        Printer._printer(message)

    @staticmethod
    def success(message: str) -> None:
        """
        Print a success message with green color.

        Args:
            message (str): The success message to be printed.
        """
        Printer._printer(f"{Colors.GREEN} {message} \033[0m")

    @staticmethod
    def warning(message: str) -> None:
        """
        Print a warning message with yellow color.

        Args:
            message (str): The warning message to be printed.
        """
        Printer._printer(f"{Colors.YELLOW} {message} \033[0m")

    @staticmethod
    def error(message: str) -> None:
        """
        Print an error message with red color.

        Args:
            message (str): The error message to be printed.
        """
        Printer._printer(f"{Colors.RED} {message} \033[0m")
