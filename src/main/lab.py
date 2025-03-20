# lab.py

class Lightbulb:
    """
    This class represents a Lightbulb object.
    """

    def __init__(self, state):
        """
        Constructor for the Lightbulb class.
        
        Parameters:
        - state: bool
            Represents the initial state of the lightbulb (True for on, False for off).
        
        Description:
        Initializes a new Lightbulb instance with the provided state. 
        The 'state' parameter determines whether the lightbulb is initially on or off.
        """
        self.state = state

    def get_state(self):
        """
        Getter method to retrieve the state of the lightbulb.
        
        Returns:
        - bool
            Current state of the lightbulb (True for on, False for off).
        
        Description:
        Returns the current state of the lightbulb.
        """
        return self.state

    def set_state(self, state):
        """
        Setter method to update the state of the lightbulb.
        
        Parameters:
        - state: bool
            New state of the lightbulb (True for on, False for off).
        
        Description:
        Sets the state of the lightbulb to the provided value.
        """
        self.state = state
    
    """

     * Now, let's create a new function named 'getDescription' that returns varying text depending on the value of 'state'. 
     * If 'state' is true,  then the bulb will be considered 'on'. If 'state' is false, then the bulb will be considered 
     * 'off'. The function should then return "The bulb is on" or "The bulb is off" depending on whether the bulb is on or 
     * off.
     * 
     * TODO: Create a function named 'get_description' that returns "The bulb is on" or "The bulb is off", depending on
     * whether 'state' is true or false.
     */    
    """

    # Write your code here

def create_bulb(state):
    """
    Function to create a new Lightbulb instance with the provided state.
    
    Parameters:
    - state: bool
        Represents the initial state of the lightbulb (True for on, False for off).
    
    Returns:
    - Lightbulb
        A new Lightbulb instance with the provided state.
    """
    return Lightbulb(state)
