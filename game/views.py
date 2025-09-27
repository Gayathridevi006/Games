import random
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "game.html")  # frontend template

def generate_matrix(request):
    rows, cols = 4, 4
    matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    return JsonResponse({"matrix": matrix})

@csrf_exempt
def find_paths(request):
    body = json.loads(request.body)
    matrix = body.get("matrix")
    target = body.get("target")

    rows, cols = len(matrix), len(matrix[0])
    result = []

    def backtrack(r, c, path, total, visited):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                path.append(matrix[nr][nc])
                backtrack(nr, nc, path, total + matrix[nr][nc], visited)
                path.pop()
                visited.remove((nr, nc))

    for i in range(rows):
        for j in range(cols):
            backtrack(i, j, [matrix[i][j]], matrix[i][j], {(i, j)})

    return JsonResponse({"paths": result})
