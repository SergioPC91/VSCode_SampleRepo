import sys
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """
    greet
    """
    greeting = f"Hello, {who_to_greet}"
    return greeting


r = requests.get("https://coreyms.com", timeout=2)
print(r.status_code)
# print(greet("World"))
# print(greet("Corey"))
