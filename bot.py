import checker

while True:
    tournamentId = input("Enter tournament id: ")
    if tournamentId != '':
        break

while True:
    minimumGames = int(input("Enter positive minimum number of games (usually 8): "))
    if minimumGames > 0:
        break

while True:
    minimumMoves = int(input("Enter minimum number of two-side moves (usually 10): "))
    if minimumMoves >= 0:
        break

while True:
    columnName = input("Enter name for new column for this tournament in the spreadsheet: ")
    if len(columnName) > 0:
        break

checker.check(tournamentId, minimumGames, minimumMoves, columnName)
