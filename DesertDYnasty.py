import time
import random
import sys
import os

#--------------------------------
DEV = True

#---------------------------------
# COLOR CODEs

RESET = "\033[0m"
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
        for row in range(4):
            line = left + f"{ICE}{arrow[row]}{RESET}" + mid + f"{PURPLE}{door[row]}{RESET}"
            line = line.ljust(70)
            frame_lines.append(line)

            print("\n", join(frame_lines), end="", flush=True)
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

# finally omg.......... ANYWAY PLAYER TIME

class player:
    def __init__(self,name, HP=30):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.items = [{"name": "coconut water", "heal": 8, "count": 2}]
        self.gold = 0
        self.small_defeated = 0
        self.friends = []
        self._guarding = False

    def heal(self, n):
        self.hp = min(self.max_hp, self.hp + n)

class Player2:
    def __init__(self, name, hp=30):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.items = [{"name": "coconut water", "heal": 8, "count": 2},
                      {"name": "ice pop", "heal": 8, "count": 2},
                      {"name": "Super Tea", "heal": 15, "count": 1}]
        self.gold = 0
        self.small_defeated = 0
        self.friends = []
        self._guarding = False

    def heal(self, n):
        self.hp = min(self.max_hp, self.hp + n)

# done with players.... its not alot but tis alot when your doing everyhting over again..........

class Creature:
    def __init__(self, name, hp, attacks, is_boss=False,
                 can_spare=False, spare_threshold=0.25, reward=None, gold=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attacks = attacks
        self.is_boss = is_boss
        self.can_spare = can_spare
        self.spare_threshold = spare_threshold
        self.reward = reward
        self.gold = gold

def battle(player, enemy):
    print(f"\n{BLOOD}--- {enemy.name} ---{RESET}")
    pause(1)
    player._guarding = False
    while enemy.hp > 0 and player.hp > 0:
        print(f"  {PALE}{player.name:<12}{RESET} {hp_bar(player.hp, player.max_hp)} {player.hp}/{player.max_hp}")
        print(f"  {BLOOD}{enemy.name:<12}{RESET} {hp_bar(enemy.hp, enemy.max_hp)} {enemy.hp}/{enemy.max_hp}")
        print()

        spare_open = enemy.can_spare and enemy.hp <= enemy.max_hp * enemy.spare_threshold
        menu = f"  {YELLOW}1{RESET} attack    {YELLOW}2{RESET} guard    {YELLOW}3{RESET} item"
        if spare_open:
            menu += f"    {YELLOW}4{RESET} spare    {YELLOW}5{RESET} walk away"
        if DEV:
            menu += f"    {YELLOW}9{RESET} skip"
        print(menu)
        choice = input("  > ").strip()
        print()

        if choice == "1":
            dmg = random.randint(4, 7)
            enemy.hp -= dmg
            print(f"  {player.name} strikes. {BLOOD}-{dmg}{RESET}")
        elif choice == "2":
            player._guarding = True
            print(f"  {player.name} braces.")
        elif choice == "3":
            usable = [it for it in player.items if it["count"] > 0]
            if not usable:
                print(f"  {GREY}no items left.{RESET}")
                continue
            for i, it in enumerate(usable):
                print(f"    {i+1} {it['name']}  (heal {it['heal']})  x{it['count']}")
            pick = input("  use > ").strip()
            if pick.isdigit() and int(pick) >= 1 and int(pick) <= len(usable):
                it = usable[int(pick) - 1]
                it["count"] -= 1
                player.heal(it["heal"])
                print(f"  {player.name} uses {it['name']}. {GREEN}+{it['heal']}{RESET}")
            else:
                print(f"  {GREY}never mind.{RESET}")
        elif choice == "4" and spare_open:
            print(f"  {player.name} lowers his weapon.")
            pause(1)
            print(f"  {GREEN}{enemy.name} stops fighting.{RESET}")
            player.gold += enemy.gold
            if enemy.gold:
                print(f"  {YELLOW}+{enemy.gold} gold{RESET}")
            if enemy.reward:
                add_item(player, enemy.reward)
                print(f"  {enemy.name} offers you {enemy.reward['name']}.")
            player.friends.append(enemy.name)
            return "spared"
        elif choice == "5" and spare_open:
            print(f"  {player.name} turns and walks away.")
            pause(1)
            print(f"  {GREY}{enemy.name} does not follow.{RESET}")
            return "walked"
        elif choice == "9" and DEV:
            print(f"  {GREY}[dev] battle skipped.{RESET}")
            enemy.hp = 0
            break
        else:
            print(f"  {GREY}pick a number from the menu.{RESET}")
            continue

        if enemy.hp <= 0:
            break

        pause(0.8)
        atk = random.choice(enemy.attacks)
        dmg = random.randint(atk["min"], atk["max"])
        if player._guarding:
            dmg = max(1, dmg // 2)
        player.hp -= dmg
        print(f"  {enemy.name} - {atk['text']}")
        print(f"  {BLOOD}-{dmg}{RESET}" + ("   (guarded)" if player._guarding else ""))
        if atk.get("funfact"):
            print(f"  {GREY}* {atk['funfact']}{RESET}")
        player._guarding = False
        pause(0.6)
        print()

    if enemy.hp <= 0:
        player.gold += enemy.gold
        if enemy.gold:
            print(f"  {YELLOW}+{enemy.gold} gold{RESET}")
        print(f"\n{enemy.name} is defeated.")
        return "defeated"
    print(f"\n{BLOOD}you fell.{RESET}")
    return "lost"

# regualr battle done...... brother time :'3

def brothers_battle(player, friend, enemy):
    print(f"\n{BLOOD}--- {enemy.name} ---{RESET}")
    pause(1)
    player._guarding = False
    friend,_guarding = False
    while enemy.hp > 0 and (player.hp > 0 or friend.hp > 0):
        print(f" {PALE}{player.name:<12}{RESET} {hp_bar(player.hp, player.max_hp)} {player.hp}/{player.max_hp}")
        print(f" {PALE}{friend.name:<12}{RESET} {hp_bar(friend.hp, friend.max_hp)} {friend.hp}/{friend.max_hp}")
        print(f" {BLOOD}{enemy.name:<12}{RESET} {hp_bar(enemy.hp, player.max_hp)} {enemy.hp}/{enemy.max_hp}")
        print()
        print(f" {GREY} << you are both of them now>> {RESET}")
        print()
        
        spare_open = enemy.can_spare and enemy.hp <= enemy.max_hp * enemy.spare_threshold

        menu = (f"  {PALE}{player.name}{RESET} ->  {YELLOW}1{RESET} strike    "
                f"{YELLOW}2{RESET} guard    {YELLOW}3{RESET} call out    {YELLOW}4{RESET} item")
        if spare_open:
            menu += f"    {YELLOW}5{RESET} spare    {YELLOW}6{RESET} walk away"
        if DEV:
            menu += f"    {YELLOW}9{RESET} skip"
        print(menu)
        choice = input("  > ").strip()
        print()

        if choice == "1":
            dmg = random.randint(4, 7)
            enemy.hp -= dmg
            print(f"  {player.name} strikes. {BLOOD}-{dmg}{RESET}")
        elif choice == "2":
            player._guarding = True
            print(f"  {player.name} plants his feet and puts up his guard.")
        elif choice == "3":
            friend._guarding = True
            print(f"  {player.name} shouts - {friend.name} hears him and braces.")
        elif choice == "4":
            usable = [it for it in player.items if it["count"] > 0]
            if not usable:
                print(f"  {GREY}no items left.{RESET}")
            else:
                for i, it in enumerate(usable):
                    print(f"    {i+1} {it['name']}  (heal {it['heal']})  x{it['count']}")
                pick = input("  use > ").strip()
                if pick.isdigit() and int(pick) >= 1 and int(pick) <= len(usable):
                    it = usable[int(pick) - 1]
                    it["count"] -= 1
                    player.heal(it["heal"])
                    print(f"  {player.name} uses {it['name']}. {GREEN}+{it['heal']}{RESET}")
                else:
                    print(f"  {GREY}never mind.{RESET}")
        elif choice == "5" and spare_open:
            print(f"  {player.name} lowers his weapon.")
            pause(1)
            print(f"  {GREEN}{enemy.name} stops fighting.{RESET}")
            if enemy.reward:
                add_item(player, enemy.reward)
                print(f"  {enemy.name} offers you {enemy.reward['name']}.")
            player.friends.append(enemy.name)
            return "spared"
        elif choice == "6" and spare_open:
            print(f"  the brothers turn and walk away.")
            pause(1)
            print(f"  {GREY}{enemy.name} does not follow.{RESET}")
            return "walked"
        elif choice == "9" and DEV:
            print(f"  {GREY}[dev] battle skipped.{RESET}")
            enemy.hp = 0
            break
        else:
            print(f"  {GREY}pick a number from the menu.{RESET}")

        if enemy.hp <= 0:
            break
        if friend.hp > 0:
            menu = (f"  {PALE}{friend.name}{RESET} ->  {YELLOW}1{RESET} strike    "
                    f"{YELLOW}2{RESET} guard    {YELLOW}3{RESET} call out    {YELLOW}4{RESET} item")
            if spare_open:
                menu += f"    {YELLOW}5{RESET} spare    {YELLOW}6{RESET} walk away"
            if DEV:
                menu += f"    {YELLOW}9{RESET} skip"
            print(menu)
            choice = input("  > ").strip()
            print()

            if choice == "1":
                dmg = random.randint(4, 7)
                enemy.hp -= dmg
                print(f"  {friend.name} strikes. {BLOOD}-{dmg}{RESET}")
            elif choice == "2":
                friend._guarding = True
                print(f"  {friend.name} plants his feet and puts up his guard.")
            elif choice == "3":
                player._guarding = True
                print(f"  {friend.name} shouts - {player.name} hears him and braces.")
            elif choice == "4":
                usable = [it for it in friend.items if it["count"] > 0]
                if not usable:
                    print(f"  {GREY}no items left.{RESET}")
                else:
                    for i, it in enumerate(usable):
                        print(f"    {i+1} {it['name']}  (heal {it['heal']})  x{it['count']}")
                    pick = input("  use > ").strip()
                    if pick.isdigit() and int(pick) >= 1 and int(pick) <= len(usable):
                        it = usable[int(pick) - 1]
                        it["count"] -= 1
                        friend.heal(it["heal"])
                        print(f"  {friend.name} uses {it['name']}. {GREEN}+{it['heal']}{RESET}")
                    else:
                        print(f"  {GREY}never mind.{RESET}")
            elif choice == "5" and spare_open:
                print(f"  {friend.name} lowers his weapon.")
                pause(1)
                print(f"  {GREEN}{enemy.name} stops fighting.{RESET}")
                if enemy.reward:
                    add_item(player, enemy.reward)
                    print(f"  {enemy.name} offers you {enemy.reward['name']}.")
                player.friends.append(enemy.name)
                return "spared"
            elif choice == "6" and spare_open:
                print(f"  the brothers turn and walk away.")
                pause(1)
                print(f"  {GREY}{enemy.name} does not follow.{RESET}")
                return "walked"
            elif choice == "9" and DEV:
                print(f"  {GREY}[dev] battle skipped.{RESET}")
                enemy.hp = 0
                break
            else:
                print(f"  {GREY}pick a number from the menu.{RESET}")

        if enemy.hp <= 0:
            break

# FINALLY NO MORE BATTLE STUFF MY BRAIN CANT TAKE THIS
# oh yeah shoppy time

def shop(player,world):
    print(f"\n{YELLOW} --- SHop --- {RESET}")
    pause(1)
    stock = world.get("shop_stock", [])
    if not stock:
        print(" The shelves are empty :O ")
        return
    while True:
        print(f" {PALE}gold: {player.gold}{RESET}\n")
        for i, it in enumerate(stock):
            print(f"  {i+1} {it['name']}   {it['price']}g   (heal {it['heal']})")
        print(f" b Back")
        c = input("  > ").strip()
        if c.lower() == "b":
            return
        if c.isdigit() and int(c) >= 1 and int(c) <= len(stock):
            it = stock[int(c) -1]
            if player.gold < it["price"]:
                print(f"  {GREY}not enough gold. {RESET}")
                continue
            player.gold -= it["price"]
            add_item(player, {"name": it["name"], "heal": it["heal"]})
            print(f" bought  {it["nane"]}.")
        else: 
            print(f"   {GREY}pick a number or b. {RESET}")

# yaaayyy done with shopppyyy bye bye shoppy
#towny time
def town(player, world, friend=None):
    print(f"\n{YELLOW}--- {world['town_name']} ---{RESET}")
    pause(1)
    while True:
        print(f"  {YELLOW}1{RESET} talk to the creatures")
        print(f"  {YELLOW}2{RESET} rest (heal to full)")
        print(f"  {YELLOW}3{RESET} shop")
        print(f"  {YELLOW}4{RESET} leave town")
        c = input("  > ").strip()
        if c == "1":
            lines = {
                "bella": "Mind the dunes at dusk.",
                "jax": "The armadillo's been furious...",
                "shopkeep": "You should check out the shop, they got good wares",
                "leon": "What did the camel say to the Oasis? 'I'll never desert you!'",
                "koby": "if you ain't got a jacket you're gonna turn into a pupsicle",
                "Zoro": "I dont know where i am, im trying to find my ship",
                "hop": "Ms wolverine is the coolest, shes so strong!",
                "caleb": "The desert is a harsh mistress, but she rewards those who respect her.",
                "mia": "The stars are beautiful at night.",
                "jordan": "The desert is vast and unforgiving."
            }
            for cr in world["town_creatures"]:
                print(f"  {PALE}{cr}:{RESET} {lines.get(cr, '...')}")
                pause(0.3)
        elif c == "2":
            player.hp = player.max_hp
            if friend:
                friend.hp = friend.max_hp
            print(f"  {GREEN}you rest. hp restored.{RESET}")
        elif c == "3":
            shop(player, world)
        elif c == "4":
            print(f"  {GREY}you leave town.{RESET}")
            return
        else:
            print(f"  {GREY}1, 2, 3 or 4.{RESET}")
#now for the scenes ooh i luv these I DID ALL THERSE MYSELF OK I SPENT AGES ON THIS STORY 

def scene_library():
    print("This is meant to be a text based version of my video game to come named Desert Dynasty, if you aren't a reader or interested in lore, this game at the moment may not be for you, Regardless i suggest you play it Enjoy :3")
    print("\033[33m A world of heroes from strength to flight, who will you be?")
    while True:
        hero = input("What is your name? ")
        print("Your name is ", hero, "correct?")
        i = input("yes/no: \033[0m").lower()
        if i == "yes":
            break

    print("\033[031m Why do you always assume every tale must be yours?\033[0m")
    for i in range(5):
        print(" ")

    print("nadroj....")
    print("nadroj")
    time.sleep(2)
    print(f"{BBLUE}Araz: Finally you're awake{RESET}")
    time.sleep(1)
    print(f"{BBLUE}Araz: Come on, we got work to do{RESET}")
    print(f"{GREEN}You need to put away the books{RESET}")

    books = 3
    shelf1 = shelf2 = shelf3 = 0

    print("You see 3 glowing shelves — put one book in each shelf.")

    while shelf1 + shelf2 + shelf3 < books:
        b = input("Which shelf do you go to next? ").lower().strip()

        if b in ("shelf 1", "shelf one", "1", "shelf1"):
            if shelf1 == 1:
                print("That shelf already has its book.")
                print("")
            else:
                print("Book: Powers and Perils")
                print("A world of peace. Clans roam these lands, from strength to telekinesis: from flight to earth control these clans shape our everyday life.")
                print("")
                shelf1 += 1

        elif b in ("shelf 2", "shelf two", "2", "shelf2"):
            if shelf2 == 1:
                print("That shelf already has its book.")
                print("")
            else:
                print("Book: A Guide to Clan Faheem")
                print("This clan has to do with arcane talents, magic spheres to powerful bodies this clan remains a steady founder")
                print("")
                shelf2 += 1

        elif b in ("shelf 3", "shelf three", "3", "shelf3"):
            if shelf3 == 1:
                print("That shelf already has its book.")
                print("")
            else:
                print("Book: A Lost World")
                print("Long ago this world was connected to another through a series of portals. Our kind worked in harmony with the desert creatures, but soon a tyrant arose, and our connection was cut off.")
                print("")
                shelf3 += 1

        else:
            print("That's not a shelf — try 'shelf 1', 'shelf 2' or 'shelf 3'.")
            print("")

    print("You have put all the books away.")

    for i in range(3):
        print(" ")

# heh i luv the lirbary. i still dont know if im gonna keeo their last name as faheem in da real game tho ^-^
#housey 
# my best freind helped me with this part. i got it to work but he helped me figureout the fire thingy. no ai here
# tried to do some funny secrets. i like it :D
def scene_home():
    fire_on = True
    fridge_open = False
    in_bed = False

    explore = 3
    fire_val = kitch_val = bed_val = 0

    print(f"{BBLUE}Araz: Hey kiddo. You done?{RESET}")
    time.sleep(1)
    print(f"{BBLUE}Araz: Good. Now let's get go home{RESET}")
    time.sleep(1)

    while kitch_val + fire_val + bed_val < explore:
        print(f"{PALE}You arrive within your house do you wish to look around?{RESET}")
        y = input("yes/no: ").lower()
        print("")

        if y == "yes":
            print("You see a small living room with a fireplace, a kitchen, and a bedroom.")
            print("where do you want to go? ")
            place = input("fireplace/kitchen/bedroom: ").lower()
            print("")

            if place in ("fire", "fireplace", "1"):
                fire_val = 1
                Question = input(f"You see a {'fire burning' if fire_on else 'empty space'} in the fireplace, {'Do you want to put it out' if fire_on else 'Do you want to light it'}? yes/no: ").lower()
                if Question == "yes":
                    print("You put out the fire" if fire_on else "You light the fire")
                    print("")
                    time.sleep(1)
                    print("It's cold now." if fire_on else "It's warm now.")
                    print("")
                    fire_on = not fire_on
                elif Question == "no":
                    print("You let the fire burn" if fire_on else "You leave the fireplace empty")
                    print("")
                    time.sleep(1)
                    print("It's warm now." if fire_on else "It's cold now.")
                    print("")

            elif place in ("kitch", "kitchen", "2"):
                kitch_val = 1
                if fridge_open:
                    Question = input("The fridge is still open, do you want to close it? yes/no: ").lower()
                    if Question == "yes":
                        print("You close the fridge.")
                        print("")
                        time.sleep(1)
                        print("The kitchen is quiet again.")
                        print("")
                        fridge_open = False
                    elif Question == "no":
                        print("You leave it hanging open.")
                        print("")
                        time.sleep(1)
                        print("The food sits in the light. It is safe from the likes of you. For now.")
                        print("")
                else:
                    Question = input("You see a fridge, do you want to open it? yes/no: ").lower()
                    if Question == "yes":
                        print("You open the fridge and see some food.")
                        print("")
                        time.sleep(1)
                        print("You eat some food and feel better.")
                        print("")
                        fridge_open = True
                    elif Question == "no":
                        print("You leave the fridge closed.")
                        print("")
                        time.sleep(1)
                        print("You think about the food inside. It is safe from the likes of you. For now.")
                        print("")

            elif place in ("bed", "bedroom", "3", "room"):
                bed_val = 1
                if in_bed:
                    Question = input("You are lying on the bed, do you want to get up? yes/no: ").lower()
                    if Question == "yes":
                        print("You get up and stretch.")
                        print("")
                        time.sleep(1)
                        print("You feel refreshed.")
                        print("")
                        in_bed = False
                    elif Question == "no":
                        print("You stay where you are.")
                        print("")
                        time.sleep(1)
                        print("The ceiling keeps its secrets. It is safe from the likes of you. For now.")
                        print("")
                else:
                    Question = input("You see a bed, do you want to lie down? yes/no: ").lower()
                    if Question == "yes":
                        print("You lie down on the bed and close your eyes.")
                        print("")
                        time.sleep(1)
                        print("You drift off for a while.")
                        print("")
                        in_bed = True
                    elif Question == "no":
                        print("You leave the bed alone.")
                        print("")
                        time.sleep(1)
                        print("You think about the comfort of the bed. It is safe from the likes of you. For now.")
                        print("")

            else:
                print("That's not a place — try 'fireplace', 'kitchen' or 'bedroom'.")
                print("")

        elif y == "no":
            print("You decide not to explore the house.")
            time.sleep(1)
            print("You think about the places you could have explored. They are safe from the likes of you. For now.")
            break

    if fire_val + kitch_val + bed_val == explore:
        print("You have explored the house.")
    else:
        print(f"{BBLUE}Araz: never mind then. straight to bed with you.{RESET}")
        time.sleep(1)
        print("You go straight to your room and fall asleep.")
        print("")
        print("The house keeps its secrets. It is safe from the likes of you. For now.")
    fly_star()
    for i in range(5):
        print(" ")

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

# i typed as much as i could man from scracth again this is a very lroe based game im a wrtier but my goodness! 
# sometimes too much bee too much. man i can wait to make graphics so i dont have to read like this

def scene_world1_intro():
    type_out(f"{BBLUE}Araz: What the")
    time.sleep(0.5)
    type_out(f"{BBLUE}Araz: nadroj? ")
    time.sleep(0.5)
    type_out(f"{BBLUE}Araz: nadrojJ!!")

    type_out(f"{BBLUE}Araz: what the hell...")
    time.sleep(0.5)
    type_out(f"{BBLUE}Araz: Where am i?")

    print(f"{PALE} you walk forward, destroyed ruins lay ahead {RESET}")
    print(f"{RED} Click to read{RESET}")
    input("Enter:")

    print(f"{BPURPLE} You crouch own to read the ruins, a touch of your hand cause a rumble")
    print(f" you stumble back as you watch the rock rise")

    print(f"{PALE}{OLD} touches a piece of the ruins.{RESET}")
    time.sleep(1.2)
    print("the stone is warm. warmer than it should be.")
    time.sleep(1.2)
    fly_star()
    ruin_guardian()

    print(f"{YELLOW}the little guardian opens its eyes.{RESET}")
    time.sleep(1)
    print("it looks up at him, then at the road ahead.")
    time.sleep(1)
    print(f"{YELLOW} ????: woah! 10,000 years will give you such a crick in the neck!")
    time.sleep(1)
    print("Hey you there! your the one who opened up my ruins aint ya!")
    time.sleep(1)
    print(f" Names Aron! im the tour guide within these parts whats yer name fella{RESET}")
    time.sleep(1)
    type_out(f"{BBLUE}Araz: My names Araz im not here for a guide or whatever i need to find my brother{RESET}", 0.01)
    print(f"{YELLOW} Aron: a missing brother huh well i got ya! ill take you to Mr.Kommo! he'll surely know where your brother is come on!{RESET}")

    new_team("Aron")

# man i remeber being real excited to do this scence. during the development anyways typing this all again SUCKS
 # ===============================================================================
 # ALL DA INFO FOR WORLD ONE IS GON BEIN DIS SECTION RIGHT HERE
m1 = Creature("Hedgehog", 10, [{"name":"nip","min":2,"max":4,"text":"it nips."}], gold=3)
m2 = Creature("thornydevil", 10, [{"name":"bite","min":2,"max":4,"text":"it bites."}], gold=3)
m3 = Creature("meerkat", 10, [{"name":"scratch","min":2,"max":4,"text":"it scratches."}], gold=4)
m4 = Creature("road runner", 12, [{"name":"peck","min":3,"max":5,"text":"it pecks."}], gold=4)
m5 = Creature("Desert spiny lizard", 12, [{"name":"sting","min":3,"max":5,"text":"it stings."}], gold=5)

jackrabbit = Creature(
    "jackrabbit", 30,
    [
      {"name":"kick","min":4,"max":7,"text":"it lashes out with a hind kick.",
       "funfact":"a jackrabbit's hind legs can launch it 10 metres in one bound."},
      {"name":"stab","min":5,"max":8,"text":"it thrusts its spear-like weapon."},
      {"name":"ear airslash","min":3,"max":6,"text":"it whips its ears, loosing a blade of air.",
       "funfact":"those huge ears dump body heat in the desert sun."},
    ],
    can_spare=True, spare_threshold=0.25,
    reward={"name":"coconut water","heal":8}, gold=15,)

armadillo = Creature(
    "armadillo", 30,
    [
      {"name":"roll","min":5,"max":7,"text":"it curls and bowls into you."},
      {"name":"slam","min":6,"max":9,"text":"it rears and slams down."},
      {"name":"quill","min":4,"max":7,"text":"it flings a loose scale."},
    ],
    is_boss=True, gold=40,
)

# more world one stuff but like docile stuff
WORLD_1 = {
    "name": "Desert",
    "town_name": "Zerzora",
    "small_monsters": [m1,m2,m3,m4,m5],
    "town_creatures": ["bella", "jax", "shopkeep", "leon"],
    "sub_boss": jackrabbit,
    "boss": armadillo,
    "spawn_chance": 0.7,
    "shop_stock": [
        {"name": "coconut water", "price": 5,  "heal": 8},
        {"name": "cactus juice",  "price": 9,  "heal": 15},
        {"name": "date cake",    "price": 12,  "heal": 20},
    ],
}

# done with that data! now im gonna give ya honesty during the actual developmetn once i finsihed world 1 i just copied and pasted that data and just changed what i needed to change
# why mess wiht what works after all... and you said to type iot out but thats a lot of sata man to do 3 times. it wasnt ai its just what i did man
# oh yeah time to finally run da world, yer hearing alot of random in these comments but its like the only thing keepin me sane rightnow
#i really tried man on arceus tis wasnt ai :'3

def run_world(player, world, start=0):
    print(f"\n{PURPLE}========== WORLD: {world['name']} =========={RESET}")
    pause(1.5)

    if start == 0:
        player.small_defeated = 0
        print(f"{GREY}- the road ahead -{RESET}")
        pause(1)
        while player.small_defeated < 5:
            input(f"{GREY}[ ENTER ] walk on{RESET} ")
            if random.random() < world["spawn_chance"]:
                enemy = random.choice(world["small_monsters"])
                enemy.hp = enemy.max_hp
                if battle(player, enemy) == "lost":
                    return "lost"
                if enemy.hp <= 0:
                    player.small_defeated += 1
                    print(f"{GREY}small monsters defeated: {player.small_defeated}/5{RESET}")
            else:
                print(f"  {GREY}the path is quiet for now.{RESET}")
            pause(0.5)

    if start <= 1:
        print(f"\n{YELLOW}a town rises in the distance.{RESET}")
        pause(1.5)
        town(player, world)

    if start <= 2:
        print(f"\n{BLOOD}- something is waiting on the road -{RESET}")
        pause(1.5)
        sub = world["sub_boss"]
        sub.hp = sub.max_hp
        # funny story about the jackrabbit when making his personality kinda the word "mate" me my best bud were trna figure out if thatd make im britush or austrlian
        type_out(f"{YELLOW}The jackrabbit plants its spear and looks at you.{RESET}", 0.02)
        pause(1)
        print(f"{YELLOW}Jackrabbit: oi mate ye a human, what in da desert are ye doing. {RESET}")
        time.sleep(1.5)
        print(f"{BBLUE}Araz: im looking for my brother, let me pass so i can keep looking.{RESET}")
        time.sleep(1)
        print(f"{YELLOW}Jackrabbit: nah mate i cant do that. its part of me job as a guard{RESET}")
        pause(1.5)

        result = battle(player, sub)
        if result == "lost":
            return "lost"

        # ive been iffy with the spare feature im keeping it but its not the same as what i want it to be in the official
        if result == "spared":
            print(f"{YELLOW}jackrabbit: ...ye had me. and you didn't take it.{RESET}")
            pause(1.2)
            print(f"{YELLOW}jackrabbit: the desert will remember yer kindness, go on kid{RESET}")
        elif result == "walked":
            print(f"{YELLOW}jackrabbit: smart.{RESET}")
        else:
            print(f"{YELLOW}jackrabbit: i did all i could scram.{RESET}")
        pause(1.5)

        while True:
            print(f"\n  {YELLOW}1{RESET} go back to town")
            print(f"  {YELLOW}2{RESET} move forward")
            c = input("  > ").strip()
            if c == "1":
                town(player, world)
            elif c == "2":
                break
            else:
                print(f"  {GREY}1 or 2.{RESET}")

    if start <= 3:
        print(f"\n{GREY}- the road to the boss -{RESET}")
        pause(1)
        for i in range(3):
            enemy = random.choice(world["small_monsters"])
            enemy.hp = enemy.max_hp
            print(f"\n{GREY}guard {i+1}/3{RESET}")
            if battle(player, enemy) == "lost":
                return "lost"

    boss = world["boss"]
    boss.hp = boss.max_hp
    # fun fact about kommo his name if ya didnt know comes from my best friends fav pokemon. pokemon is also the reason my reposotory is named incineroar
    ruin_guardian()
    pause(1)
    print(f"{YELLOW} Aron: Thats him right there thats kommo! hes a nice guy go ask him.")
    pause(0.5)
    type_out(f"{RED}the armadillo stands within his base back facing you he turns{RESET}", 0.02)
    pause(1)
    print(f"{RED}Kommo:Who are you? How did you get into my base? {RESET}")
    time.sleep(1.5)
    print(f"{BBLUE}Araz: The door. Where are you keeping my brother?{RESET}")
    time.sleep(1)
    print(f"{RED}Kommo: huh {RESET}")
    pause(1.5)
    print(f"{BBLUE}Araz: Do not lie to me! That thing took him here! I know he is around here; you have the same symbol on your armor!{RESET}")
    pause(1)
    print(f"{RED} Kommo: I do not know where your whatever is, brat, but you do not just get to barge into my base and demand things from me!{RESET}")
    pause(0.4)
    type_out(f"{BPURPLE} then Kommo tilts his hat")
    type_out(f"kommo will then let out a shriek.{RESET}")
    pause(1.5)

    result = battle(player, boss)
    if result == "lost":
        return "lost"

    # me n my buds actually already have concept art for kommo, right now were fixng all the other bosses
    #another fun fact is before stardance id already had this idea but it actually took me 3 sperate days to come up with my full prophecy and the other half is sadly not in this game
    print(f"{BBLUE}Araz: There i beat you, now tell me where is that thing keeping my brother?{RESET}")
    pause(1.2)
    print(f"{RED}Kommo: Alright. you got me.")
    type_out("Long ago we lived in peace all the worlds combined, including your human world. But then a tyrant arose, he didn't want the humans to come in contact with us for fear of the prophecy which threatened him")
    time.sleep(0.5)
    type_out(f"{RED} i dont know it all, but what i do know is {ICE} 'A world suspended, a desert concealed. Twin souls drawn into the ruin, bound by blood but separated by fate'{RESET}")
    time.sleep(0.5)

    print(f"{RED} this is why i believe out leader took your brother though i dont know the full truth. go on hero.{RESET}")
    time.sleep(0.5)

    print(f"{BBLUE}Araz: thank you kommo, you have true honor.{RESET}")
    return "cleared"

# YOOOO world one is done and done hey i already mentioned it im doing exactly what i did in development with NO AI man absolute zero. 
# im keepoign the same code becuase genuienly im trying to make it work correctly and i dont want to mess it up i had tons of errors 
#i legit stayed up till 12 tryuing to fix all individaul bugs and it was anooying becuase i kept DYING IN THE GAME
# developer mode can only do so much...

b1 = Creature("arctic fox", 12, [{"name":"nip","min":3,"max":4,"text":"it nips."}], gold=5)
b2 = Creature("arctic wolf", 12, [{"name":"bite","min":3,"max":4,"text":"it bites."}], gold=5)
b3 = Creature("canada lynx", 12, [{"name":"scratch","min":3,"max":6,"text":"it scratches."}], gold=9)
b4 = Creature("snowy owls", 14, [{"name":"peck","min":4,"max":6,"text":"it pecks."}], gold=8)
b5 = Creature("arctic skua", 14, [{"name":"sting","min":4,"max":6,"text":"it stings."}], gold=9)

wolverine = Creature(
    "wolverine", 35,
    [
      {"name":"snowball","min":4,"max":7,"text":"it throws a snowball at you.",
       "funfact":"a wolverine is Built like a tank."},
      {"name":"swing","min":5,"max":8,"text":"it slams its hammer"},
      {"name":"bite","min":3,"max":6,"text":"it bites you ",
       "funfact":"Wolverines Largest Land Weasel"},
    ],
    can_spare=True, spare_threshold=0.25,
    reward={"name":"ice pop","heal":10}, gold=15,)

polar_bear = Creature(
    "polar bear", 40,
    [
      {"name":"slide","min":5,"max":7,"text":"it slides and tackle you"},
      {"name":"ice throw","min":6,"max":9,"text":"it throws a chunk of ice at you"},
      {"name":"club","min":4,"max":7,"text":"it hits you with its club"},
    ],
    is_boss=True, gold=60,
)

WORLD_2 = {
    "name": "Arctic",
    "town_name": "Frostlock",
    "small_monsters": [b1, b2, b3, b4, b5],
    "town_creatures": ["koby","zoro","shopkeep","hop"],
    "icesub_boss": wolverine,
    "iceboss": polar_bear,
    "spawn_chance": 0.7,
    "shop_stock": [
        {"name": "Ice pop", "price": 5,  "heal": 10},
        {"name": "snow cones",  "price": 10,  "heal": 18},
        {"name": "Hot chocolate",    "price": 18,  "heal": 25},
    ],
}
# fun fact i spun a wheel to see which one piece char id oput in the village becuase i was bored and it landed on zoro :3 go wheel
def run_world1(player, world, start=0):
    print(f"\n{ICE}========== WORLD: {world['name']} =========={RESET}")
    pause(1)
    print(ruins)
    input("press [ENTER] to read")
    type_out(f"{ICE}Where the skies turn to ash and the dunes whisper, the shadow takes root in familiar flesh. The weaker vessel drinks the rot, and the fracture begins.{RESET}", delay=0.1)
    pause(1.5)

    if start == 0:
        player.small_defeated = 0
        print(f"{GREY}- the road ahead -{RESET}")
        pause(1)
        while player.small_defeated < 5:
            input(f"{GREY}[ ENTER ] walk on{RESET} ")
            if random.random() < world["spawn_chance"]:
                enemy = random.choice(world["small_monsters"])
                enemy.hp = enemy.max_hp
                if battle(player, enemy) == "lost":
                    return "lost"
                if enemy.hp <= 0:
                    player.small_defeated += 1
                    print(f"{GREY}small monsters defeated: {player.small_defeated}/5{RESET}")
            else:
                print(f"  {GREY}the path is quiet for now.{RESET}")
            pause(0.5)

    if start <= 1:
        print(f"\n{ICE}a village rises in the distance.{RESET}")
        pause(1.5)
        town(player, world)

    if start <= 2:
        print(f"\n{BLOOD}- something is waiting on the road -{RESET}")
        pause(1.5)
        icesub = world["icesub_boss"]
        icesub.hp = icesub.max_hp
        # in my story the wolverine and snake are my only girl boss characters im maybe thinking of making the addx in my 4th world a girl but drawing athena like armors hard ish

        type_out(f"{CYAN}the wolverine plants its hammer and looks at you.{RESET}", 0.02)
        pause(1)
        print(f"{CYAN}wolverine: Hah! a new opponent! good ive been getting tired of facing numbskulls. not like you'll be nay different!{RESET}")
        time.sleep(1.5)
        print(f"{BBLUE}Araz: im too busy to deal with you right now, let me pass{RESET}")
        time.sleep(1)
        print(f"{CYAN}wolverine: YOU'LL PASS IF YOU BEAT ME NERD{RESET}")
        pause(1.5)
        print(f"{PURPLE} ----- BATTLE START{RESET}")

        result = battle(player, icesub)
        if result == "lost":
            return "lost"

        # i kinda wanted to model the wolveirne after undynes personalty but realy the biggest inspo i got was cynthia from pokemon shes silly but aboslutly terrifyiing at the ame time
        if result == "spared":
            print(f"{CYAN}wolverine: impossible! theres no way you could've beaten me i'm the strongest around!{RESET}")
            pause(1.2)
            print(f"wolverine: get back here!{RESET}")
            input("Press enter to bonk: ")
            pause(1.2)
            print(f"{CYAN}wolverine: ugh, why did a riser have to be so strong{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: what did you call me?{RESET}")
            pause(1.2)
            print(f"{CYAN}wolverine: strong?{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: no the other thing{RESET}")
            pause(1.2)
            type_out(f"{CYAN}Come on Your here and you dont even know what you are? yeesh. YOU are a riser a hero from another world meant to bring peace or whatever. but i say screw you! we were doing just fine till you and that whiny brat came to our kingdom{RESET}", delay=0.03)
            print(f"{BBLUE} You! my brothers i this world inst he! where are you keeping him!{RESET}")
            pause(1.2)
            print(f"{CYAN} wolverine: he's just in the base{RESET}")
            print()
            type_out(f"{GREEN} you now know where your brother is!{RESET}")
# also this like double text is just like this becuase i neeeded soemthing simple and i didnt have time to worry about the fact truing off this spare might do something to the other bosses not only that but it kept running else in dev mode so i didnt wanna risk it
        else:
            print(f"{CYAN}wolverine: impossible! theres no way you could've beaten me i'm the strongest around!{RESET}")
            pause(1.2)
            print(f"wolverine: get back here!{RESET}")
            input("Press enter to bonk: ")
            pause(1.2)
            print(f"{CYAN}wolverine: ugh, why did a riser have to be so strong{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: what did you call me?{RESET}")
            pause(1.2)
            print(f"{CYAN}wolverine: strong?{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: no the other thing{RESET}")
            pause(1.2)
            type_out(f"{CYAN}Come on Your here and you dont even know what you are? yeesh. YOU are a riser a hero from another world meant to bring peace or whatever. but i say screw you! we were doing just fine till you and that whiny brat came to our kingdom{RESET}", delay=0.03)
            print(f"{BBLUE} You! my brothers i this world inst he! where are you keeping him!{RESET}")
            pause(1.2)
            print(f"{CYAN} wolverine: he's just in the base{RESET}")
            print()
            type_out(f"{GREEN} you now know where your brother is!{RESET}")
        pause(1.5)

        while True:
            print(f"\n  {CYAN}1{RESET} go back to town")
            print(f"  {CYAN}2{RESET} move forward")
            c = input("  > ").strip()
            if c == "1":
                town(player, world)
            elif c == "2":
                break
            else:
                print(f"  {GREY}1 or 2.{RESET}")

    if start <= 3:
        print(f"\n{GREY}- the road to the boss -{RESET}")
        pause(1)
        for i in range(3):
            enemy = random.choice(world["small_monsters"])
            enemy.hp = enemy.max_hp
            print(f"\n{GREY}guard {i+1}/3{RESET}")
            if battle(player, enemy) == "lost":
                return "lost"

    iceboss = world["iceboss"]
    iceboss.hp = iceboss.max_hp
    # you ever seen how to train yer dragon. yeah hiccups dad is how i imagine what this guys is like
    print(f"{ICE}the air is cold and the snow is falling{RESET}")
    time.sleep(0.5)

    print(f"{GREEN} you see your brother trapped in a cell, use your sword to try to get him out?  {RESET}")
    time.sleep(0.5)
    input("[ ENTER ]" )
    print("a rumble emerges, you turn to see the boss of this world.")
    type_out(f"{ICE}the polar bear stands within his base back facing you he turns{RESET}", 0.02)
    pause(1)
    print(f"{ICE}ursus: you there! get away from that cell!{RESET}")
    time.sleep(1.5)
    print(f"{BBLUE}Araz: never! im getting my brother out of here {RESET}")
    time.sleep(1)
    print(f"{ICE}ursus: In the name of ankh i shall defeat you mortal {RESET}")
    pause(1.5)
    print(f"{ICE} ursus: im not one to be trifled with brat. surrender, before i make you surrender your life{RESET}")
    pause(0.4)
    type_out(f"The polar bear raises his paws and slams the on the ground shaking the floor.{RESET}")
    pause(1.5)

    result = battle(player, iceboss)
    if result == "lost":
        return "lost"

    # i really like naming my animalk style characters after their scientifc names it just sounds
    sword_point()
    print(f"{BBLUE}Araz: now release my brother from that cell, i won fair. {RESET}")
    pause(1.2)
    print(f"{RED}ursus: Fine, you lousy brats.{RESET}")
    type_out(f"{GREEN} The polar bear snaps opening the cell. {RESET}", delay=0.2)
    type_out(f"{ICE} Now buzz off get out of my base{RESET}", delay=0.003)
    print()
    print(f"{BPURPLE}nadroj: araz!{RESET}")
    time.sleep(0.5)
    print(f"{BBLUE}Araz: Ned oh thank god. you're ok. We can go home now finally.{RESET}")
    return "cleared"

#oooooooooooooooooo finally done with these two worlds. im stayign up past my bed tiem to do this...
# anything for coding i say  im sligtghly loosing motivation just having to fix things but ireally want this game to be real so icant give upo on the little things >:3
# ANYYWAYS WORLD 3
#fun fact the ;etter number i have representing the creatures were totaly random i asked randoms in my class to pick a letter
z1 = Creature("fennec fox", 12, [{"name":"nip","min":3,"max":4,"text":"it nips."}], gold=5)
z2 = Creature("kangaroo rat", 12, [{"name":"bite","min":3,"max":4,"text":"it bites."}], gold=5)
z3 = Creature("bat", 12, [{"name":"scratch","min":3,"max":6,"text":"it scratches."}], gold=9)
z4 = Creature("sand cat", 14, [{"name":"smack","min":4,"max":6,"text":"it smacks."}], gold=8)
z5 = Creature("bearded gecko", 14, [{"name":"sting","min":4,"max":6,"text":"it stings."}], gold=9)

kitFox = Creature(
    "Kit Fox", 35,
    [
      {"name":"paw punch","min":4,"max":7,"text":"it throws a punch at you.",
       "funfact":"the smallest wild dog species in North America"},
      {"name":"swing","min":5,"max":8,"text":"it swings its claymore at you"},
      {"name":"bite","min":3,"max":6,"text":"it bites you ",
       "funfact":"Kit foxes rarely drink water. They get most of their water from the food they eat."},
    ],
    can_spare=True, spare_threshold=0.25,
    reward={"name":"Super Tea","heal":15}, gold=20,)

rattlesnake = Creature(
    "Rattlesnake", 40,
    [
      {"name":"poison spit","min":5,"max":7,"text":"it spits acid at you"},
      {"name":"tail swipe","min":6,"max":9,"text":"it swipes its tail at you and you fall"},
      {"name":"smack","min":4,"max":7,"text":"it hits you with its tail"},
    ],
    is_boss=True, gold=60,
)

WORLD_3 = {
    "name": "Infinite Night",
    "town_name": "Onyx Reach",
    "small_monsters": [z1, z2, z3, z4, z5],
    "town_creatures": ["leo","mia","shopkeep","jordan"],
    "nightsub_boss": kitFox,
    "nightboss": rattlesnake,
    "spawn_chance": 0.7,
    "shop_stock": [
        {"name": "Super Tea", "price": 10,  "heal": 15},
        {"name": "mango",  "price": 15,  "heal": 24},
        {"name": "Latte",    "price": 18,  "heal": 30},
    ],
}

def run_world2(player, friend, world, start=0):
    print(f"\n{GREY}========== WORLD: {world['name']} =========={RESET}")
    pause(1.5)

    if start == 0:
        player.small_defeated = 0
        print(f"{GREY}- the road ahead -{RESET}")
        pause(1)
        while player.small_defeated < 5:
            input(f"{GREY}[ ENTER ] walk on{RESET} ")
            if random.random() < world["spawn_chance"]:
                enemy = random.choice(world["small_monsters"])
                enemy.hp = enemy.max_hp
                if brothers_battle(player, friend, enemy) == "lost":
                    return "lost"
                if enemy.hp <= 0:
                    player.small_defeated += 1
                    print(f"{GREY}small monsters defeated: {player.small_defeated}/5{RESET}")
            else:
                print(f"  {GREY}the path is quiet for now.{RESET}")
            pause(0.5)

    if start <= 1:
        print(f"\n{GREY}a small city rises in the distance.{RESET}")
        pause(1.5)
        town(player, world, friend)

    if start <= 2:
        print(f"\n{BLOOD}- something is waiting on the road -{RESET}")
        pause(1.5)
        nightsub = world["nightsub_boss"]
        nightsub.hp = nightsub.max_hp
        # the kit fox has so far been my hardest character to desing mainly becuase ervtyimg i draw him he wither loks like a cat or a chihuahua no inbetween
        #i also think he just reminds me of my grnapas dog personality wise
        type_out(f"{GREY}the kit fox plants its claymore and looks at you.{RESET}", 0.02)
        pause(1)
        print(f"{GREY}kit fox: my goodness! its_ humans! humans in my realm! you'll never get past me humans!{RESET}")
        time.sleep(1.5)
        print(f"{BBLUE}Araz: we just want to go home we dont have to fight you {RESET}")
        time.sleep(1)
        print(f"{GREY}kit fox: Never! ill never back down i the great Tibert shall never back down from a fight!{RESET}")
        pause(1.5)
        print(f"{PURPLE} ----- BATTLE START{RESET}")

        result = brothers_battle(player, friend, nightsub)
        if result == "lost":
            return "lost"

        # honeslty.. i do not remeber how i came up witht he name tibert it lowkey just came to me i ont even know what it means. ill googleit in a bit
        if result == "spared":
            print(f"{GREY}kit fox: AGH! FOILED BY A MERE TRAVELLER! BUT DO NOT THINK THIS DENTS MY ASCENT TO GENERALHOOD! A TRULY GREAT OFFICER KNOWS HOW TO TAKE A HITTING AND LOOK MAGNIFICENT WHILE DOING IT! BEHOLD MY MAGNIFICENT RETREAT!{RESET}")
            pause(1.2)
            print(f" the fox runs away{RESET}")
            input("Press enter to bonk: ")
            pause(1.2)
            print(f"{BPURPLE} nadroj: i like that guy{RESET}")
            pause(1.2)
            for i in range(3):
                print()
            print(f"{BBLUE}Araz: hey little dude. are you good? not rattled up or anything?{RESET}")
            pause(1.2)
            print(f"{BPURPLE}nadroj: Nah bro im good{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: alright then im going to scout ahead{RESET}")
            play_scene()
            print(f"{BBLUE} Araz: there you are bud cmon lets go.{RESET}")
        else:
            print(f"{GREY}kit fox: AGH! FOILED BY A MERE TRAVELLER! BUT DO NOT THINK THIS DENTS MY ASCENT TO GENERALHOOD! A TRULY GREAT OFFICER KNOWS HOW TO TAKE A HITTING AND LOOK MAGNIFICENT WHILE DOING IT! BEHOLD MY MAGNIFICENT RETREAT!{RESET}")
            pause(1.2)
            print(f" the fox runs away{RESET}")
            pause(1.2)
            print(f"{BPURPLE} nadroj: i like that guy{RESET}")
            pause(1.2)
            for i in range(3):
                print()
            print(f"{BBLUE}Araz: hey little dude. are you good? not rattled up or anything?{RESET}")
            pause(1.2)
            print(f"{BPURPLE}nadroj: Nah bro im good{RESET}")
            pause(1.2)
            print(f"{BBLUE}Araz: alright then im going to scout ahead{RESET}")
            play_scene()
            print(f"{BBLUE} Araz: there you are bud cmon lets go.{RESET}")
# update tibert measn bold or brave people coming from old germanic and french. look at me being smart with my names
        while True:
            print(f"\n  {CYAN}1{RESET} go back to town")
            print(f"  {CYAN}2{RESET} move forward")
            c = input("  > ").strip()
            if c == "1":
                town(player, world, friend)
            elif c == "2":
                break
            else:
                print(f"  {GREY}1 or 2.{RESET}")

    if start <= 3:
        print(f"\n{GREY}- the road to the boss -{RESET}")
        pause(1)
        for i in range(3):
            enemy = random.choice(world["small_monsters"])
            enemy.hp = enemy.max_hp
            print(f"\n{GREY}guard {i+1}/3{RESET}")
            if brothers_battle(player, friend, enemy) == "lost":
                return "lost"

    nightboss = world["nightboss"]
    nightboss.hp = nightboss.max_hp
    # writing her perosnality was hard and not hard ebcuase she reminded me of hornet from silksong but then she also feels like she has asuperiority conplex which ive been wondeing about
    #its funny im wondeifng and these are my charsatcers :'3
    # tuis the life of an author who really wants to make video games
    print(f"{GREY}coming into view you see a tunnel{RESET}")
    tunnel(5)
    print(f"{BPURPLE} nadroj: araz look its a tunnel! maybe thats our way out{RESET}")
    input("[ ENTER ]" )
    print("a rumble emerges, you turn to see the boss of this world.")
    time.sleep(0.5)
    type_out(f"{GREY}the boss of this world a huge rattle snake she coiled up blocking the exit{RESET}", 0.02)
    pause(1)
    print(f"{GREY}OH NO{RESET}")
    time.sleep(1.5)
    print(f"{BBLUE}Araz: hey knock it off, we just want to get home.{RESET}")
    time.sleep(1)
    print(f"{GREY}Anantas: You think you can just walk through my desert without consequences? I'm not soft like those mammals. {RESET}")
    pause(1.5)
    print(f"{BPURPLE}nadroj: We just need to move on; we don't need to fight you")
    time.sleep(0.5)
    print(f"{ICE}Anantas: You think I care?! No! I'm not going to be a failure like the last 2; I am worthy of my position!{RESET}")
    pause(0.4)
    type_out(f"The rattlesnake coils up and prepares to strike.{RESET}")
    pause(1.5)

    result = brothers_battle(player, friend, nightboss)
    if result == "lost":
        return "lost"

    # i dont rmeebr exaclty where i go the name anantas but im cutting to the chase this time it means eternal/ endless fitting becuae this world is my infinite night eheheheheheheh 
    sword_point()
    print(f"{GREY}Anantas: Impossible, a pair of risers… who clearly don't know what they're getting into, bested me, not once! has a riser ever made it past me! {RESET}")
    pause(1.2)
    print(f"{BPURPLE}nadroj: there, We are done now; can we go?{RESET}")
    pause(1)
    print(f"{GREY}Anantas: Go through the tunnel and get out of my sight. Don't you believe you can beat me again? I'll turn your bodies to mush.{RESET}")
    time.sleep(0.5)
    print(f"{BBLUE}Araz: Noted…. Cmon bro{RESET}")
    type_out(f"{GREEN} Araz runs through the exit leaving behind Nadroj for a second {RESET}")
    pause(3)
    glitch_shake(f"{RED} Anantas: You have the mark of %#&% in you… Watch yourself…{RESET}")
    for i in range(3):
        print()
    print("Nadroj returns to his brother")
    pause(1)
    print(f"{BBLUE}Araz: there you are bud i found the portal lets go")
    portal_closing()
    return "cleared"

# YOOO PUZZLE TIME BABY 
# i spent forveer in my free time lookign for puzzles that wouldnt be too hard but i didnt want to do another word unscrambker again sooo i shoose riddelssss
#  i cant do like visual puzzles obvioulsy (i aint that good sadly... im getitng better) so we got typicall unscrmabing keeoing it simple
def puzzle_gate():
    puz_ans = "ice world"
    while True:
        ans = input("Solve: ")
        if ans == puz_ans:
            print("You solved the puzzle! You may move on")
            break
        print("Wrong, try again!\n")
def puzzle_gate2():
    puz_ans = "night world"
    while True:
        ans = input("Solve: ")
        if ans == puz_ans:
            print("You solved the puzzle! You may move on")
            break
        print("Wrong, try again!\n")
#genuienly in the devlopent these gave me so much troubleeeee it would not work soemtimes :'3
#devlopmet mode timeeeee this thing gave me so much trouble man am i glad i got it to work
def dev_menu():
    print(f"{GREY}[dev] start at:{RESET}")
    print("  1 library           2 home               3 square fight")
    print("  4 world 1 intro      5 desert road        6 desert town")
    print("  7 jackrabbit         8 desert guards      9 kommo boss")
    print(" 10 ice road          11 ice town          12 wolverine")
    print(" 13 ice guards        14 ice boss")
    print(" 15 night road        16 night town        17 kit fox")
    print(" 18 night guards      19 night boss")
    print("  ENTER = play everything from the start")
    c = input("  [dev] > ").strip()
    if c.isdigit() and int(c) >= 1 and int(c) <= 19:
        return int(c)
    return 0

#finally after so many gosh darn defnitions i can finally run the world... WITH ANOTHER DEFINTIOOOONNNn
if __name__ == "__main__":
    start = dev_menu() if DEV else 0

    if start <= 1:
        scene_library()
    if start <= 2:
        scene_home()
    if start <= 3:
        scene_square()
    if start <= 4:
        scene_world1_intro()

    # a time for da startinggggg
    dev_jump = start >= 5
    if start == 0:
        start = 5

    player = Player("Araz", 30)
    if dev_jump:
        player.gold = 25

    # <<<< world oneeee>>>>>
    if 5 <= start <= 9:
        STATE = run_world(player, WORLD_1, start - 5)
        if STATE == "lost":
            print(f"\n{RED}=== GAME OVER ==={RESET}")
            exit()
        print(f"\n{PURPLE}=== WORLD CLEARED ==={RESET}")
        print(f"{BLUE} eci rolwd")
        puzzle_gate()
        start = 10

    # <<<<<< world twoooo>>>>
    if 10 <= start <= 14:
        player.max_hp = player.max_hp + 5
        player.hp = player.max_hp
        print(f"\n{GREEN}you step through the portal feeling stronger. max hp is now {player.max_hp}.{RESET}")
        pause(1.5)
        STATE = run_world1(player, WORLD_2, start - 10)
        if STATE == "lost":
            print(f"\n{RED}=== GAME OVER ==={RESET}")
            exit()
        print(f"\n{PURPLE}=== WORLD CLEARED ==={RESET}")
        print(f"{GREY} gihnt dlowr")
        puzzle_gate2()
        start = 15

    # <<<< world thrreeeeeee>>>>>
    nadroj = Player2(YOUNG, 30)
    player.max_hp = player.max_hp + 5
    player.hp = player.max_hp
    nadroj.max_hp = nadroj.max_hp + 5
    nadroj.hp = nadroj.max_hp
    print(f"\n{BPURPLE}{YOUNG} fights at your side now. you control both brothers.{RESET}")
    print(f"{GREEN}you both feel stronger. {OLD} max hp: {player.max_hp}, {YOUNG} max hp: {nadroj.max_hp}{RESET}")
    pause(1.5)

    STATE = run_world2(player, nadroj, WORLD_3, start - 15)
    if STATE == "lost":
        print(f"\n{RED}=== GAME OVER ==={RESET}")
        exit()
    
#im going to add the final puzzle ow just for stardance along with animation credits and  maybe music in 7th pd
    print(f"{GREEN} IN ORDER TO PASS YOU MUST ANSWER THESE ThREE RIDDLES \n ONLY THEN WILL YOU BE ABLE TO RETURN HOME")
    final_puz()
    big_portal_closing()
    play_credits()
    print(f"\n{BYELLOW}=== DESERT DYNASTY - COMPLETE ==={RESET}")