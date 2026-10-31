import random
import time

currency = 30000
turn_count = 0

def gacha(currency):
  UR_characters = ["Satoru Gojo (Within Infinity)", "Satoru Gojo (Hollow Purple)", "Satoru Gojo (Teen) (The Strongest Blue)", "Ryomen Sukuna (Genuine Jujutsu)", "Suguru Geto (Teen) (To Protecet Non-Sorcerers)", "Yuta Okkotsu (Lend me your strength)", "Toji Fushiguro (The Sorcerer Killer)"]
  ssr_characters = ["Satoru Gojo (The Strongest)", "Yuji Itadori (Cursed Energy Flashes Black)", "Megumi Fushiguro (Incomplete Domain)", "Nobara Kugisaki (Girl Of Steel)", "Kento Nanami (Ratio Technique)", "Suguru Geto (This Is Justice)", "Mahito (Inspiration Of Death)", "Masamichi Yaga (Cursed Corpe Battle)", "Momo Nishimiya (Don't Look Down On Me)", "Aoi Todo (Blast From The Past)", "Kasumi Miwa (Zanshin)", "Hanami (The Thrill Of The Fight)", "Jogo (Pride Of A Cursed Spirit)", "Nobara Kugisaki (Keep Hammering At Them)"]
  sr_characters = ["Toge Inumaki (Resolved Cursed Speech)", "Kaito Yuki (The Resolve Of Being A Sorcerer)", "Masamichi Yaga (Ariadne's Thread Educator)", "Shoko Leiri (Reverse Cursed Technique)", "Kasumi Miwa (Determined Counter)", "Kasumi Miwa (Sprinting)", "Saki Rindo (Bring On The Fight)", "Toge Inumaki (The Baton Of Counterattack)", "Ultimate Mechamaru (Mode: Albatross)", "Kento Nanami (Ex-Office Worker Turned Jujutsu Sorcerer)"]
  r_characters = ["Panda (Don't Blame The Doll)", "Maki Zen'in (Maverick Outcast)", "Momo Nishimiya (Aerial Reconnaissance)", "Toge Inumaki (Cursed Power Of Words)", "Kiyotaka Ijichi (Background Support)", "Nobara Kugisaki (To Stay True To Myself)", "Saki Rindo (Cursed Energy Catastrophe)", "Mai Zen'in (A Clever Bullet)", "Aoi Todo (Reckless Grade 1)", "Yuji Itadori (Sukuna's Vessel)", "Megumi Fushiguro (Unfair Salvation)", "Junpei Yoshino (Value Of Life)", "Noritoshi Kamo (Blood of the Big Three Families)", "Panda (Take The Shortest Way)"]

#  These lists are set as comments, remove the hashtag to test out characters with special abilities without having to gamble for 5 years
#  UR_characters = ["Satoru Gojo (Within Infinity)", "Ryomen Sukuna (Genuine Jujutsu)", "Satoru Gojo (Hollow Purple)"]
#  ssr_characters = ["Mahito (Inspiration Of Death)"]

  hypothetical_currency = currency
  unlocked_characters = []



  while True:

    table_title = "Gacha"
    title = f"{table_title:=^60}"
    print(title)
    print(f"Currency: {hypothetical_currency}")
    print("1. Draw one time")
    time.sleep(0.5)
    print("2. Draw 10 times")
    time.sleep(0.5)
    print("3. Exit")
    time.sleep(0.5)
    ui = input("Choose an option: ")


    r = random.randint(0, 100)
    if ui == "1":
      if hypothetical_currency <= currency:
        print(r)
        time.sleep(0.5)
        hypothetical_currency -= 300
        if hypothetical_currency < 0:
          print("Sorry you are broke!")
        if hypothetical_currency >= 0 and r >= 95 and r <= 100:
          print("You just pulled an ULTRA RARE!!!")
          UR_character = (random.choice(UR_characters))
          print(UR_character)
          if UR_character in unlocked_characters:
            print("You already have this character. +100 currency.")
            hypothetical_currency += 100
          else:
            unlocked_characters.append(UR_character)
        elif hypothetical_currency >= 0 and r >= 85:
          print("You just pulled an SSR!!")
          ssr_character = (random.choice(ssr_characters))
          print(ssr_character)
          if ssr_character in unlocked_characters:
            print("You already have this character. +100 currency.")
            hypothetical_currency += 100
          else:
            unlocked_characters.append(ssr_character)
        elif hypothetical_currency >= 0 and r >= 50 and r <= 85:
          print("You just pulled an SR character!")
          sr_character = (random.choice(sr_characters))
          print(sr_character)
          if sr_character in unlocked_characters:
            print("You already have this character. +100 currency.")
            hypothetical_currency += 100
          else:
            unlocked_characters.append(sr_character)
        elif hypothetical_currency >= 0 and r <= 50:
          print("You just pulled a R character")
          r_character = (random.choice(r_characters))
          print(r_character)
          if r_character in unlocked_characters:
            print("You already have this character. +100 currency.")
            hypothetical_currency += 100
          else:
            unlocked_characters.append(r_character)

    elif ui == "2":
      if hypothetical_currency >= 3000:
        hypothetical_currency -= 3000
        print("Rolling 10 times...")
        for _ in range(10):
          r = random.randint(0, 100)
          if r >= 95:
            print("You just pulled an ULTRA RARE!!!")
            UR_character = (random.choice(UR_characters))
            print(UR_character)
            if UR_character in unlocked_characters:
              print("You already have this character. +100 currency.")
              hypothetical_currency += 100
            else:
              unlocked_characters.append(UR_character)
          elif r >= 85:
            print("You just pulled an SSR!!")
            ssr_character = (random.choice(ssr_characters))
            print(ssr_character)
            if ssr_character in unlocked_characters:
              print("You already have this character. +100 currency.")
              hypothetical_currency += 100
            else:
              unlocked_characters.append(ssr_character)
          elif r >= 50:
            print("You just pulled an SR character!")
            sr_character = (random.choice(sr_characters))
            print(sr_character)
            if sr_character in unlocked_characters:
              print("You already have this character. +100 currency.")
              hypothetical_currency += 100
            else:
              unlocked_characters.append(sr_character)
          else:
            print("You just pulled a R character")
            r_character = (random.choice(r_characters))
            print(r_character)
            if r_character in unlocked_characters:
              print("You already have this character. +100 currency.")
              hypothetical_currency += 100
            else:
              unlocked_characters.append(r_character)
          time.sleep(0.3)
      else:
          print("Not enough currency for 10 rolls!")

    if hypothetical_currency < 0:
      hypothetical_currency += 300
    elif ui == "3":
      break


  return hypothetical_currency, unlocked_characters, sr_characters, ssr_characters, UR_characters

def battle(currency, turn_count, sr_characters, ssr_characters, UR_characters):
  if not unlocked_characters:
    print("You don't have any characters to use!")

  player_hp = 100
  enemy_hp = 100
  landed = 0

  # code for choosing your unit
  print("Choose your unit:")
  for i, char in enumerate(unlocked_characters):
    print(f"{i + 1}. {char}") # makes each character numbered
  sel = int(input("Pick your character: "))
  ui_choice = unlocked_characters[sel-1]

  if ui_choice in UR_characters:
    player_hp = 300
    enemy_hp = 300

  if ui_choice in ssr_characters:
    player_hp = 200
    enemy_hp = 200

  if ui_choice in sr_characters:
    player_hp = 150
    enemy_hp = 150

  table_title = "Battle Start!"
  title = f"{table_title:=^60}"
  print(title)

  while player_hp > 0 and enemy_hp > 0:
    print(f"Your HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")
    turn_count += 1
    table_title = f"Turn {turn_count}"
    title = f"{table_title:=^60}"
    print(title)
    time.sleep(0.5)
    print("1. Physical Attack (10 damage)")
    time.sleep(0.5)
    print("2. Cursed Technique (20 damage, 50% chance)")
    time.sleep(0.5)
    print("3. Black Flash! (40 damage, 25%)")
    time.sleep(0.5)
    if ui_choice == "Satoru Gojo (Within Infinity)" and turn_count >= 3:
      print("4. Domain Expansion: Infinite Void")
      time.sleep(0.5)
    elif ui_choice == "Mahito (Inspiration Of Death)" and player_hp <= 50:
      print("4. Domain Expansion: Self-Enbodiment Of Perfection")
      time.sleep(0.5)
    elif ui_choice == "Ryomen Sukuna (Genuine Jujutsu)" and landed >= 4:
      print("4. Domain Expansion: Malevolent Shrine")
      time.sleep(0.5)
    elif ui_choice == "Satoru Gojo (Hollow Purple)" and turn_count >= 5:
      print("4. Imaginary technique: Hollow Purple")
    player_move = input("Choose your move: ")
    time.sleep(0.5)


    if player_move == "1":
      enemy_hp -= 10
      print("You threw a punch at them dealing 10 damage!")
      time.sleep(0.5)
    elif player_move == "2":
      if random.random() < 0.5:
        enemy_hp -= 20
        print("You launched a cursed technique attack at them dealing 20 damage!")
        time.sleep(0.5)
      else:
        print("You attempted to use cursed technique but missed!")
        time.sleep(0.5)
    elif player_move == "3":
      if random.random() <= 0.25:
        enemy_hp -= 40
        landed += 1
        print("You landed a BLACK FLASH!")
        time.sleep(0.5)
      else:
        print("You attempted a BLACK FLASH but missed!")
        time.sleep(0.5)
    elif player_move == "4" and turn_count >= 3 and ui_choice == "Satoru Gojo (Within Infinity)":
      enemy_hp -= 250
      print("You cast out your Domain...")
      time.sleep(1)
      print("Satoru Gojo: Domain Expansion: Infinite Void")
      time.sleep(3)
      print("             This is the inner world of Limitless")
      time.sleep(2)
      print("             Perception, communication...")
      time.sleep(1.5)
      print("             Every action involved in living is forcibly carried out an infinite number of times.")
      time.sleep(3)
      print("             It's ironic, isn't it?")
      time.sleep(1.5)
      print("             When granted everything, you can't do anything...")
      time.sleep(2.5)
      print("             but just die peacefully.")
      time.sleep(1.5)
      print("""
⣿⣿⣿⣿⣿⣿⣿⣿⡿⡫⣁⡴⣈⡼⣟⣭⣷⣿⡿⠿⡽⡟⠍⡙⢕⣢⣿⡟⣱⣿⣿⣿⣿⣿⠟⠋⡕⢼⣣⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⣩⣾⣿⡿⣿⣿⢿⣿⣿⣿⣿⡿⠛⣙⢄⣽⣿⣿⣿⡃⢹⣿⣿⣾⢫⢿⢇⣿⡟⣼⣿⡇⠯⠈⠰⣶⣾⣶⡄⢻⣿⣿⢎⣮⡹⠗⣠⣵⣶⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⡫⣪⡾⣫⣾⣯⠾⠛⣋⣥⣶⡿⠟⣩⢔⣼⣾⣿⣿⠏⣼⣿⣿⢟⣿⡟⣡⢊⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡿⣫⣷⣿⣿⣿⣫⢏⡼⣫⣾⣿⣿⣿⣃⢔⠟⣱⣿⣿⡿⣛⣿⣿⣿⣿⣿⣿⣏⡾⣼⡿⣸⣿⣿⠃⣴⠠⢹⣸⡿⣿⣇⡱⡊⣿⣎⣎⢷⡘⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⢞⣾⡟⠾⠿⢋⢥⣺⣯⣷⡿⢋⣴⣯⣾⡿⢟⢛⣻⠏⣼⣿⣿⠏⣾⣿⠟⣵⣿⣿⣿⣿⡿⠿⠟⠛⣛⣉⣥⣴⣶⡿⢟⣿⣿⣿⣿⡟⠑⣡⠯⣺⣿⣿⣿⣿⡿⢋⣴⣾⠿⠟⣫⣾⣿⣿⡟⣼⣿⣿⣿⡙⣽⡟⣵⣿⣿⣥⣦⡏⡇⠈⡏⣷⡹⣿⣦⠑⡜⣿⣯⢫⢭⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⣠⠟⣩⣴⡾⣥⣼⠿⣫⣥⢈⣶⠶⢛⢍⡒⣡⡶⣼⠏⣰⣿⣿⢋⠶⢿⢥⣾⣮⣭⣿⢤⣤⡶⡾⣻⣿⠟⣨⣿⡿⢋⣴⣿⡿⣛⡟⡁⣴⡞⣡⣾⣿⢟⣭⣿⡿⠱⠟⡡⡊⣠⣾⣿⡿⣫⣟⣼⣿⢫⢯⣿⢸⣿⣾⣿⣿⣿⣿⢼⣷⣿⠀⣷⢿⢸⣜⢿⣷⡘⣞⢿⣷⡵⡣⠘⢿⣿⣿⣿⣿⣿⣿⣿⠿⢟⡛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⡉⣼⣿⡿⣼⡟⢡⣾⡿⢃⢈⡴⠚⠑⣋⣾⢟⠊⡄⢠⣿⡿⢃⡴⡵⣳⣿⢟⣵⡿⣵⡿⠿⠹⣼⣿⠏⣼⡿⢋⣴⣿⡿⣫⣪⢞⣡⠟⣢⣾⣿⠟⣵⡿⠛⣩⠞⣡⠪⢞⣾⣿⠟⢡⢞⠉⢊⣿⠇⡜⣸⡇⢠⣿⣿⣿⢿⣿⡟⣾⢹⣿⢈⣿⢸⠰⢻⡄⣻⣿⣎⢈⠻⣿⣞⢆⢸⣿⡿⢿⣻⣭⣷⣾⣿⣿⣿⣿⣶⣬⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣦⣿⣿⢱⡟⣴⣿⠟⢑⣫⣷⠖⣡⣾⡿⡵⢁⡞⢻⣾⡟⢁⣞⣞⡽⣟⣵⡿⣫⠿⢋⡴⢰⣱⣿⠇⣼⠏⣠⣾⣿⢯⣾⢞⢵⣫⣷⢾⡯⠫⢠⡞⣡⢮⠞⣱⠞⣡⣢⣿⡿⠑⡠⣵⢇⣆⣾⡏⣼⠃⣿⠀⣽⡏⣿⡏⣼⣿⢳⡏⢨⡏⢘⣿⡔⢈⣸⣿⠱⡹⣿⢸⣰⡌⢛⣣⣬⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣮⠀⠩⢁⣴⣿⢟⣵⣾⡟⠩⠊⢒⢽⣾⣧⣻⡌⣾⢉⣬⠞⠏⠩⢚⣡⣾⠿⡃⡎⣿⠏⡼⢃⣼⣿⡟⢕⠕⣡⣴⢿⡫⠟⣙⣤⣶⠟⢌⡵⢋⡜⣡⡾⣵⣿⠟⢀⣤⡾⣱⡟⢌⡞⣰⡇⣠⡟⡠⣿⡇⣿⡇⣾⣿⡾⢀⣾⡟⣸⣿⣧⢸⣧⣿⢹⠁⣟⣬⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣢⣤⣿⢟⡵⠟⣁⣨⢁⣾⡌⣿⠂⢻⣿⡧⣁⠵⣋⡴⢊⡔⠈⠼⡿⣫⣾⠀⣹⣿⣿⢡⡾⣿⣋⣤⣧⠿⠫⢓⡩⣴⣾⡿⣫⠉⢠⣞⡷⢪⣤⣟⣽⣿⠏⣴⣿⢏⣾⡿⠘⡞⢱⡿⣠⣿⠇⡆⣿⡇⣿⢇⣿⣿⠁⣾⣿⢳⣿⠿⢇⣦⠻⣉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣙⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠏⠕⣩⣴⣿⡿⣣⡿⡳⣣⢹⠀⣃⠅⡨⠠⠞⢱⡞⣼⠛⣆⣧⣝⢛⡻⠤⢯⣟⣃⣲⣯⣿⠿⢛⢡⣶⣾⠛⣴⡿⣫⣾⠃⣰⣯⡟⣱⣯⣏⣼⣿⢃⣾⣿⢣⣿⢏⠄⡼⢡⣿⠇⣼⡿⢠⡏⣿⡇⣿⠈⣿⠇⣾⣿⢧⣿⠃⢀⣾⡟⡰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⠇⣼⣿⣿⢟⡼⠋⣠⠞⠋⠀⠈⣤⣤⢷⢸⡟⣨⡇⠁⣇⢸⣿⣿⣷⣮⢁⠔⡭⠋⠉⡠⣊⡞⣳⣿⣿⣫⣼⢟⣾⣿⠁⡴⣳⢏⣾⣿⣟⡾⢻⣯⣿⣿⡡⢭⢏⡟⢰⢁⡟⡘⢰⣿⡅⣐⡚⣿⡇⣿⢂⡟⣼⣿⢏⣸⠇⣨⣼⡟⡌⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⢻⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠝⡫⠞⣩⡔⣂⣮⢠⣶⡇⡐⡰⣶⠊⢸⠇⣿⡧⡗⣼⢾⣬⣭⡝⡡⡣⠚⠔⠀⢘⣼⣿⢳⣿⣿⣷⣿⣵⣿⣿⠃⣼⣵⢯⣿⣿⡟⣜⢡⡟⢹⣿⢱⣿⣿⣾⠃⢢⡟⣠⢇⣿⣿⡇⡯⠇⣽⡇⣿⢸⡽⣻⢟⠘⠈⣰⣿⡟⢸⢷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢹⣿⡏⢹⣿⡟⠁⠈⣿⡿⠁⣿⣿⠁⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢹
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣀⣥⣴⣾⣳⣾⢟⣵⢯⠞⡠⢳⢷⡭⢰⡏⡇⡏⡇⡅⢻⣿⡿⢋⠈⡀⣰⡷⠀⣠⣈⡹⢛⡿⠿⣿⣿⣿⣿⣿⡿⠰⣳⢫⣿⣿⣿⠹⣁⡾⢡⢸⢣⣿⣿⣿⠿⠐⢋⠚⡈⣬⣭⣴⣶⣞⡇⣿⡇⣿⣸⣱⠟⣎⡇⣸⣿⡟⣼⡟⡾⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠈⡿⢀⡾⠋⣠⠆⠀⣿⠁⠈⠉⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣫⣴⠿⠕⣡⢮⡾⡘⣦⣿⡸⡇⠀⡅⢡⢥⢐⡋⢦⣶⡿⢯⣽⢧⢡⣿⣺⣟⣶⣾⣥⣜⣢⠫⣉⠿⣿⣾⢏⣿⣿⣿⣿⢰⠻⢣⣿⢈⡬⠝⣀⣲⣤⣴⣟⢞⣽⣿⣿⣿⡿⣿⡿⢸⡗⣿⠉⢣⡇⣿⢠⣿⣿⡹⠟⣼⢷⢸⣿⣿⣿⣿⣿⣿⣿⡿⠀⣶⠀⠀⡼⠁⣀⣠⡄⠠⠇⢠⣾⡟⢀⣾⡿⠋⣹⣿⣿⣿⣿⣿⣿⣿⡟⢸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⣡⣘⣣⣴⡾⣽⣳⢏⡼⠁⠙⣿⡇⢿⠀⠻⡾⣸⣿⣿⡐⠢⠩⠀⠐⠀⠭⢒⣚⠯⢭⣛⡿⣿⣿⣷⣶⢤⡹⡟⣼⣿⣿⣿⣿⣮⣴⡿⠿⣄⣶⣾⣿⣿⡿⢟⣫⠭⠿⠒⠢⠤⠔⠀⠀⠘⣧⣿⠌⣿⠃⡟⣼⣿⣿⣇⠆⡿⣼⢸⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣧⣼⣧⣼⣿⣿⣦⣴⣤⣿⣿⣦⣼⡟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⣽⠃⢡⣾⠁⢞⣧⢹⡇⢸⡇⢧⢷⡉⣿⣿⣿⡃⠜⣿⣿⡇⢻⣷⡂⢸⣤⣈⠙⠂⣿⣿⣿⣧⢠⢸⣿⣿⣿⣿⣿⣿⡟⠁⣹⣿⣿⣿⣿⡿⠐⢋⠁⣤⣖⣘⣻⠇⣼⣿⣿⠃⣹⡏⠸⢃⡏⠀⣻⣿⣿⣟⡀⣇⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⢿⠛⢻⡿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⢋⣴⣿⡏⠀⣾⡿⠀⠇⣾⡉⣘⣿⣧⡸⣿⣿⣧⡡⢻⣿⣿⣦⣘⠿⢽⣛⣽⣷⡀⠸⣿⣿⣿⣃⡀⣿⣿⣿⣿⣿⣿⡟⣧⣹⣿⣿⣿⣿⠃⢰⣿⣷⣝⡻⢛⣋⣴⣿⣿⢏⣇⢻⡌⠈⡸⢽⠐⣿⣿⡟⣼⣱⡿⣠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⢠⣶⠀⣴⣿⠀⣠⣶⣶⠂⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⠀⢰⣿⠃⡜⠀⢻⡇⢸⣿⣿⣷⣽⣿⣿⣿⣣⡻⢿⣿⣿⣿⣿⣿⣿⡿⢠⣐⢉⢉⡿⢉⣴⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠻⢿⡏⢠⣌⢿⣿⣿⣿⣿⣿⣿⡿⣫⣜⣿⢳⢠⢹⡇⣸⣷⣾⢛⡇⢿⡟⣱⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⡏⢠⠿⠛⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡜⣣⣾⢁⣃⢹⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣾⣿⣥⣴⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⠡⠛⢿⣾⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠈⡇⢾⣷⣿⣿⡿⢸⣿⡞⡀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠉⢁⣀⣠⣽⣿⣿⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣵⣾⣿⢇⢈⡜⣅⠹⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣸⣧⢻⣿⣿⣿⡇⣿⡟⡀⡆⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢊⣬⣾⣿⣷⣤⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣾⣿⣿⣾⣿⣿⡿⠸⠟⠠⢠⢣⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢹⡟⠈⢹⣿⠃⣸⠏⢸⡏⠈⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⡆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣴⠀⡏⣸⡇⠎⢿⡛⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡟⢁⠀⠸⠃⣰⡟⢀⡿⠀⡀⠘⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣽
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣸⣿⠀⠀⣿⣿⢰⣾⡇⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢠⣾⡀⠀⣴⡿⠁⣾⠁⣼⣷⠀⢠⣿⠛⢙⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⡏⠠⣸⣿⣷⣿⣿⢃⣨⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣷⣾⣿⣷⣼⣿⣶⣿⣿⣷⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣾⣿⢁⣵⣿⣿⣿⣿⣿⣆⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⡙⢿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢂⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣝⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠋⢁⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢱⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣾⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣛⣿⣿⣿⣿⣿⣷⣶⣬⡁⣨⠿⣛⣛⣛⣻⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠐⠌⣿⣆⠹⣿⣿⣿⣿⣿⣏⣙⣻⠿⠿⢿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣟⣋⣤⣾⣿⣿⣿⡿⢣⣾⣿⢏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡴⣩⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡳⢹⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢦⡀⠀⠤⣤⣤⣤⣤⣤⣤⣄⠤⠖⡀⢴⣶⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⡿⠋⣀⠀⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣌⠊⣿⣿⣿⣆⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣙⠛⠛⠒⠒⠒⠒⠒⡖⢒⣩⣼⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⠍⣐⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣷⣿⣿⣿⣿⣷⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⡏⢀⡳⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣖⢀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣿⣿⣿⣿⣿⣿⡯⢅⡾⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠘⣿⡷⣝⢿⣿⣿⣿⣿⡧⠢⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣰⣿⣿⣿⣿⣿⣿⣭⣾⣿⡇⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⣿⣿⣮⡳⡍⠿⣿⣿⣿⣌⠺⢔⣌⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢂⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡌⠲⣜⢿⣿⣿⣿⡄⢠⣹⣷⣆⣉⠛⠿⠿⠿⠿⢿⠿⡿⠿⠿⠟⠋⣀⠤⡢⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡐⢔⢌⢿⣿⣿⣿⣄⠐⢿⣿⣿⣿⣿⣷⣶⣶⣦⣦⣴⣤⣦⡔⠲⢌⡱⣴⣿⣿⣿⠟⢋⣩⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⢠⠓⢮⣻⣿⣿⣿⣎⢈⠽⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠣⠕⢲⣿⣿⣿⣿⢏⣰⣾⠿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣇⢙⢴⢙⣿⣿⣿⣿⣷⡱⣦⣪⠬⣽⣛⡿⡟⣻⣿⣿⣣⣌⣴⣿⣿⣿⡿⢁⡴⢚⣋⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢝⢆⢻⣿⣿⣿⣿⣧⢩⣫⠭⢟⣻⢒⣼⣿⣿⣯⢅⣾⣿⣿⡿⢋⡀⢦⣼⠯⣭⣶⣾⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠿⢿⣿⣿⣿⣄⣺⢭⣻⡆⢾⣿⣿⣿⡄⣿⣿⣿⡟⠁⠀⢴⡟⣮⡿⠼⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
𝙎𝞓𝞣𝙐𝞒𝞗 GOJO
      """)

    elif player_move == "4" and player_hp <= 50 and ui_choice == "Mahito (Inspiration Of Death)":
      enemy_hp -= 150
      print("Mahito: Ah, what...")
      time.sleep(1)
      print("        what fresh inspiration this is!")
      time.sleep(2)
      print("        Is this...")
      time.sleep(1)
      print("        death!?")
      time.sleep(1.5)
      print("        I bet I could do it now...")
      time.sleep(2.5)
      print("        Domain Expansion:")
      time.sleep(2)
      print("        Self-Enbodiment of Perfection!!")
      time.sleep(2.5)

    elif player_move == "4" and ui_choice == "Ryomen Sukuna (Genuine Jujutsu)" and landed >= 4:
      enemy_hp -= 300
      print("Ryomen Sukuna: You really don't understand what curses truly are...")
      time.sleep(2.5)
      print("               This is a good opportunity,")
      time.sleep(1.5)
      print("               so I'll show you...")
      time.sleep(1.5)
      print("               what real jujutsu is.")
      time.sleep(2)
      print("               Domain Expansion: Malevolent Shrine")
      time.sleep(2.5)
      print("""
      ⠀⠀⠀⠀⠀⠀⠀⡀⠤⡂⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⢀⠀⡀⢀⠠⢀⠠⢀⠠⠀⠀⠀⠀⠀⠀⠢⢄⠲⡐⢆⡒⢤⠐⣆⠲⡐⢆⠦⠑⠸⠐⡌⠐⠠⢀⠒⠤⠀⠀⠄⡀⠄⠠⢀⠀⠀⠀⠐⢂⠒⠤⠐⣂⠈⣒⠰⣈⢳⣄⠒⢄⠠⢀⡐⠀⡴⢍⡳⢭⣿⣿⣿⣿⣿⣿⣿⡳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⠀⠊⠐⠁⠀⠀⠀⠄⠂⠁⡀⠄⠐⢀⠠⠐⠀⠂⠄⠂⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠊⡥⡙⠆⢀⠤⠋⠄⠁⡉⠆⢎⠈⢠⡘⠀⡀⠂⠀⠂⠄⡁⠂⠀⠄⡈⠀⠄⠨⡀⠅⢂⠀⠉⠬⠁⡄⢣⠄⡑⢂⠆⡩⢌⠂⡘⠄⢀⢃⠘⠤⡛⢞⣻⣿⣿⣿⣿⠟⡋⠄⡐⢀⠂⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡡⡀⠀⠀⠐⠀⠠⠐⢀⠠⠐⠈⢀⠀⠂⢁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠒⠴⣉⠦⡘⣌⠐⢀⠂⣀⠀⠈⠜⡰⢈⠠⠀⣁⠂⠁⠐⡀⢂⠀⡐⠀⠐⢈⠡⠐⡈⠄⠂⠄⠑⠈⡔⢣⡘⢤⠈⠜⣐⠪⠄⡁⡘⢠⠈⡂⠱⡘⠬⢳⣿⣿⠟⣵⡓⡜⡰⢀⠂⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⢀⡈⠀⠙⠁⠐⠈⠢⠕⠢⢌⣄⡂⣄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⣀⢃⠀⣂⠱⣈⠖⡱⠂⢀⠆⠈⠀⠉⡀⠀⠁⠣⣀⠐⠠⡀⠄⡂⠄⠀⠀⠀⡀⠀⣀⡀⠀⣀⠈⠄⠠⡐⡀⠬⢡⠜⢢⢡⠘⡄⠳⢀⠁⡄⠦⡁⠂⠁⠐⠚⠛⠛⠋⠚⠃⠙⠐⠁⠂⠀⠁⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠠⠀⠄⡀⢀⠀⠀⠈⠉⠉⠉⠒⠃⠶⠤⠦⢤⡤⣔⣚⡙⣉⢏⡩⠃⠀⠉⠀⢦⡙⠴⡡⠌⠀⢄⢰⣶⣤⡉⠄⠐⢄⡂⠅⠠⠅⢀⣿⣷⣶⣿⣶⣿⣿⣿⣄⣠⣮⡈⢡⠐⡰⢀⠣⡘⠥⢢⠀⠌⠁⠌⡰⢘⠐⡠⢁⢩⡉⡟⡿⢃⢯⢻⡍⡏⢌⠡⠉⠀⠀⠀⠂⠐⠈⠄⡁⠂⠀⠀⠀⠀⠀⠀⠀⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠌⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁⠒⠐⠦⢤⣀⣀⣀⡀⠀⠀⠀⠈⠉⠉⠙⠛⠓⠀⠢⡙⢆⠬⣑⠲⠀⠁⣿⣿⣿⣿⣷⣌⣳⣶⣭⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⣀⢦⣐⢀⠉⡂⠣⠄⡁⠂⠁⠆⠘⠀⠀⠀⠀⠀⠀⠠⢎⡱⢜⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⡔⠂⠚⠛⠛⡋⠳⢶⣶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠑⠘⠤⣋⠐⠂⢀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣦⣁⠀⠀⠁⠀⢠⠀⠆⠀⡀⢄⢠⠀⠠⠀⢌⠡⠌⡁⢄⠠⢀⡀⢀⡀⣀⢀⠀⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠎⠉⠀⠀⡀⣀⠬⡡⢞⣱⢳⢦⣄⡁⠐⠠⠀⠈⠑⠉⢙⡛⣛⣿⡇⢰⣶⣦⣤⠀⠂⢀⠐⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣿⣿⣿⡟⢿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢠⣄⡠⢄⢠⣀⡄⢢⣐⣡⠂⡔⢢⠒⢆⠲⢦⢶⣶⣶⣶⡾⠀⠀⠀⠀⠀⠀⡄⠀⠈⠃⠐⠀⠀
⠀⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣚⠴⢡⠉⠆⠱⠠⠓⠉⢈⡀⡉⠤⠤⠲⠓⢂⣀⠀⠠⠀⠙⢜⣻⣿⡇⢸⠏⣦⠁⠀⠀⢸⣮⡁⠠⢴⣬⣿⣿⣿⣿⣿⣿⣇⡈⠙⠛⣿⡇⢸⣿⠙⠋⠁⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⡄⢀⣄⠠⣤⣄⣤⣀⢤⡠⡀⠄⠠⠀⠤⠠⠄⠤⠤⣤⣴⣶⡶⠀⠀⠀⠀⠀⢀⠴⠦⠀⠀⠰⠢⠄⠄
⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⡀⠠⠀⠀⠂⠒⠀⠉⢈⣀⡀⢤⡐⣲⣞⣿⠱⣊⠝⠒⠒⠀⢀⠉⣴⠂⢨⠀⢿⣄⠀⠀⣾⣿⣿⣶⣯⣝⡛⠿⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⢸⡏⢰⣿⣿⣿⣿⣿⣿⡿⠿⠛⢛⣩⣴⣾⣿⣿⣿⠀⢧⣾⠏⠈⣿⠞⠦⠝⠦⠳⢍⢫⠣⡙⢆⠳⣘⢒⡶⣾⣿⡟⠀⠀⠀⠀⠀⢠⠂⡀⢐⡀⠀⠐⡀⠀⠀
⠀⠀⡀⠀⠀⠀⠀⠀⡄⠀⠉⠀⠀⡅⢃⠐⠀⠀⠀⠀⠉⠒⠼⠘⠢⢑⢧⣯⣭⣁⣀⣀⣀⠠⣀⣊⣿⣾⠀⠧⠀⠘⣿⣇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣦⣍⠛⠛⠛⢿⣿⣧⣿⣯⣼⣿⣿⡿⣿⠟⠋⠉⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⢀⣾⡏⠀⠀⠈⠉⠛⠚⠺⠴⠦⢤⣀⣀⠀⡀⠀⢈⢉⣿⠏⠀⠀⠀⠀⠀⠠⠃⠒⠀⠡⠣⠀⠀⠰⠁⠀
⠀⠀⠀⠀⠀⠀⡀⠈⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⣿⣿⢲⣣⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⢸⠙⣿⡀⢻⣿⣿⣯⡑⠽⣿⣿⡻⣿⣿⣦⡀⢐⠻⣿⣿⣿⣿⣿⣿⠞⠁⣠⣶⣿⡿⢟⣛⣿⡫⠟⣻⣿⣿⣿⡃⣺⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠙⠒⠻⠃⠀⡀⠀⠀⠀⣴⠡⢄⠠⢀⠐⠲⡄⠀⠘⡄⠁
⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠀⠁⠂⠀⠀⠀⠐⠀⠀⢹⣿⡷⣯⣿⣿⣿⣿⣿⣿⣿⠀⡿⠷⡈⠀⢨⣷⣼⣿⡟⣋⣿⣷⣤⠈⠙⠚⠩⠝⠙⡓⢤⣨⡻⣿⣿⠛⣁⣴⡟⡩⠭⠖⠂⠋⢁⣤⣴⣾⠁⢸⣿⣿⠃⣾⡀⠁⣿⣿⡄⠒⠀⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠘⠦⠧⢌⡱⠦⠀⠀⠘⠀
⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠂⠀⠛⠙⡛⠛⠻⠿⠿⢿⣿⣿⢀⣧⣄⠀⡇⠻⣿⢻⣿⣿⠀⡼⣿⣿⣄⣀⣰⣷⣦⡘⢷⣼⣿⣧⢿⡇⣾⣿⣿⣷⢂⣴⣾⡀⢀⣼⣿⣿⢣⢣⢸⢿⣿⣶⡿⡱⢠⢣⣛⣿⡄⠀⠈⠻⠋⠙⡽⢛⠿⡶⣶⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠤
⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡵⣬⠴⣤⠤⣆⢶⣧⠐⣷⣞⣧⢻⠐⢹⡆⢯⠻⡜⡆⠊⡻⢿⣿⠿⠟⢛⣫⠶⣘⣿⠟⠘⠘⢿⣋⣛⠣⣞⠿⠿⣿⣿⡿⢟⡣⣡⠝⠜⠈⠇⣿⡍⠃⡽⣲⢣⢞⠛⠀⠀⠀⢰⡀⢀⠒⢢⢴⠖⠀⠀⠀⠀⠀⢠⢏⡓⢒⡂⢄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡜⣏⣒⡙⣈⣊⡅⢸⣏⡿⠋⠈⣿⣿⣿⡘⠃⠑⢕⣚⡮⢻⣿⣿⣇⣀⣉⣉⣉⣠⣤⢄⣀⣀⣈⠛⠛⡶⠻⣿⣿⣿⣿⣯⣬⢀⡴⠶⠂⣸⣿⡷⠐⠃⠃⠋⠀⠀⠭⠀⠀⠈⢳⢇⡒⠌⠋⠀⠀⠀⠀⠀⠠⠏⡐⠌⢂⠍⡠⠁⠌⠡⠉⡐⢉⠒⡆⠀⢠
⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢢⠧⡙⠆⠙⠃⠘⠋⠀⠀⠀⠘⠿⠿⠧⢀⠉⡒⢮⣽⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⠸⣫⣭⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⡔⢠⠐⠿⡿⠡⡟⠍⠠⢢⠙⡜⡰⢻⣄⠀⠈⣿⡷⠊⠀⢀⠀⠄⡐⠀⢠⠊⡐⢈⠂⠌⡐⠈⠄⡁⠐⠀⡀⠂⠰⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠠⢀⠐⡈⠄⠡⢈⠐⡀⠂⠄⡀⠀⠐⠘⡄⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣿⣎⣰⣿⣿⣯⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠇⠀⡐⡄⠰⡀⢀⠠⠀⠀⠄⠠⡑⢎⠄⠀⠀⡀⠄⠂⠄⠈⠀⡴⠂⠄⡀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢈⠐⠀⡈⢀⠁⡐⠠⠈⠄⡁⠂⠄⡁⠂⠄⡀⢇⠸⣿⣿⣿⣿⡿⣿⣿⣿⡁⢀⣿⣿⢹⣿⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⡘⢠⠤⣥⠇⢠⠅⢌⠠⠤⢤⠰⡄⠓⠈⡀⠄⢂⠡⠐⠀⠀⠀⡴⢁⠀⡀⢁⠈⠄⡁⠢⠐⢀⠠⠀⠀⠀⠀⠀⠀⠠⠀
⠀⠀⠀⠀⠀⠀⠈⠐⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠂⢀⠂⡐⢀⠂⠄⠡⢈⠐⡀⢁⠂⠄⡁⠂⠄⠘⡀⠻⣿⣿⠋⠀⣿⣿⡿⣠⣾⣿⣿⠾⣿⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⡿⢀⠃⠙⠊⠽⠆⠸⠀⠊⡔⠁⠂⢁⠠⢀⠡⠐⠈⠀⠀⠀⠀⢀⡼⡑⢈⡐⠐⡈⠐⡀⢂⠡⠈⠀⠄⠀⡁⠀⠂⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡀⢂⠠⠐⠀⠂⢈⠐⡀⢂⠐⠠⢈⠠⢀⠡⠈⠄⠈⠢⡈⠻⣿⣶⣶⣭⢁⡿⢫⣶⣮⠀⣻⣭⠝⣿⣿⡸⠟⣉⣻⣿⣿⠟⠁⢊⠀⡀⠂⠄⠠⠀⠐⠀⡀⠐⡈⠄⠂⠄⠂⠁⢀⠀⠀⠀⢀⡀⢀⠀⠂⠄⠡⢀⠡⠐⢀⠂⠁⡈⠀⠐⠀⠀⠄⠐⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠈⠡⢌⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠠⢀⠂⢁⠂⠄⡐⠀⠌⡀⠂⠄⠂⡐⠈⡐⠀⢡⠈⠣⣈⠻⢿⡟⣾⡇⢸⣿⡟⡀⣿⣿⠀⢸⣿⣧⢿⣿⡿⢋⠠⠈⡐⠄⢂⠀⠁⠈⠀⠂⡁⠂⠄⠡⠐⡈⠐⠀⠀⠁⠀⠀⠀⠀⠯⠐⠂⠌⠐⡈⠐⡀⠂⢈⠀⠄⠂⢀⠈⠀⠐⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠈⠨⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢁⠂⠌⡀⠄⢀⠂⠐⠠⠐⢈⠠⢀⠁⢂⠁⠄⠂⠄⠈⡄⢊⠔⡈⠳⡌⣸⡿⣤⣼⣿⠁⡄⣿⣿⣷⡜⣿⣿⡎⢫⠔⢁⠂⠡⢈⠠⠀⠄⠡⢈⠐⠀⠠⠁⠌⠠⢁⠐⠠⠀⠀⠀⠀⡀⠀⠄⡐⢀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⠀⠀⠐⠀⠀⠀⠀⠀⠀⢠⠄⠄⡠⢀⠀⠀⣀⣠⠀⠀⠀⠁⠐⠠⠀⢂⠀⡈⠄⡐⠠⢀⠈⠀⠐⠠⠈⡀⠂⠌⠐⠀⠐⡈⠄⠒⠤⠁⣰⣿⢇⣿⣿⣿⢈⠄⢻⣿⣿⣧⢿⣿⣯⡀⠠⢀⠂⠡⢀⠂⠡⢈⠐⠠⠈⢀⠂⠡⢈⠐⠠⠈⠄⠡⠈⠄⠡⢀⠁⢂⠀⡀⢂⡐⠠⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠈⠠⠀⠀⠀⠀⠸⡀⠂⠄⠡⡘⣬⠛⠁⠀⠀⠠⠐⠠⢀⠐⡀⠂⠄⡐⠀⢁⠠⠈⠄⡁⢂⠐⠠⠐⡀⢂⠐⠠⠐⡈⠐⡀⣼⣿⡿⣼⣿⣿⡟⠠⠂⠌⣿⣿⣿⡜⣿⣿⣷⡀⠂⠌⡐⠠⠈⠐⠀⠈⠀⠀⠠⢈⠐⠠⠈⠄⠡⠈⠄⠡⢈⠐⠠⠈⠄⡐⠀⢂⠀⡁⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠘⠄⠌⠰⠙⠀⠀⠀⠀⠌⠠⢁⠂⠄⠂⠄⡁⠂⠄⡁⠂⠄⠂⠄⡀⠂⢈⠀⡁⠐⠠⠈⠄⠡⢀⠡⠀⣿⡟⣴⣿⣿⣿⠃⠰⠁⢂⢹⣿⣿⣧⢻⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠂⠐⠠⠈⠄⠡⠈⠄⠁⠈⡐⠠⠈⠄⡁⠂⠄⡁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠌⠠⢁⠂⠌⠠⢁⠂⠄⡁⠂⠄⠡⢈⠐⠠⢀⠁⢂⠀⠀⠌⠀⡐⠈⠐⠀⢂⢰⡏⢸⣿⣿⣿⡟⠠⠁⠀⠂⠌⣿⣿⣿⡌⣿⣿⣿⣟⠢⠀⠄⠠⠀⠠⠐⠈⠄⢁⠂⠡⠈⠄⠁⢀⠀⠂⠄⠡⢈⠐⠠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢂⠈⠄⡁⠂⠈⠐⠀⠁⠈⠐⠀⠌⠐⠠⠈⠄⡈⠐⡀⢂⠀⠄⡈⢀⠀⣾⢃⠨⣿⣿⡿⠂⡁⠂⢁⠈⠄⢹⣿⣿⣷⡙⣿⣿⣯⠙⣂⠀⠁⢀⠂⠁⠄⢂⠀⠂⠐⠀⠠⠐⠠⢈⠐⡈⠐⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠐⠠⠁⡐⠠⢈⠐⡀⠂⡼⡏⣼⣻⣟⣯⠇⠐⡀⠠⠀⠂⠌⢸⡿⣽⢯⣷⣄⢻⡽⣿⢶⠀⠁⡀⠀⠁⠐⠀⢀⠂⠡⠈⠄⡁⠂⠄⠂⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜
⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠐⣰⠯⢑⣮⢗⡾⡓⢀⠡⠀⠄⡁⠂⠌⢸⡝⣯⢻⣼⢳⡎⢱⢯⡟⣆⠀⡀⠡⠀⠄⡀⢂⠠⠁⠈⠐⢀⠡⢈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡻⠄⡾⣹⢞⡵⠃⠈⠄⠐⡀⠡⠀⠐⡈⢷⡹⣞⡽⣎⢷⠈⢾⣱⠻⡄⠁⠂⠐⠠⠁⠌⠠⠀⠂⠄⢈⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢃⢥⡚⡵⣓⢮⠒⠠⢁⠂⠐⡀⠁⢂⠐⠠⠈⠳⣍⠶⡹⢎⣇⠨⢇⡻⡱⠌⠐⡀⢁⠈⡀⢁⠠⢈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⡁⣎⠶⣙⠲⣍⠂⠁⡐⢀⠲⠒⡄⢸⠡⠋⠒⠀⢁⠈⠷⣩⠳⡜⢦⡈⠵⣉⢏⡄⠐⢀⠂⡐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠤⢀⠲⣌⠲⣡⠓⡬⠀⢂⠀⠄⡐⠠⠘⠀⡀⠂⠄⡁⠂⠠⠑⠥⡓⢬⠣⡜⢢⠑⠪⡜⣡⢀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢓⠨⡐⢆⠢⠌⡄⠡⡉⠀⠐⡀⢀⠂⠄⠁⠄⠐⠠⠁⠂⠄⠡⠀⢂⠠⠉⠆⡓⡌⣃⠎⢢⠐⡁⠎⠰⢂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠠⢈⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢣⠘⡌⠱⡘⢌⡑⢊⡌⠱⠠⠄⣁⠀⡀⢈⠀⡈⠠⠀⢁⠤⡈⠤⡁⢄⡀⠀⠂⠐⡀⠑⠄⢪⢁⠎⡰⢁⠣⢄⠢⢄⡁⠄⠀⠀⠀⠀⠀⠁⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      """)

    elif player_move == "4" and turn_count >= 5 and ui_choice == "Satoru Gojo (Hollow Purple)":
      enemy_hp -= 300
      print("Satoru Gojo: Oh well.")
      time.sleep(1.5)
      print("             Guess I'll be a little rough.")
      time.sleep(1.5)
      print("             Cursed Technique Amplication: Blue.")
      time.sleep(2)
      print("             Cursed Technique Reversal: Red.")
      time.sleep(2)
      print("             Imaginary Technique:")
      time.sleep(1.5)
      print("             Hollow...")
      time.sleep(1.5)
      print("             Purple!")
      time.sleep(1.5)

    else:
      print("Please select a valid number")
      time.sleep(0.5)

    if enemy_hp <= 0:
      print("Congratulations, you won!")
      time.sleep(0.5)
      currency += 1500
      break

    enemy_attack = random.randint(1,3)
    if enemy_attack == 1:
      player_hp -= 10
      print("Opponent dealt 10 damage!")
      time.sleep(0.5)
    elif enemy_attack == 2:
      if random.random() <= 0.5:
        player_hp -= 20
        print("Opponent dealt 20 damage!")
        time.sleep(0.5)
      else:
        print("Opponent cursed technique missed!")
        time.sleep(0.5)
    elif enemy_attack == 3:
      if random.random() <= 0.3:
        player_hp -= 40
        print("Opponent has landed a BLACK FLASH!!")

    if player_hp <= 0:
      print("You lose!")
      time.sleep(0.5)
      break
  return currency

unlocked_characters = []
# runs code again after break
while True:
  table_title = "JJK Cursed Chronicles"
  title = f"{table_title:=^60}"
  print(title)
  print(f"Currency: {currency}")
  time.sleep(0.5)
  print("1. Gacha")
  time.sleep(0.5)
  print("2. Battle")
  time.sleep(0.5)
  print("3. Exit")
  time.sleep(0.5)
  ui = input("Choose an option: ")


  if ui == "1":
    currency, unlocked_characters, sr_characters, ssr_characters, UR_characters = gacha(currency)
  if ui == "2":
    currency = battle(currency, turn_count, sr_characters, ssr_characters, UR_characters)
  if ui == "3":
    print("Thank you for playing!")
    break

