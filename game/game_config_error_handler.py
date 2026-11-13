def check_data(d: dict) -> dict:
    data: str = ""

    # highscore_filename
    data = "highscore_filename"
    try:
        if not isinstance(d[data], str) or len(d[data]) < 1:
            d[data] = "highs_score.txt"
    except KeyError:
        d[data] = "highs_score.txt"

    # width
    data = "width"
    try:
        if not isinstance(d[data], int) or d[data] < 10 or d[data] > 48:
            d[data] = 20
    except KeyError:
        d[data] = 20

    # height
    data = "height"
    try:
        if not isinstance(d[data], int) or d[data] < 8 or d[data] > 25:
            d[data] = 15
    except KeyError:
        d[data] = 15

    # lives
    data = "lives"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 3
    except KeyError:
        d[data] = 3

    # pacgum
    data = "pacgum"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 42
    except KeyError:
        d[data] = 42

    # points_per_pacgum
    data = "points_per_pacgum"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 10
    except KeyError:
        d[data] = 10

    # points_per_super_pacgum
    data = "points_per_super_pacgum"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 50
    except KeyError:
        d[data] = 50

    # points_per_ghost
    data = "points_per_ghost"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 200
    except KeyError:
        d[data] = 200

    # seed
    data = "seed"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 42
    except KeyError:
        d[data] = 42

    # level_max_time
    data = "level_max_time"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 90
    except KeyError:
        d[data] = 90

    # cell
    data = "cell"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 40
    except KeyError:
        d[data] = 40

    # speed
    data = "speed"
    try:
        if not isinstance(d[data], int) or d[data] < 0:
            d[data] = 5
    except KeyError:
        d[data] = 5

    # pacman_spawn_x
    data = "pacman_spawn_x"
    try:
        if not isinstance(d[data], int):
            d[data] = 9
        elif not isinstance(d[data], int) or d[data] < 0 or d[data] > d["width"] - 1:
            d[data] = 9
    except KeyError:
        d[data] = 9

    # pacman_spawn_y
    data = "pacman_spawn_y"
    try:
        if not isinstance(d[data], int):
            d[data] = 8
        elif not isinstance(d[data], int) or d[data] < 0 or d[data] > d["height"] - 1:
            d[data] = 8
    except KeyError:
        d[data] = 8

    # ghosts_spawn_x
    data = "ghosts_spawn_x"
    try:
        if not isinstance(d[data], int):
            d[data] = 0
        elif not isinstance(d[data], int) or d[data] < 0 or d[data] > d["width"] - 1:
            d[data] = 0
    except KeyError:
        d[data] = 0

    # ghosts_spawn_y
    data = "ghosts_spawn_y"
    try:
        if not isinstance(d[data], int):
            d[data] = 0
        elif not isinstance(d[data], int) or d[data] < 0 or d[data] > d["height"] - 1:
            d[data] = 0
    except KeyError:
        d[data] = 0

    return d
