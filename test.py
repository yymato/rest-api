from requests import get, post

print(get('http://localhost:5000/api/jobs').json(), 3 * '\n')  # Получение всех работ
print(get('http://localhost:5000/api/jobs/2').json(), 3 * '\n')  # Корректное получение одной работы
print(get('http://localhost:5000/api/jobs/999999').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — неверный id
print(get('http://localhost:5000/api/jobs/q').json(), 3 * '\n')  # Ошибочный запрос на получение одной работы — строка


print(post('http://localhost:5000/api/jobs', json={}).json(), 3 * '\n')
