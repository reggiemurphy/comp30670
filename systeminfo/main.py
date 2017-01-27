import platform


def main():
    print("Machine is:", platform.machine())
    print("Version is:", platform.version())
    print("Uname is:", platform.uname())
    print("System is:", platform.system())
    print("Processor is:", platform.processor())

if __name__ == '__main__':
    main()
