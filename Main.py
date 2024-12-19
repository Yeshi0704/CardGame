from CardGame import CardGame

player1_name = input("Enter a name for player 1")
player2_name = input("Enter a name for player 2")
game = CardGame(player1_name, player2_name, 12)
print(f"The players for this games are:")
print(f"Player 1:{player1_name} with the cards :")
print(game.player_1.player_packet_cards)
print(f"Player 2:{player2_name} with the cards :")
print(game.player_2.player_packet_cards)
counter = 1  # counts the rounds
game.new_game()
for i in range(10):
    card_player_1 = game.player_1.get_card()
    card_player_2 = game.player_2.get_card()
    print(f"Round number : {counter}")
    print(f"{player1_name}'s card is {card_player_1}")
    print(f"{player2_name}'s card is {card_player_2}")
    if card_player_1 > card_player_2:
        print(f"The winner is Player 1: {player1_name}")
        game.player_1.add_card(card_player_2)
        game.player_1.add_card(card_player_1)
    else:
        print(f"The winner is Player 2: {player2_name}")
        game.player_2.add_card(card_player_2)
        game.player_2.add_card(card_player_1)
    counter += 1
print("!!!End Of The Game!!!")
print(f"The winner is: {game.get_winner()}")