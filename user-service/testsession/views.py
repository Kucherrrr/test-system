import requests
from django.shortcuts import render
from django.http import JsonResponse

def start_test(request):
    request.session['score'] = 0
    request.session['questions_asked'] = 0
    request.session['current_level'] = 'easy'
    request.session['shown_question_ids'] = []
    return get_next_question_html(request)

def submit_answer(request):
    user_answer = request.GET.get('answer', '').strip()
    correct_answer = request.session.get('current_correct_answer', '').strip()

    is_correct = (user_answer.lower() == correct_answer.lower())

    session = request.session
    level = session.get('current_level', 'medium')

    if is_correct:
        session['score'] = session.get('score', 0) + 1
        if level == 'easy':
            session['current_level'] = 'medium'
        elif level == 'medium':
            session['current_level'] = 'hard'
    else:
        if level == 'hard':
            session['current_level'] = 'medium'
        elif level == 'medium':
            session['current_level'] = 'easy'
        # если easy и ошибка Ч остаЄтс€ easy

    session['questions_asked'] = session.get('questions_asked', 0) + 1

    if session['questions_asked'] >= 5:
        return render(request, 'test.html', {
            'result': {
                'score': session['score'],
                'total': 5
            }
        })

    return get_next_question_html(request)

def get_next_question_html(request):
    level = request.session.get('current_level', 'medium')
    try:
        resp = requests.get(f'http://quiz-service:8000/api/question/{level}/', timeout=5)
        if resp.status_code == 200:
            question = resp.json()
            # —охран€ем правильный ответ и ID в сессии
            request.session['current_question_id'] = question['id']
            request.session['current_correct_answer'] = question['correct_answer']
            return render(request, 'test.html', {'question': question})
        else:
            return render(request, 'test.html', {'error': 'No question found'})
    except Exception as e:
        return render(request, 'test.html', {'error': f'Error: {e}'})