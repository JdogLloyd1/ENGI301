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
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import servo as SERVO

class PokerRobot():
  
  display = None
  stepper = None
  dcMotor = None
  servo = None
  lightSensor = None
  
  def __init__(self, stepper='', dcMotor='', servo='', lightSensor='', i2c_bus=1, i2c_address=''):
    """initialize variables and setup display"""
    
    self.stepper = stepper
    self.dcMotor = dcMotor
    self.servo = SERVO.Servo(servo)
    self.lightSensor = lightSensor
    
    # Touchscreen with I2C
    self.display = ----.----(i2c_bus, i2c_address)
    
    self._setup()
   # end def init
  
  def _setup(self):
    """Setup hardware components"""
    
    # initialize analog input 
    ADC.setup()
    # Stepper motor
    
    # DC motor
    
    # Light sensor

  # end def setup()
    
  def deal(self, tableSide):
    """Deal one card face down"""
    # Use this function for both dealing to players and burning cards in game
    
    # set tableSide for whether DC motor to deal card will send to left or right side of the table
    tableSide = 
    # spin DC motor a set amount to shoot a card out 
    
    
  # end def deal()
    
  def deal_to_players(self, playerCount):
    """Deal two cards to each player"""
    # pull number of players
    # split up players evenly on both sides OR pull locations
    # calculate distances needed to travel 
    
    # run for loop twice to deal_down() to each player clockwise around table, moving in between locstions each time
    # return to starting location

  # end def deal_to_players()
  
  def flop(self):
  
  # burn 1 card
  deal(tableSide = '')
    
    # raise flip barrier
    self.servo.right()

    # deal 3 cards - CHECK SYNTAX
    for i=1:3:
        # slide one card over on rail
        deal(tableSide = '')


  # end def flop()
  
  def turn(self):
  
    # lower flip barrier
    self.servo.left() 

    # slide back to burn pile and burn 1 card
    deal(tableSide = '')

    # raise flip barrier
    self.servo.right()

    # slide over to 4th card position on rail

    # deal 1 card
    deal(tableSide = '')
  
  # end def turn()
  
  def river(self):
    
    # lower flip barrier
    self.servo.left() 

    # slide back to burn pile and burn 1 card
    deal(tableSide = '')

    # raise flip barrier
    self.servo.right()

    # slide over to 5th card position on rail

    # deal 1 card
    deal(tableSide = '')
  
  # end def river()

  def run(self):
    """Execute main program"""
    deckLoaded = False
    playerCount = 0
    
    while(True):
      # Display welcome screen
      # Screen 1: ask for number of players
      playerCount = ''
      # Stretch goal - place players around the table?
      # Prompt deck load
      # Check light sensor for deck loading
      # Lower flip barrier
      self.servo.left()
      # When loaded, proceed to deal in a circle along the rail, 1 card/player/cycle
      deal_to_players(playerCount=playerCount)
      
      # When betting complete, proceed to flop
      self.flop() 
      # When betting complete, proceed to turn
      self.turn()
      # When betting complete, proceed to river
      self.river()
      
      # Prompt for new hand or end game
      # If new game accepted, return to screen 1 with previous # of players pre-loaded
    
    # end def run()
    
  def cleanup(self):
    """Clean up hardware components"""
    
    # Set display to goodbye screen
    self.display.----
    
    # return to starting position on rail
    
    
    # Clean up GPIOs
    GPIO.cleanup()
    
    # Stop servo
    self.servo.cleanup()
    
  # end def cleanup()
    
# end class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
  
  poker_robot = PokerRobot()
  try:
        # Run the program
        poker_robot.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        poker_robot.cleanup()
        exit 
