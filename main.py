import this


def hello_python():
    zen = this.s.split('\n')
    print("Hello, Python!")
    print("Here's the Zen of Python:")
    for line in zen:
        print(line)


if __name__ == "__main__":
    hello_python()
