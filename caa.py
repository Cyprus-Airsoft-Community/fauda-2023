import time
import datetime
import os
import keyboard


def ascii_logo():
    caa_logo = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GP5#@@B~~?JJY&&YJ77JYP&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@&@Y~~Y5: !@@B  !YJG@&@G  J#B&&&&@&5PB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@&B5JJB@@5  YG!.~#@&J?B@@@@@@B7!#@@@&&@&! .YJ7JB@&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@G: !?^.J@@YJ5GB##BGPP5YJJJJYY5PGB#&&@@@G^^?J!  P@@#B&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#5JB@&Y777!JG@#B5J!^:.                 .^!?YG#&@#7^5@@P..75B&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&GJJ! .G&@GG##P?^.    .:^~~!!^:.  ..:~!!~^:.    .^7YB&@@Y77~~77P@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&J .??7!5&&GJ^.    .!7?JJJJJJJJJ?  !JJJJJJJJJ?7!:     :7P##57.:G@&G5#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&B&@&5:.5@@B?:      .~JJJ?7!!!!~7JJ?  7JJ?~~!!!7?JJJ!:      .7G&##&GP: 7Y#@@@@@@@@@@@@@
@@@@@@@@@@@@&J :JB@&&&5~   .::^~7??!~!7J5G#&G!~J?  7J!~5&#G5J?!~!7?7!^:::   ^Y#@57J~!?7#@@@@@@@@@@@@
@@@@@@@@@@&&@&G!.?@&Y:  .~7JJJJ7~!?5B&@@@GY?7~ .~  ~: ^!7JP@@@&BPJ!~!?JJJ?~.  .?#&Y^.Y@@@&@@@@@@@@@@
@@@@@@@@@G^:75#@&@P^  .~?JJJ7~~!DISTANCE#.                 ?P#&@@@&BY!~7JJJJ!:  .J&&&&GJ~:5@@@@@@@@@
@@@@@@@@5~P~..5@#!   ~?JJJ!^7P&@@@&G?~.                      .^7P#@@@&G?^!JJJJ!.  ^G@#: 757?&@@@@@@@
@@@@@&@5 :!:G&@P.   :JJJ7^7B@@@@G?:                              .!P&@@@#J^!JJJ~    J@#~Y5~ 7@&@@@@@
@@@@&&@#G?^~#@J     !J?^~G@@@&P~                                    ^Y&@@@#7^?J?.    !&&7:!YB@@&@@@@
@@@@&&&@@@&&@?    .!J7:J&@@@G~                                        :5@@@@5:!J7.    ~&@&&&B55&&@@@
@@@&&&@@@&&@J   :~?J7:P@@@&?                                            !#@&@B^~JJ!:   !&@?..:.5@&@@
@@&@7PJ7J&@P   ~JJJ7.G@&@#~                                              :G@&@#^~JJJ7   ?@G.P&5.#@@@
@@@P:Y:^^&&:  ^JJJ?.5@@@#^                                                .G@@@B.7JJJ!   G@J.YP:5@&@
@&@7 .5~5@Y   ?JJJ^7@@G!^                                                  .!Y@@5.?JJJ:  !@&PB@&@@&@
@&@&#B&5&&^  ^JJJ? P@&^         ...:::::::::.                                 B@B.!JJJ!   B@P7!!^P@@
@@BY555#@B   :JJJJ7~7?      ^?5BBBBGLASSES##5    ^PG^            ~G5:         !?~!?JJJ~   Y@P!7?JG@&
&@5^^^ J@P    ^?????7~:   7B@@P?~^::::::::::.  .J&@@&Y.        :5@@@#?.      .~7?J???!    ?@@###&&&&
&@#GGG^Y@5     ......:.  !@@&!                7B@&YJ&@#?     .?&@&J5@@B!     .:......     7@#:...!@&
&@Y.::.P@P    ^?????7~:  ^#@@J.             ^P@@G~  !#@@G~  !B@@5: .?&@@P^   .~7?????~    ?@&G:PJ~@&
@&&&&&&@@B   :?JJJ?~!7    :Y#@&PJ?7!!!!!!!!5@@#7   .^?G&sa@@5P@@G~   .~YB&@&Y.  ~7~7JJJJ^   Y@P: ^.@
@&&PJ?5?&&^  ^JJJ?.5@&:     .^7Y5PGGGGGGGGGGGJ.        .JOULES         :YPGY. B@G.!JJJ!   B@#5555B@@
@&@~:! 7&@J  .?JJJ:?@@5^.                                                  .^J@@P.?JJJ:  ~@@@@@&P&&@
@@@5^5.7J&#:  ^JJJ?.G@@@B:                                                 P@@@#:!JJJ!   P@Y^!?!!@&@
@@@&~:~!?&@5   !JJJ!:B@&@B^                                              .P@&@&~^JJJ?.  7@@GJ?^ B@@@
@@@@&&@&#@@@?   ^!JJ!:G@&@#!                                            ^B@&@#~^JJ7^.  ^&@&@@@YJ@&@@
@@@&@#!:.J@@@7    .7J7:5@@@@5:                                        .J&@@@G^~J?:    ^#@?:7YG&@&@@@
@@@@@&7:G~?Y#@7     7J?^7B@@@&Y:                                    .?#@@@&?:7J?.    ~#@@PJ!:~&@@@@@
@@@@@@@?^. :Y@@Y    :JJJ!^J#@@@&5!.                               ~Y#@@@&Y^~JJJ~    7&&??B@@&&@@@@@@
@@@@@@@&Y5#@&&@@B^   !JJJJ!^?B@@@@#57:                        :!YB@@@@#J~~?JJJ7.  :5@G!!: :G@@@@@@@@
@@@@@@@@@@B7:~YJB&Y.  :!JJJJ!~!YB@@@@&B5?                  !YG&@@@@#P7~!?JJJ7:   7#@J 7#G:J&@@@@@@@@
@@@@@@@@@@B!7P~ ?@@#?.  .!?JJJ?!~!JG#@@@@57!~^ .~  ^: :~~7Y@@@@&GY7~!?JJJ?!:   !B@@@5!. ~G@@@@@@@@@@
@@@@@@@@@@@@@P^ !&@&@&Y:  .:^^~!??7!~7?5G#&&B!^??  7J~~G@&#G5J7~~!??7~^^^.  .?B@#!!B@@#G&@@@@@@@@@@@
@@@@@@@@@@@@@#Y5#&&?^JB&P!.      :!JJ?77!!!!^!JJ?  7JJ7^!!!!!7?JJ7^.      ~Y#&GP5^  ?&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@?^YBG!~P@#57:     :7?JJJJJJJJJJ?  7JJJJJJJJJJ?7^     .~YB@@#^  !JJYB&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&P7J7 .SAFETY#J!:    .:^~!!77~^.  .:^!77!~^:.    :~?P#@@@@&@#J:!&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@BJ?B@&&BB&@@@&BPJ!^:.                   .^!?5G#@@@@#PP#&&@@#&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&@B55#@&&@@@@@@&#BP5YJJ??77???JY5PGB&&@@&@@&&&@#GG#@&&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&#55#&@@@@@@@@@@@@@@@@&@@@@@@&BY5#@&&&&@@&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@&BB&@&&&&BY5#&&&&&@#5YB&&&&&@&##&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@&BB&@&&&&&&#&&@&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Proudly presented by n u t r o n `.
"""
    print_timer(caa_logo)
    print(
        """\nFind the hidden words in the image above. Prioritise the words based on their importance and type them one-by-one, then hit Enter.
        \nΒρείτε τις κρυμμένες λέξεις στην παραπάνω εικόνα. Πληκτρολογήστε τις όλες μία προς μία με βάση τη σημαντικότητα τους και πατήστε Enter.\n""")

    print("Answer: / Απάντηση:")


def print_timer(object):
    # delay = 0
    delay = 0.0001
    for char in object:
        print(char, end="", flush=True)
        time.sleep(delay)


def user_input_two():
    words = ['safety', 'glasses', 'distance', 'joules']
    removed_words = []
    while words:
        user_input = input().strip().lower()
        if not user_input:
            continue
        if len(user_input.split()) > 1:
            print(
                '\nEnter only one word at a time.\nΕισαγάγετε μόνο μία λέξη κάθε φορά.\n')
        elif user_input in words[1:]:
            print(
                f'The word "{user_input}" is in the list, but not in the correct priority. Try again.\nΗ λέξη "{user_input}" βρίσκεται στη λίστα, αλλά όχι στη σωστή προτεραιότητα. Προσπαθησε ξανα.\n')
        elif user_input == words[0]:
            print(
                f'\nCongratulations! You have entered the correct word {words[0]}!\nΣυγχαρητήρια! Έχετε εισαγάγει τη σωστή λέξη {words[0]}!\n')
            removed_words.append(words[0])
            words.pop(0)
        elif user_input in removed_words:
            print(
                f'\nThe word {user_input} has already been input. Try again.\nΗ λέξη {user_input} έχει ήδη εισαχθεί. Προσπάθησε ξανά.\n')
        elif user_input not in words:
            print(
                f'\nThe word {user_input} is not in the list. Try again.\nΗ λέξη {user_input} δεν βρίσκεται στη λίστα. Προσπάθησε ξανά.\n')

        else:
            print(
                '\nSomething went wrong. Τry again.\nΚάτι πήγε στραβά. Δοκιμάστε ξανά.\n')


"""
def user_input():
    words = ["glasses", "safety", "distance", "joules"]
    correct_order = "safetyglassesdistancejoules"

    loop_value = True
    while loop_value == True:
        try:
            user_input = input()
            user_string = user_input.replace(" ", "").lower()

            if user_string == correct_order:
                print(
                    "\nCongratulations! You have entered the correct order.\n Συγχαρητήρια! Έχετε εισαγάγει τη σωστή σειρά.\n")
                loop_value = False

            elif not all(word in words for word in user_input.split()):
                print(
                    "\nSorry, you entered words that are not in the list. Please try again.\nΛυπούμαστε, εισαγάγατε λέξεις που δεν είναι σωστές. Προσπάθησε ξανά.")
            elif not all(word in user_input.split() for word in words):
                print(
                    "\nSorry, you are missing words. Please try again.\nΣου λείπουν λέξεις. Προσπάθησε ξανά.")
            else:
                print("\nSorry, the order you entered is incorrect. Please try again.\nH σειρά που εισαγάγατε είναι λανθασμένη. Προσπάθησε ξανα.")

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit()
        except:
            ("\nSorry, something went wrong. Please try again.\n")
            break
"""


def progress_bar():
    player_name = input("\nWhat is your name? / Πως σε λένε; ")

    while len(player_name) < 3:
        print("\nYour name must be at least 3 letters long.\nΤο όνομά σας πρέπει να αποτελείται από τουλάχιστον 3 γράμματα.")
        player_name = input("\nWhat is your name? / Πως σε λένε; ")

    print("Hacking. . .")

    # duration = 6
    duration = 600

    spinner = ["|", "/", "-", "\\"]

    for i in range(duration):
        spin_char = spinner[i % len(spinner)]
        pct_complete = ((i + 1) / duration) * 100
        progress_bar = f"[{'#' * int(pct_complete / 2)}{'-' * int((100 - pct_complete) / 2)}] {pct_complete:.1f}% {spin_char}"
        print(progress_bar, end='\r')
        time.sleep(1)

    output_file(player_name)


def output_file(player_name):
    name = caesar_cipher(player_name)
    verification_string = mix_date(name)

    desktop_path = os.path.join(os.path.expanduser(
        "~"), "Desktop")    # Outputs a textfile
    output_file_path = os.path.join(desktop_path, "fauda.txt")
    with open(output_file_path, "w", encoding='utf-8') as f:
        f.write(
            f"Transfer thε file FAUDA.TXT to your USB and move the USB to MISSIONS. \n\n{verification_string}\n\nΜετακινήστε το αρχείο FAUDA.TXT στο USB σας και μεταφέρετε το USB στο MISSIONS.")
        f.close


def caesar_cipher(player_name):
    result = ""
    for char in player_name:
        if char.isalpha():
            new_char_code = (ord(char) - 97 + 1) % 26 + 97
            new_char = chr(new_char_code)
        else:
            new_char = char
        result += new_char
    return result


def mix_date(s):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    date_chars = list(now)
    result = ""
    for i, char in enumerate(s):
        result += char
        if i < len(s) - 1:
            result += date_chars[i % len(date_chars)]
    return result


def app_finish():
    print("""
   Close the application, and transfer thε file FAUDA.TXT from your Desktop to your USB and move the USB to MISSIONS.
   \n
   Κλείστε το πρόγραμμα, και μετακινήστε το αρχείο FAUDA.TXT από το Desktop στο USB σας και μεταφέρετε το USB στο MISSIONS.
   """)


def fullscreen():
    keyboard.press('alt')
    keyboard.press('enter')
    keyboard.release('alt')
    keyboard.release('enter')


if __name__ == "__main__":
    fullscreen()
    ascii_logo()
    user_input_two()
    # user_input()
    progress_bar()
    app_finish()
    time.sleep(5)
    fullscreen()
    time.sleep(5)
    quit()
