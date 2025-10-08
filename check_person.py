# どのぐらいの信頼度で人がいると検知するか
REALPERSON = 0.80

def is_exist_person(detect_list):
    for detect in detect_list:
        if(detect[0] == "person" and detect[1] >= REALPERSON):
            return True
    return False