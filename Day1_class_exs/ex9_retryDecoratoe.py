import time

def retry(func):
    def wrapper():
        for attempt in range(3):
            try:
                return func()
            except Exception as e:
                print("Error : ",e)
                if attempt < 2:
                    print("Retring in 2 seconds...")
                    time.sleep(2)
        print("All 3 attempts failed.")
    return wrapper


@retry
def connect_server():
    print("connecting to server....")
    raise Exception("server not responding")

connect_server()