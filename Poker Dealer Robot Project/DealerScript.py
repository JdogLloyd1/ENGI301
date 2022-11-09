# -*- coding: utf-8 -*-
"""
Robot Texas Hold 'em Poker Card Dealer
Jonathan Lloyd, November 2022
ENGI 301 with Dr. Erik Welsh
--------------------------------------------------------------------------
License:   
Copyright 2022 - Jonathan Lloyd

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Dealer Robot that will 
  - Ask for number of players in the hand
  - Sense that the deck is loaded into the robot
  - Deal two cards per player going down the table along rail
  - Burn a card then deal/flip 3 cards for the flop when prompted
  - Burn a card then deal/flip 1 card for turn and river each when prompted
  - Ask for new hand or exit program
  
"""

import time
import Adafruit_BBIO.GPIO as GPIO

class PokerRobot():
  
  display = None
  
  def __init__(self, i2c_bus=1, i2c_address=---):
    """initialize variables and setup display"""
    self.display = ----.----(i2c_bus, i2c_address)
    
    # Touchscreen with I2C
    
    self._setup()
   # end def init
  
  def _setup(self):
    """Setup hardware components"""
    
    # Stepper motor
    
    # DC motor
    
    # Servo motor
    
    # Light sensor

    # end def setup()
    
  def dealBurn(self):
    """Deal one card face down"""
    # Use this function for both dealing to players and burning cards in game
    
    # end def dealBurn()
  
  def deal_flip(self):
    """Deal one card face up"""
    # Activate flip barrier
    # call dealBurn()
    
    # end def deal_flip()
    
  def deal_to_players(self)
    
  def run(self):
    """Execute main program"""
    deckLoaded = False
    playerCount = 0
    
    while(True):
      # Display welcome screen
      # Screen 1: ask for number of players
      # Prompt deck load
      # Check light sensor for deck loading
      # When loaded, proceed to deal in a circle along the rail, 1 card/player/cycle
      # When betting complete, proceed to flop
      # When betting complete, proceed to turn
      # When betting complete, proceed to river
      # Prompt for new hand or end game
      # If new game accepted, return to screen 1 with previous # of players pre-loaded
    
    # end def run()
    
  def cleanup(self):
    """Clean up hardware components"""
    
    # Set display to goodbye screen
    self.display.----
    
    # end def cleanup()
    
  # end class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
  
  try:
        # Run the program
        pass  # Replace this line

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        pass  # Replace this line
