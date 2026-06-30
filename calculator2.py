def calculator():
  """A simple calculator that performs +, -, *, / on two numbers."""
  print("=== Welcome to the Calculator ===\n")

  # Get user input with validation
  try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
  except ValueError:
      print("Error: Please enter valid numeric values.")
      return

  # Display operation menu
  print("\nChoose an operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  print("5. Exponentiation (**)")
  print("6. Modulus (%)")
  print("7. Floor Division (//)")

  choice = input("Enter the number of your choice (1-7): ")

  # Perform the selected operation
  if choice == '1':
      result = num1 + num2
      operation = "+"
  elif choice == '2':
      result = num1 - num2
      operation = "-"
  elif choice == '3':
      result = num1 * num2
      operation = "*"
  elif choice == '4':
      if num2 == 0:
          print("Error: Division by zero is not allowed.")
          return
      result = num1 / num2
      operation = "/"
  elif choice == '5':
      result = num1 ** num2
      operation = "**"
  elif choice == '6':
      if num2 == 0:
          print("Error: Modulus by zero is not allowed.")
          return
      result = num1 % num2
      operation = "%"
  elif choice == '7':
      if num2 == 0:
          print("Error: Floor division by zero is not allowed.")
          return
      result = num1 // num2
      operation = "//"
  else:
      print("Error: Invalid choice. Please select a number from 1 to 7.")
      return
  

  # Format and display the result in a readable way
  # Using 2 decimal places if the number is not an integer, else show as integer
  def format_number(n):
      return f"{n:.2f}".rstrip('0').rstrip('.') if '.' in str(n) else str(n)

  num1_f = format_number(num1)
  num2_f = format_number(num2)
  res_f = format_number(result)

  print("\n" + "=" * 40)
  print(f"  {num1_f} {operation} {num2_f} = {res_f}")
  print("=" * 40)

  # Extra: show a more descriptive output
  print(f"\nResult: {num1_f} {operation} {num2_f} = {res_f}")

if __name__ == "__main__":
  calculator()