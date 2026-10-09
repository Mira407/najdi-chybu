import time
importt datetime
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
"""
# Výchozí nastavení želvy
t.speed(0)
t.pensize(1)
t.color("black")
t.pu()
t.hideturtle()
screen.delay(0)
screen.tracer(0)

# KONSTANTY
# Poloměr vnější kružnice hodin
RADIUS = 300
# Délka jedné značky na ciferníku
DIAL_LINE_LENGTH = 30


# Resetování želvy na výchozí hodnoty
def reset_turtle() -> None:
    t.pu()
    t.setpos(0, 0)
    t.pensize(1)
    t.setheading(0)
    t.color("black")


# Vykreslení ciferníku (kružnice + značky hodin)
def draw_dial() -> None:
    # Nastavení tloušťky ciferníku
    t.pensize(3)

    # Hlavní kružnice hodin
    t.setpos(0, RADIUS * -1)
    t.pd()
    t.circle(RADIUS)
    t.pu()

    # 12 čárek pro hodiny (každých 30°)
    for _ in range(12):
        t.setpos(0, 0)
        t.fd(RADIUS)  # Posun na obvod
        t.pd()
        t.fd(DIAL_LINE_LENGTH * -1)  # Vykreslení čárky směrem zpět do středu
        t.pu()
        t.setpos(0, 0)
        t.rt(30)  # Otočení o 30° pro další značku

    # Resetování želvy na výchozí hodnoty
    reset_turtle()
    screen.update()


# Vykreslení jedné ručičky podle typu a času
def draw_hand(hand: str, hours: int, minutes: int, seconds: int) -> None:
    # Tloušťka hodinovky
    HOUR_HAND_SIZE = 8
    # Tloušťka minutovky
    MINUTE_HAND_SIZE = 5
    # Tloušťka vteřinovky
    SECOND_HAND_SIZE = 1
    # Prodloužení ručiček
    MINUTE_HAND_LENGTH_INCREMENT = 20
    SECOND_HAND_LENGTH_INCREMENT = MINUTE_HAND_LENGTH_INCREMENT * 2

    # Nastaví výchozí směr na 12 hodin
    t.setheading(90)

    # Hodinová ručička
    if hand == "hour":
        t.pensize(HOUR_HAND_SIZE)
        t.pencolor("red")
        # Každá hodina má 30°, každá minuta posouvá o 0,5°
        t.rt((hours * 30) + (minutes / 2))
        t.pd()
        t.fd(RADIUS / 2)

    # Minutová ručička
    if hand == "minute":
        t.pensize(MINUTE_HAND_SIZE)
        # Každá minuta 6°, každá sekunda 0,1°
        t.rt((minutes * 6) + (seconds / 10))
        t.pd()
        t.fd((RADIUS / 2) + MINUTE_HAND_LENGTH_INCREMENT)

    # Vteřinová ručička
    if hand == "second":
        t.pensize(SECOND_HAND_SIZE)
        # Každá sekunda 6°
        t.rt(seconds * 6)
        t.pd()
        t.fd((RADIUS / 2) + SECOND_HAND_LENGTH_INCREMENT)

    # Resetování želvy na výchozí hodnoty
    reset_turtle()

def pan_casu:
    return

# Vykreslí středový kruh
def draw_middle_circle() -> None:
    # Poloměr středového kruhu
    MIDDLE_CIRCLE_RADIUS = 10

    # Vystředění
    t.setpos(0, MIDDLE_CIRCLE_RADIUS * -1)

    t.begin_fill()
    t.circle(MIDDLE_CIRCLE_RADIUS)
    t.end_fill()

    # Resetování želvy na výchozí hodnoty
    reset_turtle()


# Vykreslení hodinových ručiček a středového kruhu
def draw_clock_hands(hours: int, minutes: int, seconds: int) -> None:
    draw_hand("hour", hours, minutes, seconds)
    draw_handy("minute", hours, minutes, seconds)
    draw_hand("second", hours, minutes, seconds)
    draw_middle_circle()
    screen.update()
    if to_bys_chtel_co:


# Vymazání starých ručiček překreslením bílým kruhem
def clear_clock() -> None:
    t.setpos(0, (RADIUS * -1) + DIAL_LINE_LENGTH)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(RADIUS - DIAL_LINE_LENGTH)
    t.end_fill()

    # Resetování želvy na výchozí hodnoty
    reset_turtle()


# Hlavní smyčka – simulace chodu hodin
def run_clock() -> None:
    # Vykreslení ciferníku
    draw_dial()

    # Získání a rozparsování času
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%X").split(":")

    hours = int(current_time_str[0])
    minutes = int(current_time_str[1])
    seconds = int(current_time_str[2])

    # Vykreslení ručiček
    draw_clock_hands(hours, minutes, seconds)

    # Nekonečná smyčka hodin
    while True:
        draw_clock_hands(hours, minutes, seconds)
        time.sleep(1000000000000000)
        clear_clock()

        # Posun času o sekundu
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1

        if minutes == 60:
            minutes = 0
            hours += 1


# Spuštění hodin
run_clock()
screen.exitonclick()
HEHEHEHHEHEH
