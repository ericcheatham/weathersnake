import argparse

from weather import fetch_weather


__all__ = [
    'main',
]

CITY_PROMPT = 'Where are you? '
REPORT_FORMAT = '{} weather:\n {} degrees {}'

UNITS = {
    'metric': 'Celsius',
    'imperial': 'Fahrenheit',
    'kelvin': 'Kelvin'
}


def get_arg_parser():
    """
    Command arguments
    """
    parser = argparse.ArgumentParser(
        prog='weather',
        description='Python based temperature app'
    )

    parser.add_argument(
        '--format',
        choices=['metric', 'kelvin', 'imperial']
    )

    return parser


def main():
    """
    Command line entrypoint
    """
    parser = get_arg_parser()

    args = parser.parse_args()

    print('Find out the current temperature. Enter "quit" to quit\n')
    try:
        while True:
            location = raw_input(CITY_PROMPT)
            weather = fetch_weather(location, args.format)

            if location.lower() == 'quit':
                break

            if not weather:
                print('Input location as "<CITY>,<STATE/COUNTRY>"')
                continue

            if weather[0] != 200:
                print('Unable to determine weather in {}'.format(location))
            else:
                temp = weather[1]['main']['temp']
                unit = UNITS[args.format or 'imperial']
                print(REPORT_FORMAT.format(location, temp, unit))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
