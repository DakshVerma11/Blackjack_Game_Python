# Blackjack_Game_Python
A Python code to play the BlackJack game of cards


Welcome to the Blackjack game! This simple console-based game allows you to play the classic card game of Blackjack against the computerized dealer.

## Table of Contents

1. [Introduction](#introduction)
2. [Game Rules](#game-rules)
3. [How to Run](#how-to-run)
4. [Classes and Functions](#classes-and-functions)
5. [Gameplay](#gameplay)
6. [Acknowledgments](#acknowledgments)

## Introduction

This Python script implements a basic Blackjack game using the console. The game provides a text-based interface where you can place bets, hit, stand, and play against the dealer.

## Game Rules

The rules of Blackjack are simple:
- The goal is to get as close to 21 points without going over.
- Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces can be worth 1 or 11.
- The dealer hits until reaching a total of 17 or higher.
- If a player or the dealer exceeds 21 points, they bust and lose the round.

## How to Run

To run the game, simply execute the provided Python script. The game will prompt you to place bets, make decisions (hit or stand), and play rounds against the dealer. Follow the on-screen instructions to interact with the game.

## Classes and Functions

The script consists of several classes and functions:

- **Card**: Represents a playing card with a suit, rank, and point value.
- **Deck**: Represents a deck of cards with methods for shuffling and dealing.
- **Player**: Represents a player with methods for adding cards, adjusting for Aces, and playing cards.
- **Chips**: Represents the player's chips for betting, with methods for winning and losing bets.
- Various utility functions for gameplay, such as `bet`, `hit`, `hit_or_stand`, and result-handling functions.

## Gameplay

1. **Initialization**: The game starts with the player having 100 chips.
2. **Betting**: The player is prompted to place a bet.
3. **Dealing**: The deck is shuffled, and each player (player and dealer) is dealt two cards.
4. **Player's Turn**: The player decides whether to hit or stand to get closer to 21.
5. **Dealer's Turn**: The dealer plays its hand, hitting until reaching 17 or higher.
6. **Result**: The winner is determined based on the total points without exceeding 21.
7. **Repeat or Quit**: The player can choose to play another round or exit the game.
