from os import system  # Usefull to launch firefox
import sys  # Usefull for command line arguments


def main(path):
    # First step is to read the file
    with open(path, "r") as source:
        text = source.read()

    # If the text is too long, we have to split it between several requests.
    text_split = len(text) // 5000

    for i in range(text_split):
        part_text = text[i * 5000 : (i + 1) * 5000]
        send_request(part_text)

    # We also have to send the remainder
    part_text = text[text_split * 5000 :]
    return send_request(part_text)


def send_request(text):
    # Second step is to write the HTTP GET request
    base = "https://translate.google.com"
    info = "#view=home&op=translate&sl=en&tl=fr"
    request_string = (
        f"{base}/{info}&text={text}".replace(" ", "%20")
        .replace("\n", "%0A")
        .replace("\\", "\\\\")
        .replace("!", "\!")
        .replace('"', '\\"')
        .replace("'", "'")
    )

    # Debug
    # system(f"echo \"{request_string}\"")

    # Third step is to get the result
    return system(f'firefox "{request_string}" 2>/dev/null &')


if __name__ == "__main__":
    main(sys.argv[1])
