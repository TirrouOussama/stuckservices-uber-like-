
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.graphics import Rectangle, Color, Line, Bezier, Ellipse, Triangle
from functools import partial
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
import kivymd
from kivy_garden.mapview import MapView, MapMarkerPopup, MapMarker, MapSource

import pickle
from kivy.utils import platform
from plyer import gps 
import numpy as np
import time 
import math
from math import pi
import sqlite3
import threading
import socket
import sys
import io
import PIL.Image as Image
from numpy import asarray
from array import array
import os
import zipfile 
import os.path
import requests
import re


body = ''
headers = ''
#### after login if acc is not created on the loggin device u need to import ur avatar + an additional info
####                        for this we need another socket called get my info   SAD ASF
url = ''
who = 'user'
av_pickle = 'empty.png'
error_request = ''
forgot_packet = ''
holdermsg = ''
auth_packet = ''
auth_packet_answer = ''
username = ''
conto_auth_socket_fromsaved = False
conto_auth_socket_fromlogin = False
from_login = False
decoded_auth_packet_answer = ''

lat_request = ''
lon_request = ''
radius_request = ''
conto_request_drivers_one_time = False
conto_request_drivers = False
request_drivers_packet = ''
req_full_recv = False

sub_packet = ''
sub_packet_anwer = ''
sub_packet_answer_decoded = ''
conto_sub = False
conto_sub_one_time = False
subed = False

update_packet = ''
conto_update_socket = False
conto_update_socket_one_time = False


serverip = '192.168.1.104'

myip = ''

chat_send_ip = ''
conto_chat_send_socket = False
conto_chat_send_socket_one_time = False
chat_send_packet = ''
reciever_state = 'Unactive'
chat_recv_string = ''

new_notif = []
new_notif_bool = False



###############################
									############>>>>>>>>   sockets needs a time sleep specific inside another
###############################									while loop to not consume device resources

############################################################################################################################################################
##      ######     ##                #####              #######            ######                    #                  ##############################################################################################################
##      ######     ##                 ####               ######             #####                    #                  ###############################################################################################################
##      ######     ##      #######      ##                #####      ###     ####                    #                  ##########################################################################################
##      ######     ##      ########      #      #####      ####      ####     ##########      ########     ###########################################################################
##      ######     ##      #########     #      ######      ###      #####     #########      ########     ###########################################################################
##      ######     ##      ########      #      #######     ###      ######     ########      ########     ###########################################################################
##      ######     ##      ######       ##      ########     ##      #######     #######      ########     ############################################################################
##      ######     ##                 ####      ########     ##                   ######      ########                ####################################################################################
##      ######     ##               ######      ########     ##                    #####      ########                ##################################################################################
##      ######     ##      ###############      ########     ##      ##########     ####      ########                #####################################################################
##      ######     ##      ###############      ########     ##      ###########     ###      ########     #####################################################################
##      ######     ##      ###############      #######      ##      ############     ##      ########     #####################################################################
##      ######     ##      ###############      ######      ###      #############     #      ########     #####################################################################
##                 ##      ###############                 ####      ##############           ########                  #################################################################################
##                 ##      ###############                #####      ###############          ########                  #############################################################################################
##                 ##      ###############              #######      ################         ########                  ###########################################################################################
###########################################################################################################################################################

def update_socket():
	global conto_update_socket, conto_update_socket_one_time, who, conto_update_socket, update_packet
	while conto_update_socket == False:
		time.sleep(0.5)
		while conto_update_socket_one_time == True:
			try:
				update_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				update_socket.connect((serverip, 4050))

				while True:
					if update_packet != '':
						print('sending :' + update_packet)
						update_socket.send(bytes(update_packet, 'utf-8'))		
						update_packet_answer = update_socket.recv(400)
						update_packet_answer_decoded = update_packet_answer.decode("utf-8")
						print(update_packet_answer_decoded)
						conto_update_socket_one_time = False
						update_socket.shutdown(socket.SHUT_RDWR)
						update_socket.close()	
						break

			except:
				time.sleep(0.5)
				print('trying to update')



#####################################################################################################################################
########                 ####      ########      ###                   ########                        #                ################################################################################
######                  #####      ########      ###                     #####                        ##                ############################################################################
####                   ######      ########      ###      ##########      ###                        ###                ##############################################
###     #####################      ########      ###      ############     #     #######################       ###########################
##     ######################      ########      ###      ###########     #     ########################       ############################################################################
##                       ####      ########      ###                    ###                          ###       ############################################################################
###                       ###      ########      ###                    ####                          ##       ##############################################################################
####################      ###      ########      ###      ##########     #######################       #       ########################################
####################      ###      ########      ###      ############     #####################       #       ###########################################
###################      ####      ########      ###      #############     ###################       ##       ############################
##################      #####      ########      ###      ##############     #################       ###       #############################
####                   ######      ########      ###      #############      #                      ####                 #############################
###                   #######                    ###                        ##                     #####                 ##################################################################
##                   ########                    ###                       ##                     ######                 ############################################################################################
#####################################################################################################################################


def sub_socket():
	global sub_packet, sub_packet_answer, conto_sub, conto_sub_one_time, av_pickle, error_request, username, subed

	while conto_sub == False:
	
			time.sleep(0.5)
			while conto_sub_one_time == True:
				try:
					sub_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sub_socket.connect((serverip, 2012))
					while True:
						if sub_packet != '':
							print('sending : ' + sub_packet)	
							sub_socket.send(bytes(sub_packet, 'utf-8'))
							print('receving')
							sub_packet_answer = sub_socket.recv(100)
							sub_packet_answer_decoded = sub_packet_answer.decode("utf-8")
							print(sub_packet_answer_decoded)
							if sub_packet_answer_decoded.split('|')[0] == 'FREESLOT':
								subed = True
								username = sub_packet_answer_decoded.split('|')[2]
								print(sub_packet_answer_decoded)
								file = open(av_pickle, 'rb')
								image_data = file.read(1024)
								while image_data:
									sub_socket.send(image_data)
									image_data = file.read(1024)	
								conto_sub_one_time = False
								sub_socket.shutdown(socket.SHUT_RDWR)
								sub_socket.close()	
								break	

							if sub_packet_answer_decoded.split('|')[0] == 'NOSLOT':
								print(sub_packet_answer_decoded)
								error_request = sub_packet_answer_decoded.split('|')[1]
								conto_sub_one_time = False
								sub_socket.shutdown(socket.SHUT_RDWR)
								sub_socket.close()	
								break

				except:
					time.sleep(0.5)
					print('sending subscrib')

########################################################################################################################################################################################
##                   #####                ##                  ###      ######      ##             #####                   ###########################################################################################################################
##                    ####                ##                  ###      ######      ##             ####                   ############################################################################################################################################
##     ##########      ###     #############     ########     ###      ######      ##     ###########                   ##########################################################################################
##     ###########      ##     #############     ########     ###      ######      ##     ##########      ##############################################################################################
##     ###########      ##     #############     ########     ###      ######      ##     #########       ###############################################################################################
##     ##########      ###     #############     ########     ###      ######      ##     #########                    ##############################################################################################
##     #########      ####                ##     ########     ###      ######      ##             ##                    #####################################################################################################################
##     ###           #####                ##     ########     ###      ######      ##             ###                    #######################################################################################################################
##                 #######     #############     ########     ###      ######      ##     #########################      ##################################################################################
##                    ####     #############     ########     ###      ######      ##     ########################       ######################################################################################
##     ##########      ###     #############     #####        ###      ######      ##     #######################       ########################################################################################
##     ############     ##                ##     #####        ###      ######      ##     ######################       ######################################################################################################
##     #############     #                ##                  ###                  ##             ###                 #############################################################################################################################################
##     ##############                     ##                   ##                  ##             ##                 #######################################################################################################################################################
#########################################################       #################################################################################################################
##########################################################       #######################################################################################
########################################################################################################################################################

def func_request_drivers_socket():
	global req_full_recv, request_drivers_packet, request_drivers_packet_answer, request_drivers_packet_answer_deocded, conto_request_drivers, conto_request_drivers_one_time
	while conto_request_drivers == False:
			time.sleep(0.5)
			while conto_request_drivers_one_time == True:
				try:
					request_drivers_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					request_drivers_socket.connect((serverip, 3012))
					while True:
						if request_drivers_packet != '':
								print('sending : ' + request_drivers_packet)	
								request_drivers_socket.send(bytes(request_drivers_packet, 'utf-8'))
								request_drivers_packet_answer = request_drivers_socket.recv(1024)
								request_drivers_packet_answer_deocded = pickle.loads(request_drivers_packet_answer)
								print(request_drivers_packet_answer_deocded)

								filename = 'requested.zip'
								print(filename)
								file = open(filename, 'wb')
								data = request_drivers_socket.recv(1024)
								print('before while data is :' )
								print(data)
								while data:
									print('recieving :'+ filename)
									file.write(data)
									data = request_drivers_socket.recv(1024)
									print(data)
								file.close()

								with zipfile.ZipFile('requested.zip', 'r') as zip_ref:
									zip_ref.extractall(os.getcwd())
								req_full_recv = True




								conto_request_drivers_one_time = False
								request_drivers_packet = ''
								request_drivers_socket.shutdown(socket.SHUT_RDWR)
								request_drivers_socket.close()
								break
				except:
					time.sleep(0.5)
					print('waiting requests')
########################################################################################################################################################################################
##              ##########     #######     #                   #      #######     ##                #     ########    ##########################################################################################################################
##     ####      #########     #######     #                   #      #######     ##                #      #######    ###########################################################################################################################
##     #####      ########     #######     ########     ########      #######     ##     ############       ######    #########################################################################################################
##     ######      #######     #######     ########     ########      #######     ##     ############        #####    #################################################################################################
##     #######      ######     #######     ########     ########      #######     ##     ############         ####    ##################################################################################################
##     ########      #####     #######     ########     ########      #######     ##     ############          ###    ###################################################################################################
##     #########      ####     #######     ########     ########                  ##     ############     #     ##    ###################################################################################################
##                     ###     #######     ########     ########                  ##               ##     ##     #    ####################################################################################################################
##                      ##     #######     ########     ########                  ##               ##     ###         ###################################################################################################################
##     ############      #     #######     ########     ########      #######     ##     ############     ####        ##################################################################################################
##     #############     #     #######     ########     ########      #######     ##     ############     #####       ################################################################################################
##     ##############                      ########     ########      #######     ##                #     ######      #######################################################################################################################
##     ###############                     ########     ########      #######     ##                #     #######     ######################################################################################################################
##     ################                    ########     ########      #######     ##                #     ########    #####################################################################################################################
########################################################################################################################################################################################




def func_auth_socket():

	global auth_packet, auth_packet_answer, username, conto_auth_socket_fromsaved, decoded_auth_packet_answer, holdermsg, myip
	while conto_auth_socket_fromlogin == False:
			time.sleep(1)
			while conto_auth_socket_fromsaved == False:
				try:
					auth_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					auth_socket.connect((serverip, 4012))
					myip = auth_socket.getsockname()[0]
					print(myip)



					print('connected')
					print('after conn '+ auth_packet)
					while True:
						if auth_packet != '':
							print('sending auth packet: ' + auth_packet)	
							auth_socket.send(bytes(auth_packet, 'utf-8'))
							auth_packet_answer = auth_socket.recv(100)  
							decoded_auth_packet_answer = auth_packet_answer.decode("utf-8")
							print(decoded_auth_packet_answer)
							conto_auth_socket_fromsaved = True
							print(conto_auth_socket_fromsaved)
							auth_socket.shutdown(socket.SHUT_RDWR)
							auth_socket.close()
							break
							if decoded_auth_packet_answer == 'match':
								username = auth_packet.split('|')[0]
								print('recieved username: ' + username )
								conto_auth_socket_fromlogin == True
								auth_socket.shutdown(socket.SHUT_RDWR)
								auth_socket.close()
							elif decoded_auth_packet_answer == 'unmatch':
								#auth_packet = ''
								auth_socket.shutdown(socket.SHUT_RDWR)
								auth_socket.close()									
							else:
								pass
				except:
					#auth_socket.shutdown(socket.SHUT_RDWR)
					holdermsg = 'Initializing'
					time.sleep(0.5)
					holdermsg = 'Initializing  .'
					time.sleep(0.5)
					holdermsg = 'Initializing  ..'
					time.sleep(0.5)
					holdermsg = 'Intializing  ...'
#############################################################################################################################################################
############################################################################################################################################################
#              ######           ###              ###            #     #######     #    ###                  ################################################################################################################################
#               ###              ##               ##            #     #######     #     ##                  ####################################################################################################################################
#    ########    #      #####     #    ########    #    #########     #######     #      ########    ###################################################################################################
#    ########    ##     #####     #    ########    #    #########     #######     #       #######    ##################################################################################################
#    #######     ###     ####     #    #######     #    #########     #######     #        ######    ####################################################################################################
#               ############     ##               ##    #########     #######     #    #    #####    #####################################################################################################################
#             ############      ###              ###    #########                 #    ##    ####    ##########################################################################################################################
#    ####################      ####    #############    #########                 #    ###    ###    #######################################################################################################
#    ###################      #####    #############    #########     #######     #            ##    ###################################################################################################
#    ##################      ######    #############    #########     #######     #             #    ####################################################################################################
#    #################      #######    #############    #########     #######     #    ######        ###############################################################################################
#    ################      ########    #############    #########     #######     #    #######       ##############################################################################################
#    ###############                   #############            #     #######     #    ########      ##############################################################################################################
#    ###############                   #############            #     #######     #    #########     #############################################################################################################
#############################################################################################################################################################

def func_chat_send_socket():
	global conto_chat_send_socket, conto_chat_send_socket_one_time, chat_send_packet, username, uncative_user, chat_send_ip, reciever_state
	while conto_chat_send_socket == False:
		time.sleep(0.5)   # BE very careful  the time sleep  short buts buggy long gets ignored
		print('sleeping for 0.5 on the outer socket send')


		while conto_chat_send_socket_one_time == True:
			print('inside one time')


			try:
				
				print('trinying to before cond ip = void')

				if chat_send_ip != '':
					print('after cond ip != void')
					chat_send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					chat_send_socket.connect((chat_send_ip, 4600))
					print('connected to chat send ip before while True')
					while True:
						print('after chat while True')
						if chat_send_packet != '':
							print('after cond packet != void')
							print('sending msg: ' + chat_send_packet)	
							chat_send_socket.send(bytes(chat_send_packet, 'utf-8'))
							chat_send_packet = ''
							####chat_send_ip = ' '                       ######## past it there also

							conto_chat_send_socket_one_time = False   ### past it to the closing coversation button
							chat_send_socket.shutdown(socket.SHUT_RDWR)
							chat_send_socket.close()

							print('reset')

							print('closed socket')
							break
			except:

				time.sleep(0.5)
				print('no target to')          
                        
def func_chat_recv_socket():
	global chat_recv_string, myip, chat_recv_socket, new_notif, new_notif_bool
	while True:
		if myip != '':
			print('My ip is : ' + myip)
			break
	while True:
		try:
			chat_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			chat_recv_socket.bind((myip, 4600))
			print('Binded to ' + myip)
			chat_recv_socket.listen(10)
			
			while True:
				clientsocket, address = chat_recv_socket.accept()
				print(address[0])
				print('accepted')
				while True:
					chat_recv = clientsocket.recv(100)
					print('recieving msg')
					chat_recv_string = chat_recv.decode("utf-8")
															
					new_notif_bool = True
					print(chat_recv_string)
					new_notif.append(chat_recv_string)
					#users_ip.append(chat_recv_string.spit('|')[0] + '|' + address[0])
					#print(users_ip)
					reciever_state = 'Active'
					break
					print('broke ')
					clientsocket.close()
		except:
			
			pass

#################################################################################################################
#################################################################################################################
################################################################################################################
thred_func_chat_send_socket = threading.Thread(target = func_chat_send_socket)
thred_func_chat_recv_socket = threading.Thread(target = func_chat_recv_socket)
thread_func_update_socket = threading.Thread(target = update_socket)
thread_func_sub_socket = threading.Thread(target = sub_socket)
thread_func_request_drivers_socket = threading.Thread(target = func_request_drivers_socket)
thread_func_auth_socket = threading.Thread(target = func_auth_socket)

########################################################################################################################################################################
#     ######     #               ##     ###########              #####               ###              ###############################################################################################################
#     ######     #               ##     ###########               ####               ###               ################################################################################################################
#     ######     #    #####      ##     ###########     #####      ###     #############     ######     #################################################################
#     ######     #    #####      ##     ###########     ######      ##     #############     #######     ##########################################################################       ###########       #######       ##########      #######        ##################       ############        ##################################################################################################
#                #    #####      ##     ###########     ########     #     #############     #######    ##################################################################################
#                #    #####      ##     ###########     ########     #              ####     #####     #############################################################################################
#     ######     #    #####      ##     ###########     ########     #              ####              #########################################################################################
#     ######     #    #####      ##     ###########     ########     #     #############            ###############################################################################
#     ######     #    #####      ##               #     #######     ##     #############    ##       ############################################################################
#     ######     #               ##               #                ###               ###    ####       ###############################################################################################################
#     ######     #               ##               #               ####               ###    #######     #############################################################################################################
#####################################################################################################################################################################



class holderscreen(Widget):
	#global auth_packet, auth_packet_answer, decoded_auth_packet_answer, holdermsg, from_login
	def __init__(self, **kwargs):
		global auth_packet, auth_packet_answer,decoded_auth_packet_answer, holdermsg, from_login, serverip
		super().__init__(**kwargs)
		if platform == 'android':
			from android.permissions import Permission, request_permissions	
			def callback(permission, results):
				if all ([res for res in results]):
					print('got all permissions')	
				else:
					print('not all permisions')
			request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION, Permission.READ_EXTERNAL_STORAGE])
		
		self.update_kvholder_refresh = 0.5 
		self.holderanimation_refresh = 1/40
		self.holderanimation_alive_refresh = 1/40
		self.update_saved_auth_creds_refresh = 1/50
		self.auth_transition_cond = False
		self.saved_auth_string = ''
		self.circle_list = []
		self.circlesize1 = 0
		self.circlesize2 = 0
		self.circlesize3 = 0
		self.circle1 = Line(circle=(0,0,0),width=0)
		self.circle2 = Line(circle=(0,0,0),width=0)
		Clock.schedule_interval(self.update_kvholder, self.update_kvholder_refresh)
		Clock.schedule_interval(self.holderanimation, self.holderanimation_refresh)
		Clock.schedule_interval(self.holderanimation_alive, self.holderanimation_alive_refresh)
		Clock.schedule_interval(self.update_saved_auth_creds, self.update_saved_auth_creds_refresh)
		self.x = self.width
		self.y = self.height
		with self.canvas:

			Color(1,1,1,1)
			self.circle1 = Line(circle=(self.x*0.5, self.y*0.5, 0),width=1)
			self.circle_list.append(self.circle1)
			self.circle2 = Line(circle=(self.x*0.5, self.y*0.5, 0),width=2)
			self.circle_list.append(self.circle2)
			self.circle3 = Line(circle=(self.x*0.5, self.y*0.5, 0),width=1)
			self.circle_list.append(self.circle3)

		#########################################################################################################
		##########################  CHECK SAVED AUTHENTICATIONS IN auth.db from table saved_auth ################
									############################################################
											########################################
													#####################
														###########

		self.linktoauth = sqlite3.connect('auth.db')
		self.curs = self.linktoauth.cursor()
		self.curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='saved_auth' ''')
		if self.curs.fetchone()[0]==1: 
			print('Table exists.')
			self.curs.execute('SELECT * FROM saved_auth')
			self.curs.execute("SELECT * FROM saved_auth")
			self.saved_auth_string = self.curs.fetchone()
			auth_packet = self.saved_auth_string[0] + "|" + self.saved_auth_string[1] + "|" + 'user'
			print('local saved creds: ' + auth_packet)
			#auth_packet = curs.fetchone()

						#####################  for one saved auth ######################
		else: 
			theapp.screenm.current = "loginscreen"
			Clock.unschedule(self.update_kvholder)
			Clock.unschedule(self.holderanimation)
			Clock.unschedule(self.holderanimation_alive)
			Clock.unschedule(self.update_saved_auth_creds)

	def update_kvholder(self, *args):
		global holdermsg
		self.ids.kvholder.text = holdermsg


	def holderanimation(self, *args):
		self.x = self.width
		self.y = self.height
		if self.x !=0:
			self.circlesize1 = self.circlesize1 + self.x*0.005
			self.circlesize2 = self.circlesize2 + self.x*0.005 + self.circlesize1
			self.circlesize3 = self.circlesize3 + self.x*0.005 + self.circlesize2
			if self.circlesize1 >= self.x*0.1:
				self.circlesize1 = self.x*0.05
			if self.circlesize2 >= self.x*0.2:
				self.circlesize2 = self.x*0.05
			if self.circlesize3 >= self.x*0.3:
				self.circlesize3 = self.x*0.05




	def holderanimation_alive(self, *args):
			global serverip
			self.circle_list[0].circle = [self.x*0.5, self.y*0.7, self.circlesize1]
			self.circle_list[1].circle = [self.x*0.5, self.y*0.7, self.circlesize2]
			self.circle_list[2].circle = [self.x*0.5, self.y*0.7, self.circlesize3]





	def update_saved_auth_creds(self, *args):
		global auth_packet, auth_packet_answer, username,decoded_auth_packet_answer, from_login
		if decoded_auth_packet_answer == 'match' and self.auth_transition_cond == False:
			print('to first screen  ' + decoded_auth_packet_answer)
			theapp.screenm.current = "first screen"
		
			Clock.unschedule(self.update_kvholder)
			Clock.unschedule(self.holderanimation)
			Clock.unschedule(self.holderanimation_alive)
			Clock.unschedule(self.update_saved_auth_creds)



			self.auth_transition_cond = True	
		elif decoded_auth_packet_answer == 'unmatch' and self.auth_transition_cond == False:
			print('to login screen ' + decoded_auth_packet_answer)
			if self.width > 100:            ######## WTF IS THIS
				

				Clock.unschedule(self.update_kvholder)
				Clock.unschedule(self.holderanimation)
				Clock.unschedule(self.holderanimation_alive)

				self.auth_transition_cond = True
				from_login = True
				theapp.screenm.current = "loginscreen"
				Clock.unschedule(self.update_saved_auth_creds)



		else:
			pass

	def on_size(self, *args):
		self.x = self.width
		self.y = self.height
		

	def connect_to_server(self):
		global serverip
		serverip = self.ids.server_field.text

#############################################3#############################################3#############################################3#############################################3
##       #############3#####                    ####                 ##########       ########       ######     ############3#############################################3#############################################3
##       ###############3###                    ####                 ##########       ########        #####     ##############3#############################################3#############################################3
##       ###############3###      ########      ####     ######################       #######3         ####     #########################################3#############################################3
##       ###############3###      ########      ####     ####################################3          ###     ##########################################3#############################################3
##       ###############3###      ########      ####     ####################################3           ##     ###########################################3#############################################3
 #       ###############3###      ########      ####     ######################       #######3            #     ############################################3#############################################3
##       ###############3###      ########      ####     ####             #####       ########      #           #######3#############################################3#############################################3
##       ###############3###      ########      ####     ####             #####       ########      ##          ######3#############################################3#############################################3
##       ###############3###      ########      ####     ########     #########       ########      ###         #3############################################3#############################################3
##       ###############3###      ########      ####     ########     #########       ########      ####        3#############################################3#############################################3
##                      ####                    ####                  #########       #3######      #####       ##################################3#############################################3#############################################3
##                      ####                    ####                  #########       #3######      ######      #################################3#############################################3#############################################3
#############################################3#############################################3#############################################3#############################################3

class Loginscreen(Widget):						
	#global auth_packet, conto_auth_socket_fromsaved, from_login, x_real
	def __init__(self, **kwargs):
		global auth_packet, conto_auth_socket_fromsaved, from_login, who, username
		super().__init__(**kwargs)
		who = 'user'

		self.ids.bt_driver.background_color = [0, 0, 0, 0]
		self.ids.as_driver_label.color = [1 , 1, 1, 1]
		self.ids.bt_user.background_color = [0, 0, 0, 0.2]
		self.ids.as_user_label.color = [1 , 0, 0, 1]

		self.if_login_transition_refresh = 0.1
		self.ids.check_uncheck.source = 'uncheck.png'
		self.ids.remember_login_text.text = 'Remember Me'
		self.mylat = 0
		self.mylon = 0
		self.pwd = ''
		self.usr = ''


		Clock.schedule_interval(self.if_login_transition, self.if_login_transition_refresh)







	def loginbt(self):
		global auth_packet, conto_auth_socket_fromsaved 
		self.pwd = self.ids.loginpassword.text
		self.usr = self.ids.loginusername.text
		print(self.usr + '|' + self.pwd)
		auth_packet = self.usr+ '|' + self.pwd + '|' + who
		conto_auth_socket_fromsaved = False


	def signinbt(self):
		theapp.screenm.current = "signinscreen"	
		Clock.unschedule(self.if_login_transition)                   ######### delete to origin
	def remember_login(self):
		if self.ids.check_uncheck.source == 'uncheck.png':
			self.ids.check_uncheck.source = 'check.png'
			self.ids.remember_login_text.text = '        Dont Remember Me'
		elif self.ids.check_uncheck.source == 'check.png':
			self.ids.check_uncheck.source = 'uncheck.png'
			self.ids.remember_login_text.text = 'Remember Me'

	def if_login_transition(self, *args):
		global decoded_auth_packet_answer, from_login, username
		if decoded_auth_packet_answer == 'match' and from_login == True:
			username = self.usr
			theapp.screenm.current = "first screen"
			Clock.unschedule(self.if_login_transition)               ############ delet to origin
		else:
			pass

	def forgot(self):
		theapp.screenm.current = "forgot_screen"
		Clock.unschedule(self.if_login_transition)                 ############### delet to orgin

	def as_driver(self):
		global who
		self.ids.bt_driver.background_color = [0, 0, 0, 0.2]
		self.ids.as_driver_label.color = [1 , 0, 0, 1]
		self.ids.bt_user.background_color = [0, 0, 0, 0]
		self.ids.as_user_label.color = [0 , 0, 0, 1]
		who = 'driver'


	def as_user(self):
		global who
		self.ids.bt_driver.background_color = [0, 0, 0, 0]
		self.ids.as_driver_label.color = [0 , 0, 0, 1]
		self.ids.bt_user.background_color = [0, 0, 0, 0.2]
		self.ids.as_user_label.color = [1 , 0, 0, 1]
		who = 'user'



####################################################################################################3####################################################################################################3
#              #                ##               #####               ###               ##                  ##########################################################3####################################################################################################3
#              #                ##                 ###               ###               ##                  ##############################################################3####################################################################################################3
#    ###########    ########    ##    #########     ##     #############     ######    ########     #########3####################################################################################################3
#    ###########    ########    ##    ##########     #     #############     ######    ########     #3####################################################################################################3
#    ###########    ########    ##    ##########     #     #############     ######    #######3     ####################################################################################################3
#             ##    ########    ##    #########     ##     ###        ##     ######    ########     ################3####################################################################################################3
#             ##    ########    ##    ##           ###     ###        ##     ######    ########     ##########3####################################################################################################3
#    ###########    ########    ##    ##          ####     #####    ####     ######    ########     ###########3####################################################################################################3
#    ###########    ########    ##    ########     ###     #####    ####     ######    ########     ##############3####################################################################################################3
#    ###########                ##    #########     ##              ####               ########     ################################3####################################################################################################3
#    ###########                ##    ##########     #              ####               ########     ###############################3####################################################################################################3
#################################################################################################3####################################################################################################3
class forgot_screen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ids.forgot_forward_msg.text = ''
	def forward_forgot(self):
		global forgot_packet
		if self.ids.string_forgot.text != '' and len(self.ids.string_forgot.text) >= 6 and self.ids.string_forgot.text[0] != '@' and self.ids.string_forgot.text[-1] != '@':
			for char in self.ids.string_forgot.text:
				if char == '@':
					forgot_packet = 'email|' + self.ids.string_forgot.text
					self.ids.forgot_forward_msg.text = ''
					break
				if char != '@':
					forgot_packet = 'user|' + self.ids.string_forgot.text	
					self.ids.forgot_forward_msg.text = ''
		else:
			self.ids.forgot_forward_msg.text = 'Please Enter A valid username or Email'
				
					

	def backtologin_forgot(self):
		theapp.screenm.current = "loginscreen"
		self.ids.forgot_forward_msg.text = ''
		self.ids.string_forgot.text = ''

##################################################################################################################################################################################
#####               ##      #              ####      ########     ################       ##     ########     #######################################################################################################################################
###                ###      #              ####       #######     ################       ##      #######     ########################################################################################################################################
##                ####      #     #############        ######     ################       ##       ######     ################################################################################################################################
#       #####################     #############         #####     #########################        #####     #########################################################################################################
#      ######################     #############          ####     #########################         ####     #############################################################################################################
#                #####      #     #############           ###     ################       ##          ###     #######################################################################################################################################
#                 ####      #     #############     #      ##     ################       ##     #     ##     ########################################################################################################################################
##                 ###      #     ###         #     ##      #     ################       ##     ##     #     #################################################################################################################################################
#############       ##      #     ###         #     ###           ################       ##     ###          ######################################################################################################################################
#############       ##      #     #####     ###     ####          ################       ##     ####         ###############################################################################################################################
############       ###      #     #####     ###     #####         ################       ##     #####        #############################################################################################################################
###               ####      #     #####     ###     ######        ################       ##     ######       #########################################################################################################################
##               #####      #               ###     #######       ################       ##     #######      ########################################################################################################################################
#               ######      #               ###     ########      ################       ##     ########     #####################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################


class signinscreen(Widget):
	av_source = StringProperty()
	def __init__(self, **kwargs):
		global sub_packet, conto_sub, conto_sub_one_time, who, av_pickle, error_request, subed, username
		super().__init__(**kwargs)
		self.driver_name_field = False
		self.driver_password_field = False
		self.email_field = False
		self.ids.error_string.text = ''

		self.ids.bt_driver.background_color = [0, 0, 0, 0]
		self.ids.as_driver_label.color = [1 , 1, 1, 1]


		self.ids.bt_user.background_color = [0, 0, 0, 0.2]
		self.ids.as_user_label.color = [1 , 0, 0, 1]

	def create_account(self):
		global sub_packet, conto_sub, conto_sub_one_time, who, error_request
		self.driver_name_field = False
		self.driver_password_field = False
		self.email_field = False
		self.ids.error_string.text = ''


		if len(self.ids.username_sign.text) >= 5:
			for char in self.ids.username_sign.text:

				if char != '!' or char != '@' or char != '#' or char != '$' or char != '%' or char != '^' or char != '&' or char != '(' or char != ')'or  char != '_'or  char != '+'or  char != '-'or  char != '}'or  char != '{' or char != '[' or char != ']' or char != '|' or char != '"' or char != "'" or char != ':' or char != ';' or char != '?' or char != '>' or char != '>' or char != ',' or char != '.' or char != '~' or char != '/' or char != '\\':
					
					self.driver_name_field = True
					self.driver_name_field_error = ''
					
				if char == '!' or char == '@' and char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '(' or char == ')'or  char == '_'or  char == '+'or  char == '-'or  char == '}' or  char == '{' or char == '[' or char == ']' or char == '|' or char == '"' or char == "'" or char == ':' or char == ';' or char == '?' or char == '>' or char == '>' or char == ',' or char == '.' or char == '~' or char == '/' or char == '\\':
					self.driver_name_field = False
					self.driver_name_field_error = 'A Username doesnt have special chars \n'
					break
		elif len(self.ids.username_sign.text) < 5:
			self.driver_name_field = False
			self.driver_name_field_error = 'A Username must have at least 6 alphanumeric chars \n'


		if len(self.ids.password_sign.text) >= 7:	
			if self.ids.password_sign.text == self.ids.password_signconfirm.text:
				self.driver_password_field = True
				self.driver_password_field_error = ''
			elif self.ids.password_sign.text != self.ids.password_signconfirm.text:
				self.driver_password_field = False
				self.driver_password_field_error = 'Passwords Doesnt match \n'

		elif len(self.ids.password_sign.text) < 7:
			self.driver_password_field_error = 'A Password must have at least 8 chars \n'
			self.ids.driver_password_field = False

		if len(self.ids.email.text) < 4:
			self.email_field_error = 'invalid email \n'
		elif len(self.ids.email.text) >=4 :
			self.mailchar = '@'
			self.mailchar_count = 0
			for char in self.ids.email.text:
				if char == self.mailchar:
					self.mailchar_count = self.mailchar_count + 1
					if self.mailchar_count >1:
						self.email_field_error = 'invalid email \n'
						self.email_field = False

						break
						
			if self.mailchar_count == 0:
				self.email_field_error = 'invalid email \n'
				print(self.email_field)		
			else:
				self.email_field = True
				self.email_field_error = ''
				
		self.ids.error_string.text = self.driver_name_field_error + self.driver_password_field_error +self.email_field_error



		if self.driver_name_field == True and self.driver_password_field == True and self.email_field == True:
			self.ids.error_string.text = self.driver_name_field_error + self.driver_password_field_error + self.email_field_error	
			sub_packet = who + '|' + self.ids.username_sign.text+ '|' +self.ids.password_sign.text+ '|' +self.ids.email.text
			Clock.schedule_interval(self.update_error_req, 0.5)

			conto_sub_one_time = True


			#print(self.width)
			
	def update_error_req(self, *args):
		global error_request, subed, username
		print(sub_packet_answer_decoded.split('|')[0])
		if error_request != '':
			self.ids.error_string.text  = error_request 
			error_request = ''
			Clock.unschedule(self.update_error_req)
			

		if subed == True:
			
			theapp.screenm.current = "first screen"
			Clock.unschedule(self.update_error_req)
		



	def as_driver(self):
		self.ids.bt_driver.background_color = [0, 0, 0, 0.2]
		self.ids.as_driver_label.color = [1 , 0, 0, 1]


		self.ids.bt_user.background_color = [0, 0, 0, 0]
		self.ids.as_user_label.color = [0 , 0, 0, 1]

	def as_user(self):
		self.ids.bt_driver.background_color = [0, 0, 0, 0]
		self.ids.as_driver_label.color = [0 , 0, 0, 1]


		self.ids.bt_user.background_color = [0, 0, 0, 0.2]
		self.ids.as_user_label.color = [1 , 0, 0, 1]

	def select_avatar(self):
		from plyer import filechooser	
		filechooser.open_file(on_selection = self.selected)


	def selected(self, selection):      
		global av_pickle
		##############  make sure its jpeg or jpg or png  or u ll  get a file INCLUSION attack if selected[-1]+ selected[-2]+ selected
		self.av_source = str(selection[0])
		self.w = 64
		self.h = 64
		self.av_resized = self.ids.username_sign.text + '.png'                          ###############################
																						############################      change the Image.open to username.png 
		self.img = Image.open('avatar.jpg') 
		self.img = self.img.resize((self.w, self.h), Image.ANTIALIAS)
		self.img.save(self.av_resized)
		av_pickle = self.av_resized





		
		print(av_pickle)
		print(str(selection[0]))
		print(selection)

		
		
	def backtologin(self):
		self.ids.error_string.text = ''
		self.driver_name_field_error = ''
		self.driver_password_field_error = ''
		self.email_field_error = ''

		self.ids.password_signconfirm.text = ''
		self.ids.password_sign.text = ''
		self.ids.username_sign.text = ''
		self.ids.email.text = ''
		self.ids.btn_create.disabled = False
		who = ''
		theapp.screenm.current = "loginscreen"


###### THIS TAgs are awesome really if u have above 1000 lines just start using some visuel refrence
######        i have a low memory i cant remember where i have that code 

##################################################################################################################################################################################
#     #############     #      ############     #     #########     #              #     ##########               #             ######################################################################################################################
#      ###########      #       ###########     #      ########     #              #      #########               #             #######################################################################################################################
#       #########       #        ##########     #       #######     #              #       ########               #     #################################################################################################################################
#        #######        #         ###############        ######     #     ##########        #######     ###########     #############################################################################################################
#         #####         #          ##############         #####     #     ##########         ######     ###########     ####################################################################################################################
#     #    ###    #     #           #######     #          ####     #     ##########          #####     ###########     ##############################################################################################################################
#     ##         ##     #     #      ######     #           ###     #             ##     #     ####     ###########     #########################################################################################################################################
#     ###       ###     #     ##      #####     #     #      ##     #             ##     ##     ###     ###########            ########################################################################################################################################
#     ####     ####     #     ###      ####     #     ##      #     #     ##########     ###     ##     ###########            ##############################################################################################################################
#     #####   #####     #     ####      ###     #     ###           #     ##########     ####     #     ###########     ################################################################################################################################
#     #############     #                ##     #     ####          #     ##########                    ###########     ########################################################################################################################
#     #############     #                 #     #     #####         #     ##########                    ###########     ########################################################################################################################
#     #############     #     #######           #     ######        #     ##########     #######                  #             #############################################################################################################################
#     #############     #     ########          #     #######       #     ##########     ########                 #             ##########################################################################################################################
#     #############     #     #########         #     ########      #     ##########     #########                #             #######################################################################################################################
#################################################################################################################################################################################


class fscreen(Widget):
	my_avat = StringProperty()
	rec_pos = NumericProperty()
	rec_pos_header = NumericProperty()
	expand_pop_button_source = StringProperty()
	def __init__(self, **kwargs):
		global myip, body, headers, username, request_drivers_packet, conto_request_drivers_one_time, who, request_drivers_packet_answer_deocded, update_packet, conto_update_socket_one_time, req_full_recv, av_pickle, chat_send_packet, conto_chat_send_socket_one_time, new_notif, new_notif_bool
		super().__init__(**kwargs)
		self.opened_chat = False
		self.chat_from = ''
		self.start_lon = 0
		self.start_lat = 0
		self.end_lat = 0
		self.end_lon = 0
		self.route_points = []
		self.list_of_lines = []


 					############ some initials  i dont know why i added them i REALLY DONT KNOW DONT ASK ME PLEASE					
		self.corrected = False
		
		self.list_of_unique_in_newnotif = []
		self.list_of_conver = False
		self.show_notif = False
		self.list_of_users_in_newnotif = []
		self.jar = []
		self.rec_pos = self.width*10
		self.driver_ip = ''
		self.current_show_list = []
		self.void_list = []

		Clock.schedule_interval(self.update_my_profile, 0.5)
		Clock.schedule_interval(self.update_state, 7)
		Clock.schedule_interval(self.who_update, 1)
		Clock.schedule_interval(self.update_new_notif, 2)
		Clock.schedule_interval(self.current_location, 0.5)
		Clock.schedule_interval(self.my_mark_animation, 1/40)
		Clock.schedule_interval(self.my_mark_animation_alive, 1/40)
		Clock.schedule_interval(self.search_for_animation, 1/40)



		self.initial_request = False
		self.drop_cond = False
		self.droped = False
		self.tch = 0
		self.mylat = 3.6
		self.mylon = 2
		self.ids.main_map.zoom = 11
		self.showing = False
		self.mrk_obj = MapMarkerPopup(lat= self.mylat, lon= self.mylon, source='1px.png')
		self.radiusmarker = MapMarkerPopup(lat= self.mylat, lon= self.mylon, source='1px.png')
		self.search_box_anim_down = False
		self.search_box_anim_up = False
		self.update_circle = False
		self.slider_circle_size = 0
		self.me_circle_x = 0
		self.me_circle_y = 0
		self.circlesize1 = 0
		self.circle_list = []
		self.slider_circle_x = 0
		self.slider_circle_y = 0
		self.circle1 = Line(circle=(0,0,0),width=0)
		self.slider_circle = Line(circle=(0,0,0),width=0)


		self.x = self.width
		self.y = self.height
		with self.canvas:
			Color(0,0,0,1)
			self.circle1 = Line(circle=(self.me_circle_x, self.me_circle_y, 0),width=2)
			self.circle_list.append(self.circle1)
			Color(0.6,0,1,0.3)
			self.slider_circle = Line(circle=(self.width*2, self.slider_circle_y, 0),width=12)
			self.circle_list.append(self.slider_circle)

		

####################### this ON ANDROID ONLY ###########################################
########################################################################################
#########################################################################################
########################################################################################
	def on_size(self, *args):
		self.x = self.width
		self.y = self.height
		if self.width > 100:
			self.rec_pos = self.width*1.1
			print('on size:' + str(self.width))
			self.rec_pos_header = self.width*1.1
			self.corrected = True

	def who_update(self, *args):  ##### STOP its not fuckkking dr who its just a funcktion          and ITS AFUCKING HACK STOP IT

		if who == 'driver':
			self.ids.drivers.pos[0] = self.width*1.1
			self.ids.drivers_label.pos[0] = self.width*1.1
			

		if who == 'user':
			self.ids.drivers.pos[0] = self.width*0.89
			self.ids.drivers_label.pos[0] = self.width*0.9325
			

	def current_location(self, *args):
		if platform == 'android':
			from plyer import gps
			gps.configure(on_location=self.updatemyloc, on_status=self.on_auth_status)
			gps.start(minTime=1000, minDistance=0)
		
	def updatemyloc(self, *args, **kwargs):  ###### Android gps.configure update
		self.mylat = kwargs['lat']
		self.mylon = kwargs['lon']
		self.ids.main_map.lat = self.mylat
		self.ids.main_map.lon = self.mylon
		self.ids.main_map_me.lat = self.mylat
		self.ids.main_map_me.lon = self.mylon



	def on_auth_status(self, general_status, status_messgae):
		if general_status == 'provider-enabled':
			pass		
		else:
			print('enable GPS please')

	def my_mark_animation(self, *args): #### well it is still got a bug sometimes when u have a screen
										####  put on the table u cant move widgets to table or just 
										###   a mapview bug 

		if self.x > 100 and self.y > 100:
			self.me_circle_x = self.ids.main_map_me.pos[0]
			self.me_circle_y = self.ids.main_map_me.pos[1]
			self.circlesize1 = self.circlesize1 + self.x*0.001
			if self.circlesize1 >= self.ids.main_map_me.size[0]*0.8:
				self.circlesize1 = self.ids.main_map_me.size[0]*0.5



	def my_mark_animation_alive(self, *args):
			self.circle_list[0].circle = [self.me_circle_x+self.ids.main_map_me.size[0]/2, self.me_circle_y+self.ids.main_map_me.size[1]/2, self.circlesize1]


	def center_me(self):  ########## i love this one line functions  SO much
		self.ids.main_map_me.lat = 36.59308912856339
		self.ids.main_map_me.lon = 3.006193661499026
		self.ids.main_map.center_on(self.ids.main_map_me.lat, self.ids.main_map_me.lon)





	def press_me(self):
		print('pressed')

	def rooting(self):
		pass


	

	def request_ride(self):
		pass

	def pin_drop(self):
		self.drop_cond = True

	def remove_pin(self, instance): #####  poor graphics, poor coding, poor taste, or just lazy
		pass
	def on_touch_up(self, touch):  ######## i dont know who have done this another hacking kid with a keyboard
								  ##### i discust* my self     
		    	 
		if touch.x < self.width*0.9:
			if self.drop_cond == True and self.droped == False:
				print(self.ids.main_map.get_latlon_at(touch.x,touch.y))
				self.pin_lat = self.ids.main_map.get_latlon_at(touch.x,touch.y)[0]
				self.pin_lon= self.ids.main_map.get_latlon_at(touch.x,touch.y)[1]
				self.pin_marker = MapMarkerPopup(lat=self.pin_lat, lon=self.pin_lon, source='dropp.png')				
				#self.remove = Button(text='X', size_hint=(0.5, 0.5), pos=(2, 2), font_size = self.height*0.023, font_name='fonts/cello-sans/hinted-CelloSans-Bold.ttf', background_color=(0,0,0,0), color=(1,0,0,1),on_press=self.remove_pin)
				#self.pin_marker.add_widget(self.ids.rmpin)
				self.ids.main_map.add_widget(self.pin_marker)
				self.ids.rmpin.pos[0] = self.pin_marker.pos[0] + 0.5*self.pin_marker.size[0]
				self.ids.rmpin.pos[1] = self.pin_marker.pos[1] + self.pin_marker.size[1]

				self.ids.route.pos[0] = self.pin_marker.pos[0] - 0.25*self.pin_marker.size[0]
				self.ids.route.pos[1] = self.pin_marker.pos[1] + self.pin_marker.size[1]

				self.droped = True
				self.drop_cond = False
				Clock.schedule_interval(self.update_rm_pin_pos, 1/50)


	def rm_pin(self):
		
		Clock.unschedule(self.update_rm_pin_pos)
		self.ids.main_map.remove_widget(self.pin_marker)                              ####
		self.droped = False
		self.ids.rmpin.pos[0] = self.width*1.1 
		self.ids.rmpin.pos[1] = self.height*1.1
		self.ids.route.pos[0] = self.width*1.1
		self.ids.route.pos[1] = self.height*1.1

	def update_rm_pin_pos(self, *args):
		self.ids.rmpin.pos[0] = self.pin_marker.pos[0] + 0.5*self.pin_marker.size[0]
		self.ids.rmpin.pos[1] = self.pin_marker.pos[1] + self.pin_marker.size[1]
		self.ids.route.pos[0] = self.pin_marker.pos[0] - 0.25*self.pin_marker.size[0]
		self.ids.route.pos[1] = self.pin_marker.pos[1] + self.pin_marker.size[1]



	def btn_route(self):
		
		global body, headers
		self.start_lon = self.ids.main_map_me.lon   # can be also as text
		self.start_lat = self.ids.main_map_me.lat  # can be also as text

		self.end_lon = self.pin_marker.lon    # can be also as text
		self.end_lat = self.pin_marker.lat    # can be also as text

		print('start_lon :' + str(self.start_lon))
		print('start_lat :' + str(self.start_lat))
		print('end_lon :' + str(self.end_lon))
		print('end_lat :' + str(self.end_lat))


		body = {"coordinates":[[self.start_lon,self.start_lat],[self.end_lon,self.end_lat]]}

		headers = {
		    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
		    'Authorization': '5b3ce3597851110001cf6248e32f3f787ba541e8b3d916f4681b9340',
		    'Content-Type': 'application/json; charset=utf-8'
		}

		self.call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car/gpx', json=body, headers=headers)
		self.string = self.call.text
		self.tag = 'rtept'
		self.reg_str = '</' + self.tag + '>(.*?)' + '>'
		self.res = re.findall(self.reg_str, self.string)
		print(str(self.res))
		print('_____________________________________')
		self.string1 = str(self.res)
		self.tag1 = '"'
		self.reg_str1 = '"' + '(.*?)' + '"'
		self.res1 = re.findall(self.reg_str1, self.string1)
		self.final =[]
		self.final = self.res1
		self.flt = []
		for i in range(0, len(self.final)-1, 1):
				self.flt.append(self.final[i])

		print(self.flt)
		self.route_points = []
		for i in range(0,len(self.flt)-1, 2):
			self.pointmark = MapMarkerPopup(lat=self.flt[i], lon=self.flt[i+1], source='waypoints.png')
			self.ids.main_map.add_widget(self.pointmark)
			self.route_points.append(self.pointmark)

	

		self.list_of_lines = []
		with self.canvas:
			Color(0.05, 0.92, 0.95, 0.6)
			for j in range(0, len(self.route_points)-1, 1):
				self.lines = Line(points=(self.route_points[j].pos[0], self.route_points[j].pos[1], self.route_points[j+1].pos[0], self.route_points[j+1].pos[1]),width=10)
				print('drawing')
				self.list_of_lines.append(self.lines)

		print('number of route_points is '+str(len(self.route_points)))
		print('number of lines is ' +str(len(self.list_of_lines)))
		Clock.schedule_interval(self.update_route_lines, 1/10)

	def update_route_lines(self, *args):
		for j in range(1, len(self.route_points), 1):
			self.list_of_lines[j-1].points = [self.route_points[j-1].pos[0],self.route_points[j-1].pos[1], self.route_points[j].pos[0], self.route_points[j].pos[1]]

	def btnshow_drivers(self):  ########## this calling the Thread of requests to get some milk

		global request_drivers_packet, conto_request_drivers_one_time		
		request_drivers_packet = 'user1'+'|'+str(self.ids.main_map_me.lat)+'|'+str(self.ids.main_map_me.lon)+'|'+str(self.radius_length)
								#### fix this ####
		conto_request_drivers_one_time = True
		print(request_drivers_packet)
		Clock.schedule_interval(self.update_the_show, 1)


	def update_the_show(self, *args):  #### filling the cup with some milk ofc

		global request_drivers_packet_answer_deocded, req_full_recv
		if self.initial_request == True:
			for obj in self.mrks:
				self.ids.main_map.remove_widget(obj)
		self.mrks = []
		self.list_enum = 0
		if req_full_recv == True:
			self.current_show_list = request_drivers_packet_answer_deocded
			self.i = 0
			for drivers in self.current_show_list:
				self.mrk_obj = MapMarkerPopup(lat=float(drivers[3]), lon=float(drivers[4]),source=drivers[8])

				self.mrk_obj.add_widget(Button(text='Chat:'+drivers[0] , size_hint=(0.5, 0.5), font_size = self.height*0.018, background_color=(0,0,0,0.3), color=(0,0,0,1), font_name= 'fonts/cello-sans/hinted-CelloSans-BoldItalic.ttf', on_press=self.chat_with))


				self.ids.main_map.add_widget(self.mrk_obj)
				self.mrks.append(self.mrk_obj)
				
				self.showing = True
				print('showing'+str(self.showing))
				self.initial_request = True
				#self.ids.clear_drivers.pos[0] = self.width*0.8
				#self.ids.clear_label.pos[0] = self.width*0.835
				
				self.ids.slider_driver.pos[0] = self.width*1.1
				self.ids.km_label.pos[0] = self.width*1.1
				self.ids.show_drivers.pos[0] = self.width*1.1
				self.ids.show_label.pos[0] = self.width*1.1
				self.ids.clear_drivers.pos[0] = self.width*0.89 
				self.ids.clear_drivers.pos[1] = self.height*0.61

				self.ids.clear_label.pos[0] = self.width*0.93
				self.ids.clear_label.pos[1] = self.height*0.59



		Clock.unschedule(self.update_the_show)
 

	def btnclear_drivers(self):  #### for some stranger just remeber that MapMarkerPopups are objects
								#####    STORE them so u wont end with a d**k in ur hand trying to remove them later 
		for obj in self.mrks:
			self.ids.main_map.remove_widget(obj)

		self.ids.clear_drivers.pos[0] = self.width*2
		self.ids.clear_label.pos[0] = self.width*2
		self.showing = False

	def chat_with(self, instance):
		global chat_send_ip
		print(instance.text)
		print(instance.text.split(':')[1])
		Clock.schedule_interval(self.update_msg_recv, 1)
		Clock.schedule_interval(self.animate_chat_pop, 1/60)
		self.opened_chat = True
		self.chat_from = instance.text.split(':')[1]
		print('chat from      '+self.chat_from)

		for drivers in self.current_show_list:

			print(drivers[0])
			print(drivers[6])
			if instance.text.split(':')[1] == drivers[0]:
				print('incond : '+ drivers[6])
				self.ids.chat_header.text = 'Chat With :'+drivers[0]+':'+ reciever_state            
				chat_send_ip = drivers[6]				 												
				break																	
																			

		if self.showing == True:
			self.ids.clear_drivers.pos[0] = self.width*0.89 
			self.ids.clear_drivers.pos[1] = self.height*0.61

			self.ids.clear_label.pos[0] = self.width*0.93
			self.ids.clear_label.pos[1] = self.height*0.59
			self.ids.slider_driver.pos[0] = self.width*1.1
			self.ids.km_label.pos[0] = self.width*1.1
			self.ids.show_drivers.pos[0] = self.width*1.1
			self.ids.show_label.pos[0] = self.width*1.1
			self.opened_chat = True



					
		
	def update_new_notif(self, *args):
		global new_notif_bool, new_notif
		self.cnt_notif = 0
		if new_notif_bool == True:

			self.void_list = []
			self.breaking = False
			self.ids.notif_img.source = 'notif.png'	
			self.cnt_notif = 0
			self.new_notif_number = 0
			
			for notif in new_notif:
				self.cnt_notif = 0
				self.new_notif_number = self.new_notif_number + 1 
				for target in new_notif:
					if target.split('|')[0] == notif.split('|')[0]:
						self.cnt_notif = self.cnt_notif + 1
					if self.cnt_notif == 2:
						break
				if self.cnt_notif < 2:
					self.list_of_unique_in_newnotif.append(notif.split('|')[0])
			print(self.list_of_unique_in_newnotif)	
			for users in self.list_of_unique_in_newnotif:
				self.msg = ''
				for notif in new_notif:
					if users == notif.split('|')[0]:
						self.msg = self.msg + '\n' + notif.split('|')[1]
				#print(users.split('|')[0] + self.msg)
				self.void_list.append(users.split('|')[0] + '|' + self.msg)
			print(self.void_list)
			self.ids.notif_numbers.text = str(self.new_notif_number)
			#self.list_of_unique_in_newnotif = []
			#new_notif = []

			new_notif_bool = False

	def btn_close_chat(self):
		global chat_send_ip
#		self.ids.scroll_rectangle.pos[0] = self.width*0.2
		self.rec_pos = self.width*1.1
		self.ids.scrolled_chat.pos[0] = self.width*1.1
		self.ids.chat_header.pos[0] = self.width*1.1
		self.ids.close_current_chat.pos[0] = self.width*1.1
		self.ids.chat_push_to_scroll.pos[0] = self.width*1.1
		self.ids.chat_send.pos[0] = self.width*1.1
		self.rec_pos_header = self.width*1.1
		self.opened_chat = False
		
		#chat_send_ip = ''
		#self.chat_from = ''


	def btn_notif(self):
		global new_notif_bool, chat_send_ip, conto_chat_send_socket_one_time
		print('on click' + str(self.show_notif))

			#chat_send_ip = ''
			#self.chat_from = ''

			
			
		self.start_h = self.height*0.84
		if self.show_notif == False:
			self.list_of_imgg = []
			self.list_of_conver = []
			print('in False')
			for notif in self.void_list:			
				self.btn_conversation = Button(text= notif.split('|')[0], size=(self.width*0.05, self.height*0.05), pos=(self.width*0.045, self.start_h+self.width*0.02), font_size = self.width*0.001, on_press=self.open_conver)	
				self.ids.main_map.add_widget(self.btn_conversation)
				self.list_of_conver.append(self.btn_conversation)

				self.imgg = kivy.uix.image.Image(source=notif.split('|')[0]+'.png', size=(self.width*0.09, self.width*0.09), pos=(self.width*0.02, self.start_h))
				self.ids.main_map.add_widget(self.imgg)
				self.list_of_imgg.append(self.imgg)
				self.start_h = self.start_h - self.width*0.092
			self.show_notif = True
			print('in false after '+ str(self.show_notif))
			print(self.list_of_imgg)
			print(self.list_of_conver)

		elif self.show_notif == True:
			print(self.list_of_imgg)
			print(self.list_of_conver)

			print('in true')
			for btn_conversation in self.list_of_conver:		
				self.ids.main_map.remove_widget(btn_conversation)
				print('removing btn')

			for imgg in self.list_of_imgg:			
				self.ids.main_map.remove_widget(imgg)
				print('remoiving img')

			self.show_notif = False
			print('in true after '+ str(self.show_notif))


		self.btn_close_chat()	
			


	def open_conver(self, instance):
		global new_notif, chat_send_ip
		print(instance.text)
		for conver in self.void_list:
			if instance.text == conver.split('|')[0]:
				print(conver.split('|')[1])
				self.ids.chat_header.text = 'Chat with :' + instance.text + ':' + reciever_state
				self.ids.inscroll_msgs.text = self.ids.inscroll_msgs.text + conver.split('|')[1]
				
				self.chat_from = conver.split('|')[0]
				Clock.schedule_interval(self.update_msg_recv, 1)
				Clock.schedule_interval(self.animate_chat_pop, 1/60)
				for elem in new_notif:
					if elem.split('|')[0] == instance.text:
						chat_send_ip = elem.split('|')[2]
		self.btn_notif()
		self.opened_chat = True

	def update_msg_recv(self, *args):
		global new_notif
		print('opened chat ' + str(self.opened_chat))
		if self.opened_chat == True:
			if self.chat_from == self.ids.chat_header.text.split(':')[1]:
				self.count_void = -1
				for msg in self.void_list:
					self.count_void = self.count_void + 1
					if msg.split('|')[0] == self.ids.chat_header.text.split(':')[1]:

						if msg.split('|')[1] != self.ids.inscroll_msgs.text:

							print('update msg = ' + msg.split('|')[1])
							print('update inscrollmsg = ' + self.ids.inscroll_msgs.text)
							self.ids.inscroll_msgs.text = self.ids.inscroll_msgs.text + '\n' + msg.split('|')[1].split('\n')[-1] 

							print(self.void_list)
							print(self.count_void)

							self.void_list[self.count_void] = msg.split('|')[0] + self.ids.inscroll_msgs.text 
							break

	def btn_chat_push_to_scroll(self):
		global chat_send_packet, conto_chat_send_socket_one_time, chat_send_ip, username
		if self.ids.chat_send != '':
			chat_send_packet = username + '|' + username + ':' +self.ids.chat_send.text + '|' + myip

			#print('packet_chat_send __fromapp  ' + chat_send_packet)
			self.ids.inscroll_msgs.text = self.ids.inscroll_msgs.text + '\n' + username + ': ' +  self.ids.chat_send.text
			self.ids.chat_send.text = ''
			print(chat_send_ip)

			conto_chat_send_socket_one_time = True
			#print('conto_chat_send_one_time __fromapp ' + str(conto_chat_send_socket_one_time))
			#print('chat_send_ip ___fromapp' + chat_send_ip) 
				



		

	def animate_chat_pop(self, *args):
		self.opened_chat = True
		if self.rec_pos > self.width*0.03:
			#self.rec_pos = self.rec_pos - self.width*0.001
			if self.ids.close_current_chat.pos[0] > self.width*0.822:
				self.ids.close_current_chat.pos[0] = self.ids.close_current_chat.pos[0] - self.width*0.02

			if self.ids.chat_header.pos[0] >= self.width*0.15:	

				self.ids.chat_header.pos[0] = self.ids.chat_header.pos[0] - self.width*0.02	
			if self.rec_pos_header >= self.width*0.1:
				self.rec_pos_header = self.rec_pos_header - self.width*0.02

			if self.ids.chat_push_to_scroll.pos[0] >= self.width*0.82:
				self.ids.chat_push_to_scroll.pos[0] = self.ids.chat_push_to_scroll.pos[0] - self.width*0.02
		

			self.ids.scrolled_chat.pos[0] = self.ids.scrolled_chat.pos[0] - self.width*0.02			
			self.rec_pos = self.rec_pos - self.width*0.02
			self.ids.chat_send.pos[0] = self.ids.chat_send.pos[0] - self.width*0.02 
		if self.rec_pos <= self.width*0.03:
			Clock.unschedule(self.animate_chat_pop)

		


	def search_for(self):
		if self.ids.search_box.pos[1] >= self.height*1:
			self.search_box_anim_down = True
			self.search_box_anim_up = False

		elif self.ids.search_box.pos[1] <= self.height*0.94:
			self.search_box_anim_up = True
			self.search_box_anim_down = False

	def search_for_animation(self, *args): ############  The search Box is buggy get on it please 
											#########         u lazy motherf****


		if self.search_box_anim_up == True and self.ids.search_box.pos[1] <= self.height*1.1:
			self.ids.search_box.pos[1] = self.ids.search_box.pos[1] + self.height*0.01

		elif self.search_box_anim_down == True and self.ids.search_box.pos [1] >= self.height*0.945:
			self.ids.search_box.pos[1] = self.ids.search_box.pos[1] - self.height*0.01


	def btn_drivers(self): 
		if self.showing == True:		    ### I DONT know who wrote this!!. A lot of hacking than coding i dont want to
			self.btnclear_drivers()					   ###   look at it i feel ashamed (crtl mouse wheel the fuck up) 
		self.ids.main_map.zoom = 11	
		self.ids.main_map.center_on(self.ids.main_map_me.lat, self.ids.main_map_me.lon)
		if self.ids.slider_driver.pos[0] >= self.width*1.1:
			#Clock.schedule_interval(self.search_for_animation, 1/40)
			Clock.schedule_interval(self.update_slider_circle, 1/40)
			self.ids.slider_driver.pos[0] = self.width*0.915
			self.ids.km_label.pos[0] = self.width*0.918
			self.ids.show_drivers.pos[0] = self.width*0.89
			self.ids.show_label.pos[0] = self.width*0.93
			self.slider_circle_x = self.ids.main_map_me.pos[0]
			self.slider_circle_y = self.ids.main_map_me.pos[1]

			self.lat_radius = self.ids.main_map_me.lat + (8 /110.574)
			#111.320*cos(latitude) km = 1 lon
			self.lon_radius = self.ids.main_map_me.lon +(8 /111.320*math.cos(self.lat_radius))
			self.radius_length = math.sqrt((self.lat_radius-self.ids.main_map_me.lat)**2 + (self.lon_radius - self.ids.main_map_me.lon)**2)
			self.ids.slider_driver.value = 8
			self.ids.km_label.text = ' Range\n ' + str(8) + ' km'
			self.radiusmarker = MapMarkerPopup(lat= self.lat_radius, lon= self.lon_radius, source='1px.png'  )
			self.ids.main_map.add_widget(self.radiusmarker)
			if self.ids.main_map_me.pos[0] < self.radiusmarker.pos[0]:
				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]
			
			elif self.ids.main_map_me.pos[0] > self.radiusmarker.pos[0]:
				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]		
			


			self.update_circle = True

		elif self.ids.slider_driver.pos[0] < self.width*1.1:
			Clock.unschedule(self.update_slider_circle)         
			self.ids.main_map.remove_widget(self.radiusmarker)
			self.ids.slider_driver.pos[0] = self.width*1.1	
			self.slider_circle_y = self.ids.main_map_me.pos[1]
			self.slider_circle_size = 0
			self.circle_list[1].circle = [self.width*2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, 0]
			self.ids.km_label.pos[0] = self.width*2
			self.ids.show_drivers.pos[0] = self.width*2
			self.update_circle = False
			self.ids.show_label.pos[0] = self.width*2
			if self.showing == False:
				self.ids.clear_drivers.pos[0] = self.width*2
				self.ids.clear_label.pos[0] = self.width*2


	def get_slider_value(self):  ####  this fu??in? mess needs to be cleared of prints and all that shit 
								 ####          JUST CLEAR IT NOW WOULD YOU 


		print(self.ids.slider_driver.value)
		if self.ids.slider_driver.pos[0] == self.width*0.915:
			self.ids.main_map.zoom = 11
			print('this is the zoom: ' + str(self.ids.main_map.zoom))
			print(self.ids.main_map.get_bbox())
			self.ids.km_label.text = ' Range\n ' + str(self.ids.slider_driver.value) + ' km'

			#110.574 km  = 1 lat
			self.lat_radius = self.ids.main_map_me.lat + (self.ids.slider_driver.value /110.574)
			#111.320*cos(latitude) km = 1 lon
			self.lon_radius = self.ids.main_map_me.lon +(self.ids.slider_driver.value /111.320*math.cos(self.lat_radius))
			self.radius_length = math.sqrt((self.lat_radius-self.ids.main_map_me.lat)**2 + (self.lon_radius - self.ids.main_map_me.lon)**2)
			
			print(self.radius_length)
			self.ids.main_map.remove_widget(self.radiusmarker)
			self.radiusmarker = MapMarkerPopup(lat= self.lat_radius, lon= self.lon_radius, source='1px.png' )
			self.ids.main_map.add_widget(self.radiusmarker)
			if self.ids.main_map_me.pos[0] < self.radiusmarker.pos[0]:

				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]
			
			elif self.ids.main_map_me.pos[0] > self.radiusmarker.pos[0]:
				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]
			
			print(self.ids.slider_driver.value)
			print('_________________________________________')
			print('lat radiuss: '+str(self.lat_radius)+'  lon raddius  '+str(self.lon_radius))
			print('lat me: '+str(self.ids.main_map_me.lat)+ ' lon me : '+str(self.ids.main_map_me.lat))
			print('_________________________________________')
			print('xcslider '+str(self.slider_circle_x)+ '  ycslider '+str(self.slider_circle_y)+'  sizecslider '+str(self.slider_circle_size))
			print('xradius  '+ str(self.radiusmarker.pos[0])+ '  yradiuss '+ str(self.radiusmarker.pos[0]))


	def update_slider_circle(self, *args): ###############   this func calcs the radius of the circle based on
		if self.update_circle == True:     ###############		the slider's value 

			self.slider_circle_x = self.ids.main_map_me.pos[0]
			self.slider_circle_y = self.ids.main_map_me.pos[1]		
			if self.ids.main_map_me.pos[0] < self.radiusmarker.pos[0]:
				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]
		
			elif self.ids.main_map_me.pos[0] > self.radiusmarker.pos[0]:
				self.slider_circle_size = math.sqrt((self.radiusmarker.pos[0]**2) - 2*self.radiusmarker.pos[0]*self.ids.main_map_me.pos[0] + (self.radiusmarker.pos[1]**2) - 2*self.radiusmarker.pos[1]*self.ids.main_map_me.pos[1] + (self.ids.main_map_me.pos[0]**2) + (self.ids.main_map_me.pos[1]**2))
				self.circle_list[1].circle = [self.slider_circle_x+self.ids.main_map_me.size[0]/2, self.slider_circle_y+self.ids.main_map_me.size[1]/2, self.slider_circle_size]
			
	
	def update_state(self, *args):   ######## updating state can bug the database on the server 
									#########    its frequency should scale with number of users
									#########    more users means lower frenquency   its just sqlit3  <3 native stuff
		global update_packet, conto_update_socket_one_time, who, username, av_pickle 	
		if username != '':
			self.update_val_lat = self.ids.main_map_me.lat
			self.update_val_lon = self.ids.main_map_me.lon
			self.update_val_state = 'active'		
			update_packet = who + '|' + username + '|' + str(self.update_val_lat) + '|' + str(self.update_val_lon) + '|' + self.update_val_state


			
			conto_update_socket_one_time = True
			



	def btn_myself(self):
		#global av_pickle
		#print(self.my_avat)
		#self.my_avat = av_pickle
		pass

	def update_my_profile(self, *args):
		global username

		if username != '': ############################ DONT be dump search for this FILE before loading it 
			self.my_avat = username +'.png'
			    ########          or go kill urself   right???!!!!
			Clock.unschedule(self.update_my_profile)




class secscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)



class thscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class theapp(App):
	def build(self):
		self.screenm = ScreenManager(transition=FadeTransition())



		self.holderscreen = holderscreen()
		screen = Screen(name = "holderscreen")
		screen.add_widget(self.holderscreen)
		self.screenm.add_widget(screen)

		self.Loginscreen = Loginscreen()
		screen = Screen(name="loginscreen")
		screen.add_widget(self.Loginscreen)
		self.screenm.add_widget(screen)


		self.forgot_screen = forgot_screen()
		screen = Screen(name = "forgot_screen")
		screen.add_widget(self.forgot_screen)
		self.screenm.add_widget(screen)


		self.signinscreen = signinscreen()
		screen = Screen(name = "signinscreen")
		screen.add_widget(self.signinscreen)
		self.screenm.add_widget(screen)	

		self.fscreen = fscreen()
		screen = Screen(name = "first screen")
		screen.add_widget(self.fscreen)
		self.screenm.add_widget(screen)

		self.secscreen = secscreen()
		screen  = Screen(name = "secondscreen")
		screen.add_widget(self.secscreen)
		self.screenm.add_widget(screen)

		self.thscreen = thscreen()
		screen  = Screen(name = "thirdscreen")
		screen.add_widget(self.thscreen)
		self.screenm.add_widget(screen)

		return self.screenm

if __name__ == "__main__":
	theapp = theapp()
	#func_auth_socket()
	thred_func_chat_send_socket.start()
	thred_func_chat_recv_socket.start()
	thread_func_auth_socket.start()								
	thread_func_request_drivers_socket.start()
	thread_func_sub_socket.start()
	thread_func_update_socket.start()
	threading.Thread(target = theapp.run())

chat_recv_socket.close()
conto_auth_socket_fromsaved = True
conto_auth_socket_fromlogin = True
conto_request_drivers_one_time = False
conto_request_drivers = True
conto_sub = True
conto_sub_one_time = False
conto_update_socket_one_time = False
conto_update_socket = True
chat_recv_socket.close()
conto_chat_send_socket = True
conto_chat_send_socket_one_time = False