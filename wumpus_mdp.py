import solver;

class WumpusMDP:
  # wall_locations is a list of (x,y) pairs
  # pit_locations is a list of (x,y) pairs
  # wumnpus_location is an (x,y) pair
  # gold_location is an (x,y) pair
  # start_location is an (x,y) pair representing the start location of the agent


  def __init__(self, wall_locations, pit_locations, wumpus_location, gold_location, start_location):
    self.actions = ["do nothing", "left", "right", "up", "down", "shoot left", "shoot right", "shoot up", "shoot down"];

    self.arrow_count = 1;

    self.states = [];
    self.define_states_space(wall_locations);

    self.pit_locations = pit_locations;
    self.gold_location = gold_location;
    self.start_location = start_location;
    self.wall_locations = wall_locations;
    self.wumpus_location = wumpus_location;

  def define_states_space(self, wall_locations):
    max_number_of_rows = 0;
    max_number_of_columns = 0;

    min_number_of_rows = 0;
    min_number_of_columns = 0;

    if len(wall_locations) > 0:
      min_number_of_rows = wall_locations[0][0];
      min_number_of_columns = wall_locations[0][1];
    
    for wall_locations_temp in wall_locations:
      if max_number_of_rows < wall_locations_temp[0]:
        max_number_of_rows = wall_locations_temp[0];
      if max_number_of_columns < wall_locations_temp[1]:
        max_number_of_columns = wall_locations_temp[1];
      if min_number_of_rows > wall_locations_temp[0]:
        min_number_of_rows = wall_locations_temp[0];
      if min_number_of_columns > wall_locations_temp[1]:
        min_number_of_columns = wall_locations_temp[1];
      
    #print(max_number_of_rows, " ", max_number_of_columns);
    #print(min_number_of_rows, " ", min_number_of_columns);

    for rows_count in range(min_number_of_rows, (max_number_of_rows + 1)):
      for columns_count in range(min_number_of_columns, (max_number_of_columns + 1)):
        self.states.append((rows_count, columns_count));

    #print(self.states);
    
    
  def A(self):
    # return list of actions
    return self.actions;

  def S(self):
    # return list of states
    return self.states;

  def P(self, s, a, u):
    # return probability of transitioning from state s to state u when taking action a:
    #print(s);

    #print(s, " a ", a, " u ", u);

    #calculating transition probability when the target and initial state are both the same:
    if s == u:
      #print("s = u");
      #calculating transition probability when the action is to shoot an arrow:
      if a == self.actions[7]:
        if self.wumpus_location != None:
          if self.wumpus_location[1] == s[1] and self.wumpus_location[0] < s[0]:
            self.wumpus_location = None;
            return 0.9;
      elif a == self.actions[8]:
        if self.wumpus_location != None:
          if self.wumpus_location[1] == s[1] and self.wumpus_location[0] > s[0]:
            self.wumpus_location = None;
            return 0.9;
      elif a == self.actions[6]:
        if self.wumpus_location != None:
          if self.wumpus_location[0] == s[0] and self.wumpus_location[1] > s[1]:
            self.wumpus_location = None;
            return 0.9;
      elif a == self.actions[5]:
        if self.wumpus_location != None:
          if self.wumpus_location[0] == s[0] and self.wumpus_location[1] < s[1]:
            self.wumpus_location = None;
            return 0.9;
      else:
        return 0;
    #calculating transition probability when the target and initial state are not the same:
    elif s != u:
      #print("s != u");
      
      if a == self.actions[1] and u[1] == (s[1] - 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0.1;
      if a == self.actions[1] and u[1] == (s[1] + 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0;
      if a == self.actions[2] and u[1] == (s[1] + 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0.1;
      if a == self.actions[2] and u[1] == (s[1] - 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0;

      if a == self.actions[3] and u[0] == (s[0] - 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0.1;
      if a == self.actions[3] and u[0] == (s[0] + 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0;
      if a == self.actions[4] and u[0] == (s[0] + 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0.1;
      if a == self.actions[4] and u[0] == (s[0] - 1):
        if ((self.wumpus_location == u) or (u in self.pit_locations)):
          return 0;
        elif self.gold_location == u:
          return 0.9;
        return 0;
    #print("here");
    return 0;
    
  def R(self, s):
    # return reward for state s
    if ((s in self.pit_locations) or (s == self.wumpus_location)):
      return -100;
    elif s == self.gold_location:
      return 100;
    else:
      return -1;

  def initial_state(self):
    # return initial state
    return self.start_location;

  def gamma(self):
    return 0.99

# EXAMPLE USAGE:

mdp = WumpusMDP([(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(0,2),(0,1)], [(1,2)], (2,1), (2,2), (1,1));
s = solver.Solver(mdp)
policy = s.solve()

print("policy ", policy);

