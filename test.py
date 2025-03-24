from requests import get, post

# print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ
# print(get('http://localhost:5000/api/jobs/2').json(), 3 * '\n')  # Корректное получение одной работы
# print(get('http://localhost:5000/api/jobs/999999').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — неверный id
# print(get('http://localhost:5000/api/jobs/q').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — строка


print(post('http://localhost:5000/api/jobs', json={}).json(), 3 * '\n')  # Пустой json
print(post('http://localhost:5000/api/jobs', json={'job': '123'}).json(), 3 * '\n')  # Не все данные в json
print(post('http://localhost:5000/api/jo', json={}).json(), 3 * '\n')  # Не корректная ссылка
print(post('http://localhost:5000/api/jobs', json={
                                                    'team_leader': 1,
                                                    'job': 'test',
                                                    'work_size': 20,
                                                    'collaborators': '2, 3',
                                                    'is_finished': False
                                                }).json(), 3 * '\n')  # правильный запрос

print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ