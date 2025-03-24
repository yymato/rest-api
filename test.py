from requests import get, post, delete, put

# print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ
# print(get('http://localhost:5000/api/jobs/2').json(), 3 * '\n')  # Корректное получение одной работы
# print(get('http://localhost:5000/api/jobs/999999').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — неверный id
# print(get('http://localhost:5000/api/jobs/q').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — строка


# print(post('http://localhost:5000/api/jobs', json={}).json(), 3 * '\n')  # Пустой json
# print(post('http://localhost:5000/api/jobs', json={'job': '123'}).json(), 3 * '\n')  # Не все данные в json
# print(post('http://localhost:5000/api/jo', json={}).json(), 3 * '\n')  # Не корректная ссылка
# print(post('http://localhost:5000/api/jobs', json={
#
#                                                     'team_leader': 1,
#                                                     'job': 'test',
#                                                     'work_size': 20,
#                                                     'collaborators': '2, 3',
#                                                     'is_finished': False
#                                                 }).json(), 3 * '\n')  # правильный запрос
# print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ

# print(delete('http://localhost:5000/api/jobs/q').json(), 3 * '\n')  # Не корректный id
# print(delete('http://localhost:5000/api/jobs/999999999').json(), 3 * '\n')  # Не корректный id
# print(delete('http://localhost:5000/api/jobs/3').json(), 3 * '\n')  # правильный запрос
# print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ

# print(put('http://localhost:5000/api/jobs', json={'job': 'test2123123123213'}).json(), 3 * '\n')  # нет id в запросе
# print(put('http://localhost:5000/api/jobs', json={}).json(), 3 * '\n')  # пустой запрос
# print(put('http://localhost:5000/api/jobs', json={'id': 3, 'job': 'test2123123123213'}).json(), 3 * '\n')  # правильный запрос
#
# print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ