// Problem description: Miriam and Alejandro are playing a card game with a deck of custom cards, each of which contains a single number of it, with numbers possibly duplicated across multiple cards and negative numbers allowed. To begin the game, the first player draws the top card from the deck and adds its face value to their score. If the value of the card is a multiple of 3, then the deck is flipped, such that the second player draws a card from what was previously the bottom of the deck; if the value is not a multiple of 3, the deck stays in its current orientation. This continues back-and-forth until all cards have been drawn, at which point the player with the highest score wins. Note that the deck may not initially have an even number of cards, so it is possible for the first player to draw one card more than the second player over the course of the game. It is also possible for the players to draw/tie.
// Problem statement: Assume that Miriam always draws the first card. Implement the following function in the code editor to compute the difference between Miriam's score and Alejandro's score at the conclusion of the game. The function should take in the following arguments: (const std::vector<int & deck)

#include <iostream>
#include <vector>

int computeScoreDifference(const std::vector<int> &deck)
{
    int miriamScore = 0;
    int alejandroScore = 0;
    bool isMiriamTurn = true;
    int front = 0;
    int back = deck.size() - 1;
    bool isFront = true;
    for (int i = 0; i < deck.size(); i++)
    {
        int toAdd = 0;

        if (isFront)
        {
            toAdd = deck[front];
            front++;
        }
        else
        {
            toAdd = deck[back];
            back--;
        }
        if (toAdd % 3 == 0)
        {
            isFront = !isFront;
        }
        if (isMiriamTurn)
        {
            miriamScore += toAdd;
        }
        else
        {
            alejandroScore += toAdd;
        }
        isMiriamTurn = !isMiriamTurn;
    }
    return miriamScore - alejandroScore;
}

int main()
{
    // Write C++ code here
    std::vector<int> deck = {3, 7, 2, 6, 5};
    std::cout << computeScoreDifference(deck);

    return 0;
}