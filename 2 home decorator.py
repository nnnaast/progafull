import functools

users = {
    'alice': {'role': 'admin'},
    'bob': {'role': 'user'},
    'eve': {'role': 'guest'}
}

def require_role(required_role):
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_data = kwargs.get('user')
            
            if user_data is None:
                raise ValueError("Аргумент 'user' не передан в функцию")
            
            if user_data.get('role') == required_role:
                return func(*args, **kwargs)
            else:
                return f"Доступ запрещен. Требуется роль: {required_role}"
        
        return wrapper
    
    return decorator

@require_role('admin')
def delete_database(db_name, user=None):
    return f"База {db_name} удалена!"

current_user = 'bob'
result = delete_database('test_db', user=users[current_user])
print(result)

current_user = 'alice'
result = delete_database('test_db', user=users[current_user])
print(result)
