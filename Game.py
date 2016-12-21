from Hand import Hand
from Deck import Deck

print 'Welcome to Casino Royale!'

new_deck = Deck()

player = Hand()
dealer = Hand()

player.add_card(new_deck.draw_card())
player.add_card(new_deck.draw_card())

dealer.add_card(new_deck.draw_card())



while not player.is_busted():

    player.print_hand()
    dealer.print_hand()

    if player.get_score() == 21:
        print 'You hit blackjack!'
        break

    action = raw_input('Hit Or Stay: ').lower()

    if action == 'hit' or action == 'h':
        player.add_card(new_deck.draw_card())

        if player.is_busted():
            print 'You busted! You have', str(player.get_score()), 'which is over 21!'
            break
    else:
        while dealer.get_score() < 17:
            dealer.add_card(new_deck.draw_card())
            dealer.print_hand()

        if dealer.get_score() > 21 or dealer.get_score() < player.get_score():
            print 'You won with a score of ' + str(player.get_score()) + '! Dealer had ' + str(dealer.get_score()) + '.'
        else:
            print 'You lost! You have ' + str(player.get_score()) + ' to the dealer\'s ' + str(dealer.get_score()) + '.'

        break