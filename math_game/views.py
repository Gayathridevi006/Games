from django.shortcuts import render
import random

def generate_problem():
    operators = ['+', '-', '*']
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(operators)
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
    return {'a': a, 'b': b, 'op': op, 'answer': answer}

def math_game_view(request):
    result = None
    user_answer = None
    problem = generate_problem()

    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        user_answer = int(user_answer) if user_answer else None
        correct_answer = int(request.POST.get('correct_answer'))
        if user_answer == correct_answer:
            result = "Correct! 🎉"
        else:
            result = f"Wrong! Correct answer is {correct_answer}"

        # Generate new problem after submission
        problem = generate_problem()

    # ✅ calculate mid value in Python
    mid_value = (problem['a'] + problem['b']) // 2

    return render(request, 'game_3.html', {
        'problem': problem,
        'result': result,
        'user_answer': user_answer,
        'mid_value': mid_value,  # pass to template
    })
