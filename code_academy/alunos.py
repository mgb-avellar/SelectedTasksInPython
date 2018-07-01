#! /usr/bin/python

print
 
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

class_list = [lloyd, alice, tyler]
i = 0
for student in class_list:
  print student["name"]
  print student.keys()[i+3], student["homework"]
  print student.keys()[i], student["quizzes"]
  print student.keys()[i+1], student["tests"]
  print
  # ficou bonito na impressao, mas veio fora de ordem e tive de procurar os indices corretos 
  # para colocar em ordem correta. Pode ser que se rodarmos em outra instancia ou computador, 
  # tenhamos que redefinir os indices. CUIDADO!


# Add your function below!
def average(numbers):
  total = float(sum(numbers))
  return total / len(numbers)
  
def get_average(class_list):
  homework = average(class_list["homework"])
  quizzes = average(class_list["quizzes"])
  tests = average(class_list["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

def get_class_average(class_list): 
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

for student in class_list:  
  print student["name"], get_average(student), get_letter_grade(get_average(student))
  print  


class_average_score = get_class_average(class_list)
class_average_grade = get_letter_grade(class_average_score)

print "The average score and grade of the class are: ", class_average_score, class_average_grade
print


