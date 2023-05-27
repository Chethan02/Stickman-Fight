import pygame
from paths import *
from player_status_codes import *
from bitarray import bitarray

def justPass(val):
	print(val)
	return val
class Stickman_player:

	# Player attributes

	_facing = "R" # Direction in which the character faces
	_stop = 0 # Boolean for stopping action
	_movement_status = bitarray('00000000')|STANDING

	# Animation and other attributes

	_animate_frame = 0 # Keeps count of the animation frames
	_jump_frame_counter = 0 # Keeps count of the jump frames
	_frames = 6 # Number of times a frame is to be shown in a loop
	_player_horizontal_speed = 2 # Horizontal speed of the character
	_vertical_jump_speed = 4 # Vertical speed (Jump of the character)


	""" INITIALIZATION OF THE CHARACTER """

	def __init__(self,WINDOW_DIMENSIONS):
		
		# For reference of dimensions
		self.WINDOW_DIMENSIONS = WINDOW_DIMENSIONS

		# Position of the character
		self.x = WINDOW_DIMENSIONS[0]/2
		self.y = WINDOW_DIMENSIONS[1]*7/8
		self.default_y_location = self.y

		# Standing image facing Left Direction
		self.standing_imgL = [pygame.image.load(standing_imgL)]
		self.standing_imgL+=[(self.standing_imgL[0].get_width(),self.standing_imgL[0].get_height())]
		
		# Standing image facing Right Direction
		self.standing_imgR = [pygame.image.load(standing_imgR)]
		self.standing_imgR+=[(self.standing_imgR[0].get_width(),self.standing_imgR[0].get_height())]

		# Walking images facing Left Direction
		self.walking_imgsL = [[pygame.image.load(walking_img)] for walking_img in walking_imgsL]

		# Walking images facing Right Direction
		self.walking_imgsR = [[pygame.image.load(walking_img)] for walking_img in walking_imgsR]
		
		# Jumping images facing Left Direction
		self.jumping_imgsL = [[pygame.image.load(jumping_img)] for jumping_img in jumping_imgsL]

		# Jumping images facing Left Direction
		self.jumping_imgsR = [[pygame.image.load(jumping_img)] for jumping_img in jumping_imgsR]

		# Adding other attributes to the images' list
		for img in self.walking_imgsR:
			img.append((img[0].get_width(),img[0].get_height()))

		for img in self.walking_imgsL:
			img.append((img[0].get_width(),img[0].get_height()))

		for img in self.jumping_imgsR:
			img.append((img[0].get_width(),img[0].get_height()))
		
		for img in self.jumping_imgsL:
			img.append((img[0].get_width(),img[0].get_height()))

		# Width and Height of all image frames
		self.width,self.height = self.standing_imgL[1][0],self.standing_imgL[1][1]


	""" PRIVATE METHODS FOR FRAME MANAGEMENT AND CHARACTER MOVEMENT """

	# Get position of the character : X - Center, Y - Bottom
	def get_pos(self):
		return (self.x,self.y)

	# Private method left facing animation of the character
	def _to_left(self):

		val = self._animate_frame//self._frames
		if val == len(self.walking_imgsL):
			self._animate_frame = 0

		val = self._animate_frame//self._frames
		
		self._animate_frame+=1
		self.x -= self._player_horizontal_speed if self.x-self._player_horizontal_speed>10 else 0
		return self.walking_imgsL[val]

	# Private method right facing animation of the character
	def _to_right(self):

		val = self._animate_frame//self._frames
		if val == len(self.walking_imgsR):
			self._animate_frame = 0

		val = self._animate_frame//self._frames

		self._animate_frame+=1
		self.x += self._player_horizontal_speed if self.x+self._player_horizontal_speed<self.WINDOW_DIMENSIONS[0]-10 else 0

		if self.is_standing():
			return self.walking_imgsR[val]
		return self.crouching_imgsR[val]

	# Jump animations
	def _jump(self):

		# Get values for img array indexing
		val = self._jump_frame_counter//(self._frames+4)
		self._jump_frame_counter+=1

		# Checking if its the end of jump animation
		if val == len(self.jumping_imgsR):
			self._remove_jumping()
			self._jump_frame_counter = 0
			return self.jumping_imgsR[-1] if self._facing == "R" else self.jumping_imgsL[-1]

		# Movement in the vertical direction
		if self._jump_frame_counter > len(self.jumping_imgsR)*(self._frames+4)/2:
			self.y += self._vertical_jump_speed if self.y+self._vertical_jump_speed<self.default_y_location else 0
		else:
			self.y -= self._vertical_jump_speed

		# Case where the player is walking
		if self.is_walking():
			if self._facing == "R":
				self.x += self._player_horizontal_speed
				return self.jumping_imgsR[val]
			self.x -= self._player_horizontal_speed
			return self.jumping_imgsL[val]

		# Player isn't moving in the x - direction
		else:
			if self._facing == "R":
				return self.jumping_imgsR[val]
			return self.jumping_imgsL[val]


	""" STATUS MODIFICATION OPERATIONS """

	# Remove any status from the _movement_status
	def _removeStatus(self,status):
		self._movement_status &= ~status

	# Add any status from the _movement_status
	def _addStatus(self,status):
		self._movement_status |= status


	""" STATUS CHECKING """

	# Private method returns whether the character is moving or not
	def is_moving(self):
		return (self._movement_status & MOVING) == MOVING

	# Private method returns whether the character is walking or not
	def is_walking(self):
		return (self._movement_status & WALKING) == WALKING

	# Private method returns whether the character is jumping or not
	def is_jumping(self):
		return (self._movement_status & JUMPING) == JUMPING

	# Private method returns whether the character is standing or not
	def is_standing(self):
		return (self._movement_status & STANDING) == STANDING

	# Private method returns whether the character is crouching or not
	def is_crouching(self):
		return (self._movement_status & CROUCHING) == CROUCHING


	""" STATUS SETTING """

	# Private method adds moving to status
	def _make_moving(self):
		self._addStatus(MOVING)

	# Private method adds walking to status
	def _make_walking(self):
		self._addStatus(WALKING)

	# Private method adds jumping to status
	def _make_jumping(self):
		self._addStatus(JUMPING)

	# Private method sets status to standing
	def _make_standing(self):
		self._addStatus(STANDING)
		self._removeStatus(CROUCHING)

	# Private method sets status to crouching
	def _make_crouching(self):
		self._addStatus(CROUCHING)
		self._removeStatus(STANDING)


	""" STATUS REMOVAL """

	# Private method removes moving status
	def _remove_moving(self):
		self._removeStatus(MOVING)

	# Private method adds to status to walking
	def _remove_walking(self):
		self._removeStatus(WALKING)

	# Private method adds to status to standing
	def _remove_jumping(self):
		self._removeStatus(JUMPING)


	""" FRAME MANAGEMENT """

	# Return the default frame for the character
	def _default_frame(self):
		# Check for stop moving condiiton
		if self._stop:
			self._animate_frame = 0 # Set animation frames back to zero
			self._stop = 0	# Since stopping action will be complete, _stop is made false again

		# Player is standing
		if self._facing == "R":
			return self.standing_imgR + [self.get_pos()]
		return self.standing_imgL + [self.get_pos()]

	# Frame movement of the character
	def frame_movement(self):
		# Checking if the character is moving
		if self.is_moving():
			# Checking for movement status type
			if self.is_walking():
				if self.is_jumping():
					return self._jump() + [self.get_pos()]
				if self._facing == "R":
					return self._to_right() + [self.get_pos()]
				return self._to_left() + [self.get_pos()]

		# Jumping when there is no movement
		if self.is_jumping():
			return self._jump() + [self.get_pos()]
			
		# If the character isn't moving
		return self._default_frame()

	
	""" CHARACTER MOVEMENT """

	# Set the _stop to 1 in order to stop the frame changing of the character
	def stop_moving(self):
		self._stop = 1
		self._remove_moving()
		self._remove_walking()

	# Set direction as right
	def move_right(self):
		self._facing = "R"
		self._make_moving()
		self._make_walking()

	# Set direction as left
	def move_left(self):
		self._facing = "L"
		self._make_moving()
		self._make_walking()
	
	# Jump up
	def jump_up(self):
		self._make_moving()
		self._make_jumping()

	# Crouch down
	def crouch_down(self):
		self._make_moving()
		self._make_crouching()
