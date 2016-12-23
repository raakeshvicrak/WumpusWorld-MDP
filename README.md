# WumpusWorld-MDP

A Wumpus world is characterised by the locations of the walls,
pits and Wumpus, gold and starting square of the agent.

The actions are A = {do nothing, left, right, up, down, shoot left, shoot right, shoot up, shoot down}.

If the agent shoots, then the arrow moves until it either hits a wall or the Wumpus. The
Wumpus is killed if hit and the agent has only one arrow (so can only shoot once).

If the agent moves, then with probability 0.9 it moves one square in the intended direction
and with probability 0.1 it moves uniformly at random in one of the three other directions.

If the agent moves into a wall, then it is moved back to its location prior to hitting the wall.

If the agent does nothing, then nothing changes.

If the agent moves into a living Wumpus or a pit, then it suffers -100 utility indefinitely. If
the agent finds the gold, then it receives 100 utils indefinitely. The reward for being in every
other state is -1 util.
