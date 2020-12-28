from utils import * 

if __name__ == '__main__':
  grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
  grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
  grid3  = '.54.3.2...1.7.....3.2..8...9...5....2.3...4.8....2...3...2..5.1.....9.7...8.1.62.'
  hard1  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'

  puzz1 = '8769......1...6....4.3.58..4.....21..9.5......5..4.3.6.29.....8..469.173.....1..4'
  puz1 = [[8, 7, 6, 9, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 6, 0, 0, 0],
            [0, 4, 0, 3, 0, 5, 8, 0, 0],
            [4, 0, 0, 0, 0, 0, 2, 1, 0],
            [0, 9, 0, 5, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 4, 0, 3, 0, 6],
            [0, 2, 9, 0, 0, 0, 0, 0, 8],
            [0, 0, 4, 6, 9, 0, 1, 7, 3],
            [0, 0, 0, 0, 0, 1, 0, 0, 4]]

  puzzle=grid_to_puzzle(grid3)

  print_board(puzzle)
  for itrations in range(0, 10):
    zones = extract_zones(puzzle)
    for zone in zones:
      if zone["type"] == "row":
        row = zone["coord"]
        for col in range(0, 9):
          insert_possibilities(puzzle, row, col)
      elif zone["type"] == "col":
        col = zone["coord"]
        for row in range(0, 9):
          insert_possibilities(puzzle, row, col)
      else:
        row_begin = zone["coord"][0]
        row_end = zone["coord"][1]
        col_begin = zone["coord"][2]
        col_end = zone["coord"][3]
        for row in range(row_begin, row_end+1):
          for col in range(col_begin, col_end+1):
            insert_possibilities(puzzle, row, col)
  
  print("=" * 50)
  print_board(puzzle)


