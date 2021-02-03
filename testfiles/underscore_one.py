def external():
    print("I am external")

def _internal():
    print("I am internal") 


if __name__ == "__main__":
    print(__name__)
    _internal()