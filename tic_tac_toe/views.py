from django.shortcuts import render, redirect

# Initialize empty board
def empty_board():
    return [["" for _ in range(3)] for _ in range(3)]

# Check for winner
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def tic_tac_toe_view(request):
    # Start or reset game
    if "start" in request.GET:
        request.session["board"] = empty_board()
        request.session["player"] = "X"
        request.session["winner"] = None
        request.session.modified = True
        return redirect("tic_tac_toe_view")  # Redirect to same page without ?start=1
    if "reset" in request.GET:
        request.session.flush()
        return redirect("home")  # Redirect to same page without ?reset=1

    board = request.session.get("board", empty_board())
    player = request.session.get("player", "X")
    winner = request.session.get("winner", None)

    # Handle a move
    if request.method == "POST" and not winner:
        row = int(request.POST.get("row"))
        col = int(request.POST.get("col"))
        if board[row][col] == "":
            board[row][col] = player
            winner = check_winner(board)
            request.session["winner"] = winner
            request.session["player"] = "O" if player == "X" else "X"
            request.session.modified = True

    # Check if game has started
    game_started = "board" in request.session and any(cell for row in board for cell in row) or not winner

    context = {
        "board": board,
        "player": player,
        "winner": winner,
        "game_started": game_started,  # pass this to template
    }
    return render(request, "game_2.html", context)
