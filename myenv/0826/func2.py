class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

def handle_user_login(event_data):
    return f"로그인 처리: 사용자 {event_data}"

def handle_user_logout(event_data):
    return f"로그아웃 처리: 사용자 {event_data}"

def handle_data_update(event_data):
    return f"로그인 처리: 사용자 {event_data}"

events = [
    Event("LOGIN",{"username":"Alice"}),
    Event("UPDATE",{"field":"email","value":"alice@example.com"}),
    Event("LOGOUT",{"username":"Alice"}),
    Event("UNKNOWN",{"data":"some data"})

]


event_handlers = {
    "LOGIN":handle_user_login,
    "LOGOUT":handle_user_logout,
    "UPDATE":handle_data_update
}

def process_event(event, handlers):
    if event.type in handlers:
        return handlers[event.type](event.data)
    return f"처리되지 않은 이벤트 탕입:"




result = list(map(lambda event:process_event(event,event_handlers), events))
for results in result: 
    print(result)