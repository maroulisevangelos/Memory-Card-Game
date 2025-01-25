# Memory-Card-Game

This project is a variation of the classic memory card game implemented in Python. The game supports 2 or more players and uses a deck of 52 cards (spades, hearts, diamonds, clubs) with ranks 1-10 and face cards (J, Q, K). Players take turns flipping pairs of cards, earning points for matches based on predefined rules.

Features:

  Difficulty Levels:
    Easy: 16 cards (only face cards and 10) arranged in a 4x4 grid.
    Medium: 40 cards (numbers only) in a 4x10 grid.
    Hard: Full 52-card deck in a 4x13 grid.
    
  Special Card Rules:
    Two Jacks: Earn points and play again.
    Two Kings: Earn points, and the next player skips their turn.
    Queen + King: Flip a third card for bonus points if matches are found.
    
  Bonus Mode: Option to score points for matching cards of the same suit.
  
  User-Friendly Input Validation: Ensures valid moves and prevents errors like selecting already opened cards.
  
  Interactive Display: Cards initially revealed for easy memorization before starting the game.
  
Enjoy testing your memory and strategy in this enhanced multiplayer card game!

I recommend you to use Python IDLE and type playgame().
