def banner_text(text):
    screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError('String {} is larger specifiend widty {}'
                         .format(text, screen_width))

    if text == '*':
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width))
        print(output_string)