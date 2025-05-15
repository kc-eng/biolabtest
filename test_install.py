try:
    import biolabtest
    print("biolabtest package is installed successfully!")
    print("\nAvailable functions:")
    print("- biolabtest.print_program1()")
    print("- biolabtest.print_program2()")
    print("- biolabtest.print_program3()")
except ImportError as e:
    print("Error: biolabtest package is not installed properly")
    print(f"Error message: {e}") 