import random

class Solver:
  def __init__(self, mdp):
    # any initialisation you might like
    self.mdp = mdp;
    self.value_function = [];

    self.initialize_value_function();
    #print("Value Function: ", self.value_function);

    self.is_list_of_list = False;
    
  def initialize_value_function(self):
    list_of_states = self.mdp.S();
    for individual_list in list_of_states:
      if isinstance(individual_list, int):
        is_list_of_list = False;
      else:
        is_list_of_list = True;

    #print("is list of list ", is_list_of_list);
    #is_list_of_list = all(isinstance(individual_list, ) for individual_list in list_of_states);
    if is_list_of_list:
      self.is_list_of_list = True;
##      for individual_list in list_of_states:
##        temp_list = [];
##        for individual_items in individual_list:
##          temp_list.append(0);
##        self.value_function.append(temp_list);
      for individual_items in list_of_states:
        self.value_function.append(0);
    else:
      self.is_list_of_list = False;
      for individual_items in list_of_states:
        self.value_function.append(0);

  def get_neighbours(self, row, column, possible_actions):
    neighbours_list = [];
    neighbours_actions = [];

    #if (((row + 1) < len(self.value_function)) and ((row + 1) >= 0)):
    neighbours_list.append((row + 1) + " " + column);
    nejghbours_actions.append("down");
    #if (((row - 1) < len(self.value_function)) and ((row - 1) >= 0)):
    neighbours_list.append((row - 1) + " " + column);
    nejghbours_actions.append("up");
    #if (((column + 1) < len(self.value_function[0])) and ((column + 1) >= 0)):
    neighbours_list.append(row + " " + (column + 1));
    nejghbours_actions.append("right");
    #if (((column - 1) < len(self.value_function[0])) and ((column - 1) >= 0)):
    neighbours_list.append(row + " " + (column - 1));
    nejghbours_actions.append("left");

    return neighbours_list, neighbours_actions;
    
  def get_neighbours(self, row, possible_actions):
    neighbours_list = [];
    neighbours_actions = [];

    #if (((row + 1) < len(self.value_function)) and ((row + 1) >= 0)):
    neighbours_list.append((row + 1));
    neighbours_actions.append("right");
    #if (((row - 1) < len(self.value_function)) and ((row - 1) >= 0)):
    neighbours_list.append((row - 1));
    neighbours_actions.append("left");
      
    return neighbours_list, neighbours_actions;
  
  def calculate_value_function_iterative(self):

    possible_actions = self.mdp.A();
    state_space = self.mdp.S();
    
    neighbours_list = [];
    neighbours_actions = [];
    delta_too_small = False;
    #temp = 0;
    iterations = 0;
    temp = 0; 
    
    while True:
      temp = temp + 1;
      iterations = iterations + 1;
      #print(iterations);
      #temp = temp + 1;
      #check if it's list_of_list:
      if self.is_list_of_list == True:
        
        for individual_list_count in range(0, len(self.value_function)):
          #for individual_item_count in range(0, len(self.value_function[individual_list])):
          neighbours_list =[];
          neighbours_actions = [];
          
          #get the neighbours of this current state:
          #neighbours_list, neighbours_actions = self.get_neighbours(individual_list_count, individual_item_count, possible_actions);

          value_function_neighbour_states = [];
          value_function_neighbour_states_actions_sum = [];
          for possible_actions_item in possible_actions:
            value_function_neighbour_states = [];
            for state_space_item in state_space:
              value_function_neighbour_states.append(self.calculate_value_function_neighbours(state_space[individual_list_count], state_space_item, possible_actions_item)); 
            value_function_neighbour_states_actions_sum.append(sum(value_function_neighbour_states));
              
          self.value_function[individual_list_count] = max(value_function_neighbour_states_actions_sum);
          #print(value_function_neighbour_states);
          #print("value_function_neighbour_states if ",value_function_neighbour_states);

          if ((self.value_function[individual_list_count] - delta) != 0 and (self.value_function[individual_list_count] - delta) < 0.01):
            delta_too_small = True;

          if delta_too_small:
            break;
            #pass;
              
      else:
        
        #print((self.value_function));
        for individual_list_count in range(0, len(self.value_function)):
          neighbours_list = [];
          neighbours_actions = [];

          #print((self.value_function));

          delta = self.value_function[individual_list_count];
          

          #get the neighbours of the current state:
          neighbours_list, neighbours_actions = self.get_neighbours(individual_list_count, possible_actions);

          value_function_neighbour_states = [];
          value_function_neighbour_states_actions_sum = [];
          for possible_actions_item in possible_actions:
            value_function_neighbour_states = [];
            for state_space_item in state_space:
              value_function_neighbour_states.append(self.calculate_value_function_neighbours(state_space[individual_list_count], state_space_item, possible_actions_item));
            value_function_neighbour_states_actions_sum.append(sum(value_function_neighbour_states));
        
          
          self.value_function[individual_list_count] = max(value_function_neighbour_states_actions_sum);
          
          #print("value_function_neighbour_states else ",value_function_neighbour_states_actions_sum);
          #print("neighbours_list ", neighbours_list);
          #print("individual_list_count ", individual_list_count);
          #print("value function ", self.value_function);
          
          if ((self.value_function[individual_list_count] - delta) != 0 and (self.value_function[individual_list_count] - delta) < 0.01):
            delta_too_small = True;

          if delta_too_small:
            break;
            #pass;

        if delta_too_small:
          break;
          #pass;
  
  def calculate_value_function_neighbours(self, current_state, neighbour, action):
    transition_probability = self.mdp.P(current_state, action, neighbour);
    reward = self.mdp.R(neighbour);
    discount_factor = self.mdp.gamma();

    #print("transition_probability ", transition_probability, " reward  ", reward);

    #print(self.mdp.S().index(neighbour));
    #print("value function ", self.value_function);

    value_function_estimate = transition_probability * (reward + (discount_factor * self.value_function[self.mdp.S().index(neighbour)]));
    #print("value_function_estimate ",value_function_estimate);
    return value_function_estimate;

  def calculate_optimal_policy(self, state):

    #check if it's list of list or not:
    list_of_states = self.mdp.S();
    is_list_of_list = all(isinstance(individual_list, list) for individual_list in list_of_states);
    if is_list_of_list:
      pass;

    else:
      value_func = [];
      value_func_actions = [];
      
      if (((state + 1) < len(self.value_function)) and ((state + 1) >= 0)):
        value_func.append(self.value_function[(state + 1)]);
        value_func_actions.append("right");
      if (((state - 1) < len(self.value_function)) and ((state - 1) >= 0)):
        value_func.append(self.value_function[(state - 1)]);
        value_func_actions.append("left");

      value_func.append(self.value_function[state]);
      value_func_actions.append("do_nothing");
      
      policy = max(value_func);
      action = value_func_actions[value_func.index(policy)];
      if action == "do_nothing":
        if state == 0:
          action = "left";
        elif state == (len(self.value_function) - 1):
          action = "right";
      return action;
    
  def solve(self):

    self.calculate_value_function_iterative();
    actions_to_take = [];

    for value_function_item in self.value_function:
      actions_to_take.append(self.calculate_optimal_policy(self.value_function.index(value_function_item)));
      
    # returns a random policy
    
    ##print(self.mdp.S() , " " , self.mdp.A() ," ", self.mdp.gamma());
    ##print("transition probability ", self.mdp.P(0, "left", 1));
    
    ##for s in self.mdp.S():
    ##  random.choice(self.mdp.A());

    #print(self.value_function);
    #print(actions_to_take);
    ##return {s : random.choice(self.mdp.A()) for s in self.mdp.S()}
    return actions_to_take;

