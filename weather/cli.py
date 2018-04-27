from weather import fetch_weather

__all__ = [
    'main',
]

CITY_PROMPT = 'Where are you? '

def main():
    while True:
        location = raw_input(CITY_PROMPT)
        print(fetch_weather(location))

if __name__ == '__main__':
    main()
