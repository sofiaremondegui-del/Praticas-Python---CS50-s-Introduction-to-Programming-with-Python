def main():
    name = input("What's your name? ").strip().title()
    first, last = name.split(" ")
    hello(first)

def hello(to = "world"):
    print(f"hello, {to}")

main()