class BaseStrategy ():
    def __init__(self, envelope_arr):
        self.envelopes = envelope_arr #array of envelopes on which the strategy is performed
        self.count = 0 #integer stating the number of envelopes opened and used to access the next envelope tha array
        self.chosen_envelope = None #Variable from type Envelope that contains the envelope that has been chosen as part of the strategy
        self.continue_strategy = True #boolian variable which informs if the strategy should be continued
    """Defines the values of BaseStrategy's properties.
        :param envelope_arr: self.envelopes value
        :type envelope_arr: Envelope[]
        """

    def play(self):
        while ((self.continue_strategy)and(self.count<100)):
            self.perform_strategy(self.envelopes[self.count])
        if (self.chosen_envelope == None):
            self.chosen_envelope = self.envelopes[self.count]
        return self.chosen_envelope
    """Activates perform_strategy() for each envelope in the array until one is chosen.
        :return: The chosen envelope (self.chosen_envelope)
        :rtype: Envelope
        """

    def perform_strategy(self, envelope):
        print ('the sum in this envelope is {envelope.money}')
        envelope.used = True
        choice = input(f'if you would like to keep it press u (use) if not press c (continue)')
        if (choice == 'c'):
            self.count = self.count + 1
        else:
            self.continue_strategy = False
            self.chosen_envelope = envelope
    """Presents the user with the amount of money in the envelope and lets him choose if he wants to keep it or continue.
        :param envelope: envelope value
        :type envelope: Envelope
        """

    def display(self):
        print("Base strategy - you open the envelopes one after the other and stop whenever you feel like it")
    """Prints out an explaination about the method"""


