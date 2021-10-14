def a_file
   
   print("Keep it logically awesome.")
   print("Keep it logically awesome.")
   print("Keep it logically awesome.")
  
    a_file = open("quote.txt", "r")
    lines = a_file.readlines()
    last_lines = lines[-5:]
  
    print(last_lines)
   
    a_file