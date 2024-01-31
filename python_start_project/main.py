import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Python CLI Program")
    parser.add_argument('name', help='Your name')
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
