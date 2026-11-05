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
    _|_  |   /  _   _  \ 
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

# now for the super evil bad guy to come. nwo that i think abotu it while retyping this i severly dont remember if i named this guy.
# ehhh sucks to suck
def scene_square():
    print()
    print(f"{GREY}- THE SQUARE -{RESET}")


    print("\033[35m DAY:SATURDAY \033[0m")
    print("\033[91m CRASH \033[0m")


    print(f"{BBLUE}Araz: What the heck was that?{RESET}")
    print(f"{BBLUE}Araz: Cmon lil bro lets go check it out{RESET}")


    print(f"{BBLUE}Araz: Come on, this way{RESET}")
    time.sleep(1)


    slide_arrow()


    print(f"{BBLUE}Araz: woah!{RESET}")
    print("He moves you out of the way, you narrowly dodge the spear")
    time.sleep(1)
    msg = input("What do you want to say (1/2)")
    if msg in ("one", "1"):
        print(f"{BBLUE}nadroj: Who are you, what do you want from us?{RESET}")
    else:
        print("What the heck dude?!")


    time.sleep(1)


    slide_arrow()
    print("You dodge again it seems this monster doesn't want to talk")
    print("Time to fight")


    pause(1.2)
    print("There is something at the far end, where the road turns.")
    print("It is shaped like a man.")
    print("Your eyes keep sliding off it.")
    pause(1.8)


    print()
    print(f"{BLOOD}{BOSS} moves.{RESET}")
    slide_arrow()
    pause(0.5)
    print("A spear is in the air.")
    pause(0.4)
    print(f"It is not aimed at you. It is aimed at {YOUNG}.")


    pause(0.8)
    print(f"{YOUNG}: ...")
    pause(0.6)
    print(f"{OLD}: Behind me. stay behind me.")
    pause(1.8)


    print()
    print(f"{GREY}- you are both of them now -{RESET}")
    pause(1)
    print("Each round you pick one action for each brother.")
    print(f"  {YELLOW}1{RESET}  strike     swing at the shape")
    print(f"  {YELLOW}2{RESET}  guard      take the hit on your guard - half damage")
    print(f"  {YELLOW}3{RESET}  call out   warn your brother - he guards for you")
    pause(2)
    print(f"{GREY}3 is the one that matters. they only last this long because they cover each other.{RESET}")
    pause(2)


    old_hp   = MAX_HP
    young_hp = MAX_HP
    round_no = 0


    BOSS_ATTACKS = [
        "A fist that is not a fist comes down like a dropped anvil",
        "It is beside you. it was not beside you a moment ago",
        "The air folds and something goes through it, fast",
        "A sound like a struck bell, and the flagstones jump",
    ]


    while young_hp > 1:
        round_no += 1
        print(f"{GREY}- round {round_no} -{RESET}")
        show_status(old_hp, young_hp)


        a_old   = choose_action(OLD)
        a_young = choose_action(YOUNG)
        print()


        if a_old == 1:
            print(f"  {OLD} Swings. the blade crosses the monster and comes out clean.")
            print(f"  {GREY}There is nothing there to cut.{RESET}")
        elif a_old == 2:
            print(f"  {OLD} Plants his feet and puts up his guard.")
        else:
            print(f"  {OLD} Shouts - {YOUNG} has time to get his guard up.")


        if a_young == 1:
            print(f"  {YOUNG} Swings, low and fast. it goes through the monster like smoke.")
            print(f"  {GREY}The monster does not move.{RESET}")
        elif a_young == 2:
            print(f"  {YOUNG} Plants his feet and puts up his guard.")
        else:
            print(f"  {YOUNG} Shouts - {OLD} hears him and braces.")


        guarded = set()
        if a_old == 2:
            guarded.add("old")
        if a_young == 2:
            guarded.add("young")
        if a_old == 3:
            guarded.add("young")
        if a_young == 3:
            guarded.add("old")


        pause(0.8)
        print()
        print(f"  {BLOOD}{BOSS}{RESET} - {random.choice(BOSS_ATTACKS)}.")
        pause(0.8)


        base = random.randint(3, 5) + round_no // 2


        dmg = base + 2
        if "old" in guarded:
            dmg = max(1, dmg // 2)
        old_hp = max(1, old_hp - dmg)
        print(f"  it catches {OLD}. {BLOOD}-{dmg}{RESET}"
              + ("   (on his guard)" if "old" in guarded else ""))
        if old_hp == 1:
            print(f"  {GREY}He is still on his feet. He is always still on his feet.{RESET}")


        dmg = base
        if "young" in guarded:
            dmg = max(1, dmg // 2)
        young_hp = max(1, young_hp - dmg)
        print(f"  it catches {YOUNG}. {BLOOD}-{dmg}{RESET}"
              + ("   (on his guard)" if "young" in guarded else ""))
        print()
        pause(0.6)


        if round_no == 2:
            print(f"{GREY}  the blades are not doing anything.{RESET}")
            pause(2)


    print(f"{GREY}- 1 HP -{RESET}")
    show_status(old_hp, young_hp)
    pause(1.5)


    print(f"{BLOOD}{BOSS} stops.{RESET}")
    pause(1.5)
    print("it was never fighting them. it was waiting for one of them to be slow.")
    pause(1.8)


    print()
    type_out(f"it takes {OLD} by the throat and lifts him off the stones.", 0.02)
    pause(1)
    print(f"{OLD}'s feet leave the ground. he does not make a sound.")
    pause(1.5)
    print(f"{YOUNG} is face down on the flagstones behind them. one hit left in him.")
    pause(1.8)


    print()
    print(f"{PURPLE}the air opens in twelve places.{RESET}")
    pause(1)
    print("arrows. not thrown - summoned. hanging in a ring around the square,")
    print("all of them turned inward.")
    pause(1.5)
    print()
    arrow_volley(rows=4)
    print(f"{BLOOD}every one of them lands.{RESET}")
    pause(1.5)
    print(f"{OLD} is held up in the air with nowhere to go.")
    pause(2)


    print()
    print(f"{GREY}   .   .   .{RESET}")
    pause(2.5)
    print(f"{YOUNG} opens his eyes.")
    pause(1)
    print("the stones are warm. the square is loud.")
    pause(1.2)
    type_out("he gets an elbow under himself. then a knee. then he is up.", 0.02)
    pause(1.5)


    print()
    print("the spear is still in the flagstones. ten paces away, where it landed beside him.")
    pause(1.5)
    print(f"{YOUNG} looks at it. then at his brother in the air. then at it again.")
    pause(1.5)
    print(f"{YOUNG}: ...okay.")
    pause(1.5)


    print()
    print(f"{YOUNG} crosses the square.")
    pause(1)
    print(f"{BOSS} does not turn around. it is busy.")
    pause(1)
    type_out("he takes the spear in both hands and puts it through the shape's back.", 0.02)
    pause(1.5)


    print()
    print(f"{BLOOD}the arrows stop.{RESET}")
    pause(1)
    print("all twelve of them at once, like a held breath let go.")
    pause(1.2)
    print(f"{OLD} drops to the stones.")
    pause(1.8)


    print()
    print("the shape goes still.")
    pause(1)
    print("then it starts to leak.")
    pause(1.2)
    print(f"{PURPLE}blot{RESET} - thick, black, wrong - running out of the wound and down its legs.")
    pause(1.5)
    print("it pools at its feet.")
    print("the pool spreads.")
    print("the pool is not a pool any more.")
    pause(1.8)


    print()
    print(f"{PURPLE}it stands up out of the floor as a portal.{RESET}")
    pause(1.2)
    print("nothing behind it. the square, seen through something that is not air.")
    pause(1.8)


    print()
    print(f"{BOSS} throws {OLD} aside like it is finished with him.")
    pause(1)
    print(f"{OLD} hits the ground and stays there.")
    pause(1.2)
    type_out(f"it turns, takes {YOUNG} by the back of the neck, and walks him into the doorway.", 0.02)
    pause(1.5)
    print(f"{YOUNG}: brother-")
    pause(1)
    print("gone.")
    pause(1.5)
    print("then the monster steps through after him.")
    pause(2)


    print()
    print(f"{OLD} is on his hands and knees in the middle of the square.")
    pause(1.2)
    print("the doorway is still standing open.")
    pause(1)
    print("it is already smaller than it was.")
    pause(1.5)


    print()
    portal_closing()
    print()
    input(f"{ICE}[ ENTER ]{RESET} ")


    print()
    print(f"{OLD} gets up.")
    pause(0.8)
    print("he runs.")
    pause(0.8)
    type_out("he goes through the portal shoulder first, and it takes him.", 0.02)
    pause(2)


    print()
    print(f"{ICE}the portal closes on itself.{RESET}")
    pause(1.5)
    print("no light. no sound. no seam in the stones where it was.")
    pause(2)
    print("the square is empty.")
    pause(2.5)


    title_screen()


