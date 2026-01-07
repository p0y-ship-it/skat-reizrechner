def jack_available(name):
    while True:
        input_var = input(f"{name} vorhanden? (Y/N): ").strip().lower()
        if input_var in ("y", "yes"):
            return 1
        elif input_var in ("n", "no"):
            return 0
        else:
            print("Bitte nur Y oder N eingeben.")

def game_color():
    while True:
        input_var = input("Welches Farben-Spiel? Schellen (S), Herz (H), Blatt (B), Eichel (E), Grand (G), Null (N): ").strip().lower()
        if input_var in ("s", "schellen"):
            return "diamonds"
        elif input_var in ("h", "herz"):
            return "hearts"
        elif input_var in ("b", "blatt"):
            return "clubs"
        elif input_var in ("e", "eichel"):
            return "spades"
        elif input_var in ("g", "grand"):
            return "grand"
        elif input_var in ("n", "null"):
            return "zero"
        else:
            print("Bitte nur gültige Farben eingeben.")

def multiplicator_input(name):
    while True:
        input_var = input(f"{name}? (Y/N): ").strip().lower()
        if input_var in ("y", "yes"):
            return 1
        elif input_var in ("n", "no"):
            return 0
        else:
            print("Bitte nur Y oder N eingeben.")

def multiplicator(color):
    count = 0
    if multiplicator_input("Handspiel") == 1:
        count += 1
        hand = "Hand"
    else:
        hand = ""
    
    if multiplicator_input("Schneider") == 1:
        count += 1
        tailor = "Schneider"
        if multiplicator_input("Schwarz") == 1:
            count += 1
            black = "Schwarz"
            tailor = ""
    else:
        tailor = ""
        black = ""
        
    if multiplicator_input("Ouvert") == 1:
        count += 1
        ouvert = "Ouvert"
    else:
        ouvert = ""
    
    if color != "grand":
        if multiplicator_input("Spitze") == 1:
            count += 1
            spitze = "Spitze"
        else:
            spitze = ""
    else:
            spitze = ""
    
    return count, hand, tailor, black, ouvert, spitze

def zero_value():
    count = 0
    if multiplicator_input("Handspiel") == 1:
        count += 1
        hand = "Hand"
    else:
        hand = ""
    if multiplicator_input("Ouvert") == 1:
        count += 1
        ouvert = "Ouvert"
    else:
        ouvert = ""
    if hand and ouvert:
        count = 59
    elif ouvert:
        count = 46
    elif hand:
        count = 35
    else:
        count = 23
    return count, hand, "", "", ouvert, ""

def with_jack(jacks):
    count = 0
    for x in jacks:
        if x == 1:
          count += 1
          if count == 4:
              return count + 1
        else:
          count += 1
          return count

def without_jack(jacks):
    count = 0
    for x in jacks:
        if x == 0:
          count += 1
          if count == 4:
              return count + 1
        else:
          count += 1
          return count

def main():
    possible_steps = [
        18, 20, 22, 23, 24, 27, 30, 33, 35, 36, 40, 44, 45,
        46, 48, 50, 54, 55, 59, 60, 63, 66, 70, 72, 77, 80,
        81, 84, 88, 90, 96, 99, 102, 108, 110, 120, 121, 126,
        132, 135, 140, 143, 144, 150, 153, 154, 160, 162, 165,
        168, 170, 176, 180, 187, 192, 198, 200, 204, 216, 240,
        264
    ]
    DiamondsJack = jack_available("Karo-Bube / Schellen-Bube")
    HeartsJack  = jack_available("Herz-Bube / Herz-Bube")
    ClubsJack   = jack_available("Pik-Bube / Blatt-Bube")
    SpadesJack   = jack_available("Kreuz-Bube / Eichel-Bube") 

    jacks = [SpadesJack, ClubsJack, HeartsJack, DiamondsJack]
    color = game_color()
    if color == "zero":
        color_value, hand, tailor, black, ouvert, spitze = zero_value()
        color_name = "Null"
    else:
        multiplicator_count, hand, tailor, black, ouvert, spitze = multiplicator(color)

    if color == "diamonds":
        color_value = 9
        color_name = "Schellen"
    elif color == "hearts":
        color_value = 10
        color_name = "Herz"
    elif color == "clubs":
        color_value = 11
        color_name = "Blatt"
    elif color == "spades":
        color_value = 12
        color_name = "Eichel"
    elif color == "grand":
        color_value = 24
        color_name = "Grand"

    if SpadesJack == 0:
        jack_count = without_jack(jacks)
        final = f"ohne {jack_count - 1} spiel {jack_count}, {color_name}" 
    else:
        jack_count = with_jack(jacks)
        final = f"mit {jack_count - 1} spiel {jack_count}, {color_name}"
    if hand:
        final += f", {hand}"
    if tailor:
        final += f", {tailor}"
    if black:
        final += f", {black}"
    if ouvert:
        final += f", {ouvert}"
    if spitze:
        final += f", {spitze}"
    if color == "zero":
        points = color_value
    else:
        points = color_value * (jack_count + multiplicator_count)
    if points > 264:
        points = 264
    steps = [step for step in possible_steps if step <= points]
    final += f" => Punkte: {points}"
    print(f"{final}\n Reizschritte: {', '.join(map(str, steps))}")

if __name__ == "__main__":
    main()