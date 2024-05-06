import pyshorteners

def generate_short_url(long_url):
    # Initialize the URL shortener
    s = pyshorteners.Shortener()

    # Shorten the URL
    short_url = s.tinyurl.short(long_url)

    return short_url

if __name__ == "__main__":
    long_url = input("Enter the long URL: ")
    short_url = generate_short_url(long_url)
    print("Short URL:", short_url)
