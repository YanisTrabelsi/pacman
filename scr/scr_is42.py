from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def get42_cells(grid) -> list[tuple[int, int]]:
    arr_cell_42: list[tuple[int, int]] = []
    cell_size: int = gconf.cell
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            cell_42: tuple[int, int] = (0, 0)
            if cell == 15:
                cell_42 = (j * cell_size, i * cell_size)
                arr_cell_42.append(cell_42)

    return arr_cell_42
