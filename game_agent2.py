"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random

import math


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def heuristic3(game, player):
    """Uses the improve score heuristic but also gives points for positions in the board
    where the opponent player is less than 2 squares away from the border.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    location = game.get_player_location(player)
    borderx1_distance = min(max(2 - location[0], 0), 2)
    borderx2_distance = min(max(3 + location[0] - game.width, 0), 2)
    bordery1_distance = min(max(2 - location[1], 0), 2)
    bordery2_distance = min(max(3 + location[1] - game.height, 0), 2)

    total_player = borderx1_distance + borderx2_distance + bordery1_distance + bordery2_distance

    location = game.get_player_location(game.get_opponent(player))
    borderx1_distance = min(max(2 - location[0], 0), 2)
    borderx2_distance = min(max(3 + location[0] - game.width, 0), 2)
    bordery1_distance = min(max(2 - location[1], 0), 2)
    bordery2_distance = min(max(3 + location[1] - game.height, 0), 2)

    total_opponent = borderx1_distance + borderx2_distance + bordery1_distance + bordery2_distance

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves + total_opponent - total_player)


def heuristic2(game, player):
    """Uses the improve score heuristic but also gives points for positions in the board
    where the opponent player is less than 2 squares away from the border.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    location = game.get_player_location(game.get_opponent(player))
    borderx1_distance = min(max(2 - location[0], 0), 2)
    borderx2_distance = min(max(3 + location[0] - game.width, 0), 2)
    bordery1_distance = min(max(2 - location[1], 0), 2)
    bordery2_distance = min(max(3 + location[1] - game.height, 0), 2)

    total = borderx1_distance + borderx2_distance + bordery1_distance + bordery2_distance

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves + total)


def heuristic1(game, player):
    """Uses the improve score heuristic but also penalises positions in the board
    where the player is less than 2 squares away from the border.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    location = game.get_player_location(player)
    borderx1_distance = min(max(2 - location[0], 0), 2)
    borderx2_distance = min(max(3 + location[0] - game.width, 0), 2)
    bordery1_distance = min(max(2 - location[1], 0), 2)
    bordery2_distance = min(max(3 + location[1] - game.height, 0), 2)

    total = borderx1_distance + borderx2_distance + bordery1_distance + bordery2_distance

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves - total)


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    return heuristic3(game, player)


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)  This parameter should be ignored when iterative = True.

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).  When True, search_depth should
        be ignored and no limit to search depth.

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            DEPRECATED -- This argument will be removed in the next release

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves

        # Immediate returns
        # moves_available = game.get_legal_moves(self)
        moves_available = legal_moves
        if moves_available == 0:
            return -1, -1
        elif moves_available == 1:
            return moves_available[0]

        # Initial move (try center of the board)
        if game.get_player_location(self) is None:
            x = int(math.floor(game.width / 2))
            y = int(math.floor(game.height / 2))
            if game.move_is_legal((x, y)):
                return (x, y)
            elif game.move_is_legal((x - 1, y)):
                return (x - 1, y)
            elif game.move_is_legal((x, y - 1)):
                return (x, y - 1)
            elif game.move_is_legal((x + 1, y)):
                return (x + 1, y)
            elif game.move_is_legal((x, y + 1)):
                return (x, y + 1)

        # Init variables
        if self.method == 'minimax':
            current_method = self.minimax
        else:
            current_method = self.alphabeta

        current_solution = moves_available[0]
        current_score = float('-inf')

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.iterative:
                current_depth = 0
                while True:
                    new_score, new_solution = current_method(game, current_depth, maximizing_player=True)
                    current_score = new_score
                    current_solution = new_solution
                    current_depth += 1
            else:
                new_score, new_solution = current_method(game, self.search_depth, maximizing_player=True)
                return new_solution

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return current_solution

        # Return the best move from the last completed search iteration
        return current_solution

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!

        # Immediate returns
        if depth == 0:
            return self.score(game, self), game.get_player_location(self)

        current_solution = None
        current_score = float('-inf') if maximizing_player else float('inf')

        moves_available = game.get_legal_moves(self) if maximizing_player else game.get_legal_moves(
            game.get_opponent(self))
        for m in moves_available:
            new_board = game.forecast_move(m)
            new_score, new_solution = self.minimax(new_board, depth - 1, maximizing_player=not maximizing_player)
            if maximizing_player and new_score > current_score:
                current_score = new_score
                current_solution = m
            elif not maximizing_player and new_score < current_score:
                current_score = new_score
                current_solution = m

        return current_score, current_solution

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!
        # Immediate returns
        if depth == 0:
            return self.score(game, self), game.get_player_location(self)

        current_solution = None
        current_score = float('-inf') if maximizing_player else float('inf')

        moves_available = game.get_legal_moves(self) if maximizing_player else game.get_legal_moves(
            game.get_opponent(self))
        for m in moves_available:
            new_board = game.forecast_move(m)
            new_score, new_solution = self.alphabeta(new_board, depth - 1,
                                                     alpha=max(alpha, current_score) if maximizing_player else alpha,
                                                     beta=beta if maximizing_player else min(beta, current_score),
                                                     maximizing_player=not maximizing_player)
            if maximizing_player and new_score > current_score:
                current_score = new_score
                current_solution = m
                if current_score >= beta:
                    break
            elif not maximizing_player and new_score < current_score:
                current_score = new_score
                current_solution = m
                if current_score <= alpha:
                    break

        return current_score, current_solution
