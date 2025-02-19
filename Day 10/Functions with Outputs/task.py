#pause 1
#function that takes the first and last name of someone
def format_name(f_name, l_name):
    title_f_name, title_l_name = title_turn(f_name=f_name, l_name=l_name)
    print(f"Hello, {title_f_name} {title_l_name}")


def title_turn(f_name, l_name):
    return f_name.title(), l_name.title()


format_name(f_name='leonardo', l_name='sousa')