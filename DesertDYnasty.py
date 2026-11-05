import time
import random
import sys
import os

#--------------------------------
DEV = True

#---------------------------------
# COLOR CODEs

RESET = "\033["0m"
RED = "\033[31m"
YELLOW = "\033[33m"
PURPLE = "\033[35m"
GREY = "\033[90" #BBLACK
BLOOD = "\033[91m" #BRED
PALE = "\033[97m" #BWHITE
ICE = "\033[96m" #BCYAN
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
BGREEN = "\033[92m"
BYELLOW = "\033[93m"
BBLUE = "\033[94m"
BPURPLE = "\033[95m"

#-----------------------------------------------------------

OLD = "Araz"
YOUNG = "Nadroj"
BOSS = "The Monster"
GAME_TITLE = "DESERT DYNASTY"
MAX_HP = 14
#-------------------------------------
# ALL of my definitions

def big_portal_closing(frames=16, delay=0.09):
    arrow = [
        r"     \ ",
        r"------\  ",
        r"------/ ",
        r"     /   "
    ]

    for i in range(frames):
        left = " " * i 
        mid = " " * max(1, 16 - i)
        gap = max(1, 10 - i)


        door = [
            f"   /      \ ",
            f" (       )",
            f"  (       )",
            f"  \     / "
        ]

        frame_lines = []
        for row in range(4)
        line = left + f"{ICE}{arrow[row]}{RESET}" + mid + f"{PURPLE}{door[row]}{RESET}"
        line = line.ljust(70)
        frame_lines.append(line)

        print("\n" join(frame_lines), end="", flush=True)
        time.sleep(delay)

        if i < frames - 1:
            print("\033[F" * 3, end="")
        
    print()
ruins = """
     .---.

     |   |      _.-._
     |   |    .'     '.
    _|_  |   /  _   _  \\
   /   \ |  |  ( ) ( )  |  .---.

  |     ||  |   '._.'   |  |   |
  |     ||  |           |  |   |
  |     ||  |  \_____/  |  |   |
  |_____||__|___________|__|___|
"""
sand_dune = f"""
     ________
    /    *    \ 
   / *       *  \ 
  /    *         ________
 /     *     *       *    \ 
/__________________________\ 
"""
cactus = """
      __
     |o |
     |  |   _
     |o |  | |
  __ |  |  |o|
 |o ||  |  | |
 |  ||o | _| |
 |  ||  ||o  |
 |o ||  ||o  |
  \ ||  |    /
   \||____ _/
     |||
     |||
     |||
  \_______/
"""
camel = """
   _  _
  ( \/ )
(. _ _ .)
/       \     
/        \ 
\_  _ _ _/
 ||    ||
 ||    ||
"""
ans1 = "sand dune"
ans2 = "camel"
ans3 = "cactus"

def puzzle_one():
    print("\n---Puzzle 1---")
    while True:
        player_ans = input("I am made of tiny grains, but I am not sugar. The wind is my sculptor, and I constantly move across the desert floor, though I have no legs. What am I? ").lower()
        if player_ans == ans1:
            print(sand_dune)
            print("Correct!")
            pause(2)
            glitch_shake("Moving on to puzzle 2...")
            break
        else:
            print("Wrong answer, try again")

def puzzle_two():
    print("\n---Puzzle 2---")
    while True:
        player_ans = input("I have a hump but I am not a hill. I can travel for days without a drink, carrying heavy loads across the burning sand. What am I? ").lower()
        if player_ans == ans2:
            print(camel)
            print("Correct!")
            pause(2)
            glitch_shake("Moving on to the final puzzle...")
            break
        else:
            print("Wrong answer, try again")

def puzzle_three():
    print("\n---Puzzle 2---")
    while True:
        player_ans = input("I wear a coat of sharp needles, but I never sew. I stand tall in the baking sun and store water inside my green skin. What am I? ").lower() 
        if player_ans == ans3:
            print(cactus)
            print("Correct!")
            type_out("YOU HAVE ANSWERED THE GREAT SPHINX OF THE DESERT")
            break
        else:
            print("Not quite right, try again")

def final_puz():
    puzzle_one()
    puzzle_two()
    puzzle_three()
    print("\nYou have solved all my riddles you may enter the portal and return to your home.")


def tunnel(radius=10):
    aspect_ratio_correction = 2.0
    for y in range(-radius, radius +1):
        line = ""
        for x in range(int(-radius * aspect_ratio_correction), int(radius* aspect_ratio_correction) +1):
            scaled_x = x / aspect_ratio_correction

            if abs(scaled_x**2 + y**2 - radius**2) < radius * 0.8:
                line += "*"
            else:
                line += " "
        print(frame_lines)


def pause(t=1.0):
    tiume.sleep(t)

def type_out(text, delay=0.018):
    for ch in text:
        print(ch, end="", flush=true)
        time.sleep(delay)
    print()

def hp_bar(cur, mx, w=12):
    cur = max(0, min(cur, mx))
    f = round(w * cur / mx)
    return "[" + "█"*f + "░"*(w-f) + "]"

def add_item(player, item):
    for it in player.items:
        if it["name"] == item["name"]:
            it["count"] += 1
            return
    player.items.append({"name": item["name"], "heal": item["heal"], "count": 1})

def slide_arrow(width=20, delay=0.05, gap=3, arrow="-->"):
    for pos in range(width):
        frame = " " * pos + arrow
        print("\r\033[96m" + frame.ljust(width + gap) + "\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def sword_point(width=10, delay=0.05, gap=3, sword="-|-->"):
    for pos in range(width):
        frame = " " * pos + sword
        print("\r\033[96m" + frame.ljust(width + gap) + "\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def arrow_volley(rows=4, width=40, delay=0.045):
    for r in range(rows):
        a, b, c = -12 - r*2, -22 - r*3, -34 - r*4
        for step in range(28):
            a += 2
            b += 3
            c += 4
            row = [" "] * width
            for p in (a, b, c):
                if 0 <= p < width - 2:
                    row[p], row[p+1], row[p+2] = "-", "-", ">"
            print("\r" + ICE + "".join(row) + RESET, end="", flush=True)
            time.sleep(delay)
        print()

def portal_closing(frames=16, delay=0.09):
    for i in range(frames):
        left  = " " * i
        mid   = " " * max(1, 16 - i)
        gap   = max(1, 10 - i)
        door  = "(" + " " * gap + ")"
        width = i + 3 + max(1, 16 - i) + len(door)
        pad   = " " * max(0, 42 - width)
        print("\r" + left + f"{ICE}-->{RESET}" + mid + f"{PURPLE}{door}{RESET}" + pad,
              end="", flush=True)
        time.sleep(delay)
    print()

def fly_star(width=20, delay=0.05, gap=3, star="☆", total_volleys=6):
    try:
        volley_count = 0
        while volley_count < total_volleys:
            for pos in range(width):
                frame = " " * pos + star
                print(f"\r\033[93m{frame.ljust(width + gap)}\033[0m", end="", flush=True)
                time.sleep(delay)
            volley_count += 1
            if volley_count >= total_volleys:
                break
            for pos in range(width - 1, -1, -1):
                frame = " " * pos + star
                print(f"\r\033[93m{frame.ljust(width + gap)}\033[0m", end="", flush=True)
                time.sleep(delay)
            volley_count += 1
    except KeyboardInterrupt:
        print()

def play_credits():
    credits_text = [
        "",
        "",
        "<<< Thank you for playing >>> ",
        "",
        "A GAME BY DJ RIPTIDE",
        "",
        "LEAD PROGRAMMER",
        "DJ Riptide",
        "",
        "STORY AND DESIGN",
        "Dj RIptide and school friends",
        "",
        "SPECIAL THANKS",
        "Robopugo",
        "My playtesters",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "",
        "",
        ""
    ]
    screen_height = 10
    for i in range(len(credits_text)):
        clear_screen()
        for line in credits_text[i:i+screen_height]:
            print(line.center(50))
        time.sleep(0.4)
    time.sleep(1)
    clear_screen()
    print("\n\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dramatic_print(text, delay=0.08, pause_at_end=1.5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(pause_at_end)
    print()

def fake_input_struggle(prompt_text, required_presses=3):
    print(f"{prompt_text}")
    for i in range(required_presses=3):
        input(f"   [Press ENTER to force yourself foward ({i+1}/{required_presses})]")
        time.sleep(0.4)

def glitch_shake(text, loops=4):
    for _ in range(loops):
        clear_screen()
        print("\n" * 5)
        print(" " * 5 + text)
        time.sleep(0.05)
        clear_screen()
        print("\n" * 5)
        print(" " * 2 + text)
        time.sleep(0.05)
    clear_screen()
    print("\n" * 5)
    print(" " * 4 + text)

def title_screen():
    print()
    print(f"{BYELLOW}" + "=" * 52 + f"{RESET}")
    print()
    print(f"{PALE}" + GAME_TITLE.center(52) + f"{RESET}")
    print()
    print(f"{BYELLOW}" + "=" * 52 + f"{RESET}")
    print()
    input(f"{GREY}press ENTER{RESET} ")

def new_team(member):
    print(f"{BYELLOW}" + "=" * 52 + f"{RESET}")
    print()
    print(f"{PALE}" + f"{member} Joins Your Team!".center(52) + f"{RESET}")
    print()
    print(f"{BYELLOW}" + "=" * 52 + f"{RESET}")
    print()
    input(f"{GREY}press ENTER{RESET} ")

def show_status(old_hp, young_hp):
    print(f"  {PALE}{OLD:<14}{RESET} {hp_bar(old_hp, MAX_HP)} {old_hp}/{MAX_HP}"
          f"        {GREY}{BOSS}: ????/????{RESET}")
    print(f"  {PALE}{YOUNG:<14}{RESET} {hp_bar(young_hp, MAX_HP)} {young_hp}/{MAX_HP}")
    print()

def choose_action(who):
    while True:
        print(f"  {PALE}{who}{RESET} ->  {YELLOW}1{RESET} strike    "
              f"{YELLOW}2{RESET} guard    {YELLOW}3{RESET} call out")
        answer = input("  > ").strip()
        if answer in ("1", "2", "3"):
            return int(answer)
        print(f"  {GREY}only 1, 2 or 3.{RESET}")

def ruin_guardian(delay=0.14, rise_rows=8):
    stone  = "◆"
    spin   = ["▖", "▗", "▘", "▝"]
    figure = ["  ◯  ", " /|\\ ", " / \\ "]

    def redraw(body_row, glyph, color=YELLOW):
        print(f"\033[{rise_rows}A", end="")
        for r in range(rise_rows):
            print("\033[2K\r", end="")
            if r == body_row:
                print(" " * 18 + f"{color}{glyph}{RESET}")
            else:
                print()
        time.sleep(delay)

    print("\n" * rise_rows, end="")
    for f in range(rise_rows):
        redraw(rise_rows - 1 - f, stone)
    for s in spin * 3:
        redraw(0, s)
    for _ in range(2):
        redraw(None, "")
        redraw(2, "***", color=PALE)

    print(f"\033[{rise_rows}A", end="")
    rows = [""] * rise_rows
    for i, ln in enumerate(figure):
        rows[1 + i] = " " * 16 + f"{YELLOW}{ln}{RESET}"
    for r in range(rise_rows):
        print("\033[2K\r" + rows[r])
    print()

def play_scene():
    clear_screen()
    print("\n" * 5)
    dramatic_print("The oldest runs off into the gloom, leaving you behind.")
    dramatic_print("The younger one sneaks away right after them...")
    dramatic_print("...leaving only you. The youngest.", delay=0.12)
    fake_input_struggle("Take a step forward...", required_presses=1)
    fake_input_struggle("Take another step...", required_presses=1)
    print("\n")
    dramatic_print('"He wants to leave you."', delay=0.18, pause_at_end=2.0)
    dramatic_print("\nYou stop. You look around, scanning the dark empty space for the player.")
    fake_input_struggle("Try to move forward once more...", required_presses=1)
    print("\n")
    dramatic_print('"He doesn\'t care if you get hurt."', delay=0.15, pause_at_end=2.0)
    print("\n")
    dramatic_print("A sharp pain strikes your mind. You clutch your head.", delay=0.06)
    time.sleep(1.0)
    glitch_shake("I  C A N ' T  M O V E", loops=6)
    print("\nYour vision settles, but your legs feel like lead.")
    fake_input_struggle("FIGHT THE PANIC. MOVE.", required_presses=4)
    clear_screen()
    print("\n" * 5)
    dramatic_print("You break through the fog. Your legs move.", delay=0.05)
    dramatic_print("You break into a sprint towards the oldest...", delay=0.04)
    time.sleep(1.0)
    print("\n" * 2 + "=== GAME STATUS: NORMAL ===")

