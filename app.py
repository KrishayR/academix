from mathgenerator import mathgen
from flask import Flask, render_template
from flask import request, jsonify
import sys
import random
# import requests
# from bs4 import BeautifulSoup

app = Flask(__name__)

# basic_funcs = ['basic_algebra', 'log', 'multiply', 'int_to_22_matrix', 'midpoint_of_two_points',
#                'factoring', 'system_of_equations', 'distance_two_points', 'linear_equations', 'intersection_of_two_lines', 'vector_cross',
#                 'simple_interest']

# funcs = []

# res = requests.get('https://github.com/lukew3/mathgenerator')
# print("The status code is ", res.status_code)
# print("\n")
# soup_data = BeautifulSoup(res.text, 'html.parser')
# print("\n")
# lst = soup_data.find_all('td')[0::6]


# for i in lst:
#     funcs.append(i.get_text())


# funcs = funcs[17:]
# basic_funcs += funcs
# funcs = basic_funcs
funcs = ['basic_algebra', 'log', 'factoring', 'system_of_equations', 'distance_two_points', 'linear_equations', 'quadratic_equation', 'multiply_complex_numbers', 'complex_quadratic', 'combine_like_terms', 'expanding', 'addition', 'subtraction', 'multiplication', 'division', 'square_root', 'square', 'complex_division', 'divide_fractions', 'fraction_multiplication', 'compare_fractions', 'cube_root', 'exponentiation', 'percentage', 'is_prime', 'power_of_powers', 'area_of_triangle', 'valid_triangle', 'third_angle_of_triangle', 'pythagorean_theorem']
isolution = 0

@app.route('/homework')
def popu():
    hwproblems = []
    hwsolutions = []
    for i in range(1, len_missed_q*2):
        func = random.choice(missed_q)
        method = getattr(mathgen, func)
        hwproblem, hwsolution = method()

        hwproblems.append(hwproblem)
        hwsolutions.append(hwsolution)

    return render_template('homework.html', name=[hwproblems, hwsolutions, len_missed_q])

@app.route('/ace')
def popo():
    return render_template('homeworka.html')

@app.route('/create')
def create():
    return render_template('teachers.html', lst=funcs)


@app.route('/homework',  methods=["GET", "POST"])
def populate():
    global missed_q
    global len_missed_q
    if request.method == "POST":
        missed_q = request.get_json()
        len_missed_q = len(missed_q)
        if len(missed_q) < 1:
            print("No elements in missedq")
            popo()
        else:
            missed_q = list(set(missed_q))
            print(missed_q)
            popu()
        
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500

@app.route('/assessment')
def assessment():
    problems = []
    solutions = []
    methods = []
    for i in range(1, 6):
        func = random.choice(funcs)
        method = getattr(mathgen, func)
        methods.append(func)

        problem, solution = method()
        problems.append(problem)
        solutions.append(solution)

    return render_template('assessment.html', assess=[problems, solutions, methods])

@app.route('/startassessment')
def startassessment():
    return render_template('startassessment.html')

if __name__ == "__main__":
    app.run(debug=True)




