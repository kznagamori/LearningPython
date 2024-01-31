import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

def main():
    url = "https://api.github.com"
    data = fetch_data(url)
    print(data)

if __name__ == "__main__":
    main()
