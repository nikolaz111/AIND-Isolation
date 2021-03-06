"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Uses the improve score heuristic but also gives points for positions in the board
    where the opponent player is less than 2 squares away from the border.

    Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

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


def custom_score_2(game, player):
    """Uses the improve score heuristic but also gives points for positions in the board
    where the opponent player is less than 2 squares away from the border.

    Calculate the heuristic value of a game state from the point of view
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


def custom_score_3(game, player):
    """Uses the improve score heuristic but also penalises positions in the board
    where the player is less than 2 squares away from the border.

    Calculate the heuristic value of a game state from the point of view
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


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

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

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        current_solution = (-1, -1)
        current_score = float('-inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            new_score = self.min_value(new_board, depth - 1)
            if new_score > current_score:
                current_score = new_score
                current_solution = m

        return current_solution

    def max_value(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(depth):
            return self.score(game, self)

        current_score = float('-inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            current_score = max(current_score, self.min_value(new_board, depth - 1))
        return current_score

    def min_value(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(depth):
            return self.score(game, self)

        current_score = float('inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            current_score = min(current_score, self.max_value(new_board, depth - 1))
        return current_score


    def terminal_test(self, depth):
        if depth == 0:
            return True
        else:
            return False




class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

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

        best_move = (-1, -1)

        try:
            depth = 0
            while True:
                depth += 1
                best_move = self.alphabeta(game, depth=depth)
        except SearchTimeout:
            # Handle any actions required at timeout, if necessary
            pass

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

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

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        current_solution = (-1, -1)
        current_score = float('-inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            current_score = self.min_value(new_board, depth - 1, alpha, beta)
            if current_score > alpha:
                current_solution = m
                alpha = current_score

        return current_solution


    def max_value(self, game, depth, alpha, beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(depth):
            return self.score(game, self)

        current_score = float('-inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            current_score = max(current_score, self.min_value(new_board, depth - 1, alpha, beta))
            if current_score >= beta:
                return current_score
            alpha = max(alpha, current_score)

        return current_score


    def min_value(self, game, depth, alpha, beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(depth):
            return self.score(game, self)

        current_score = float('inf')
        for m in game.get_legal_moves():
            new_board = game.forecast_move(m)
            current_score = min(current_score, self.max_value(new_board, depth - 1, alpha, beta))
            if current_score <= alpha:
                return current_score
            beta = min(beta, current_score)

        return current_score


    def terminal_test(self, depth):
        if depth == 0:
            return True
        else:
            return False
