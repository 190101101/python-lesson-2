import random

game = {
	"stone": {
		"win": "scissor",
		"draw": "stone",
		"lose": "paper",
	},
	"scissor": {
		"win": "paper",
		"draw": "scissor",
		"lose": "stone",
	},
	"paper": {
		"win": "stone",
		"draw": "paper",
		"lose": "scissor",
	},
}

game_score = {
	"player": 0,
	"robot": 0,
	"draw": 0
}

#
while True:
	player = input(f"choice element: stone:1, scissor:2, paper:3 ")
	robot = random.randint(1,3)

	p1 = {1:"stone", 2:"scissor", 3:"paper"}

	player = player.replace(' ', '')

	if player == '' or player.isalpha() or not player.isalnum():
		print("Only number and 1,2,3")
		continue
	else:
		player = int(player)

	if type(player) != int:
		print("Only number and 1,2,3")
		continue


	if (len(p1)) < player:
		print("Only number and 1,2,3")
		continue

	player_choice = game.get(p1.get(player))
	robot_choice = game.get(p1.get(robot))

	if player_choice.get("win") == robot_choice.get("lose"):
		game_score["player"] = game_score["player"] + 1
		print(f"you win: {p1[player]} > {p1[robot]}")

	elif robot_choice.get("win") == player_choice.get("lose"):
		game_score["robot"] = game_score["robot"] + 1
		print(f"you lose: {p1[player]} < {p1[robot]}")

	elif robot_choice.get("draw") == player_choice.get("draw"):
		game_score["draw"] = game_score["draw"] + 1
		print(f"draw: {p1[player]} == {p1[robot]}")

	print(f"player: {game_score.get('player')} | robot: {game_score.get('robot')} | draw: {game_score.get('draw')}\n")

	if game_score["player"] == 10:
		print("the game is over and you win \n ") 
		break

	if game_score["robot"] == 10:
		print("the game is over and robot win \n ") 
		break

	if game_score["draw"] == 10:
		print("the game is over status:draw \n ") 
		break
