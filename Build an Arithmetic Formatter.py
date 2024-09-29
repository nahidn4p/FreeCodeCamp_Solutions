def arithmetic_arranger(problems, show_answers=True):
    first=""
    second=""
    lines=""
    res=""
    if len(problems)>5:
        return "Error: Too many problems."
    else:
          for problem in problems:
               print(problem)
               upper,operator,lower=problem.split()
               
               print(upper,operator,lower)
               if not upper.isdigit() or not lower.isdigit():
                    return "Error: Numbers must only contain digits."
               else:
                    if len(upper) > 4 or len(lower) > 4:
                         return "Error: Numbers cannot be more than four digits."
               if operator != "+" and operator != "-":
                         return "Error: Operator must be '+' or '-'."
               elif operator == "+" :
                         sol = str(int(upper) + int(lower))

               elif operator == "-" :
                         sol = str(int(upper) - int(lower))
               
               
               length = max(len(upper), len(lower)) + 2
               top=str(upper).rjust(length)
               bottom=operator+str(lower).rjust(length-1)
               line = ""
               result = str(sol.rjust(length))
               for _ in range(length):
                    line += "-" 
               if problem!=problems[-1]:     
                    first +=top+'    '
                    second +=bottom+'    '
                    lines +=line+'    '
                    res +=result+'    '     
               else:
                       first +=top    
                       second +=bottom
                       lines +=line
                       res +=result
          if (show_answers):
                    operations= first+"\n"+second+"\n"+lines+"\n"+res
          else:
                    operations= first+"\n"+second+"\n"+lines
          
          return operations
                    

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
