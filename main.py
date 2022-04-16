from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import numpy as np
import cv2
from gaze_tracking import GazeTracking

from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


import uuid 
from kivy.uix.label import Label
from gtts import gTTS
import os
import playsound #pip install playsound==1.2.2
import wikipedia

Builder.load_file('layout.kv')
gaze = GazeTracking()

class AndroidCamera(Camera):
    camera_resolution = (640, 480)
    cam_ratio = camera_resolution[0] / camera_resolution[1]

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 1

        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )

        with self.canvas.before:
            Color(255, 225, 225, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MyApp(MDApp):
    counter = 0
    isOnLeft = True
    isOnRight = False
    currentLeftIndex = -1
    currentRightIndex = -1
    prevLeftIndex = -1
    prevRightIndex = -1
    isLeftNotChanged = True
    isRightNotChanged = True
    left = ['Xin chào', 'Vâng', 'Cảm ơn', 'Không', 'Được']
    right = ['Mở tivi', 'Mở nhạc', 'Nước', 'Trái cây', 'Ăn cơm']
    leftIds = []
    rightIds = []
    sentence = ""
    blinking = 0
    wikipedia.set_lang('vi')
    language = 'vi'

    def build(self):
        return MyLayout()
    
    def render(self):        
        for i in range(len(self.left)):
            id = str(uuid.uuid4())
            self.leftIds.append(id);
            btn = Button(text = self.left[i],
                        font_size ="20sp",
                        # background_color =(232,232,232,1),
                        background_normal = 'icontext.png',
                        background_down = 'icontext1.png',
                        border = (30, 30, 30, 30),
                        color =(242, 124, 22, 1),
                        size =(32, 32),
                        size_hint =(.2, .2),
                        font_name = 'FrancoisOne-Regular.ttf'
                        )
            # btn= MDRectangleFlatButton(text= self.left[i],pos_hint={'center_x':0.5,'center_y':0.3})
            self.root.ids[id] = btn   
            self.root.ids.left_grid.add_widget(btn)
        for i in range(len(self.right)):
            id = str(uuid.uuid4())
            self.rightIds.append(id);
            btn = Button(text = self.right[i],
                        # font_size ="20sp",
                        # background_color =(232,232,232,1),
                        # color =(255, 255, 255, 1),
                        # size =(32, 32),
                        # size_hint =(.2, .2)

                        font_size ="20sp",
                        background_normal = 'icontext.png',
                        background_down = 'icontext1.png',
                        border = (30, 30, 30, 30),
                        color =(242, 124, 22, 1),
                        size =(32, 32),
                        size_hint =(.2, .2),
                        font_name = 'FrancoisOne-Regular.ttf'
                        )
            self.root.ids[id] = btn   
            self.root.ids.right_grid.add_widget(btn)

    def on_start(self):
        self.render()
        Clock.schedule_once(self.get_frame, 5)

    def get_frame(self, dt):
        cam = self.root.ids.a_cam
        image_object = cam.export_as_image(scale=round((400 / int(cam.height)), 2))
        w, h = image_object._texture.size
        frame = np.frombuffer(image_object._texture.pixels, 'uint8').reshape(h, w, 4)
        # gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        
        gaze.refresh(frame)
        text = ""

        if gaze.is_blinking():                    
            if self.isOnRight == True:  
                self.currentRightIndex += 1
            if self.isOnLeft == True:  
                self.currentLeftIndex += 1
        elif gaze.is_right():
            if self.isOnRight == False:                
                self.isOnRight = True
                self.isOnLeft = False
                self.currentLeftIndex = -1
        elif gaze.is_left():
            if self.isOnLeft == False:                
                self.isOnRight = False
                self.isOnLeft = True
                self.currentRightIndex = -1
        elif gaze.is_center(): pass
        else: pass
        
        self.counter += 1

        if self.currentRightIndex >= len(self.rightIds): self.currentRightIndex = 0            
        if self.currentLeftIndex >= len(self.leftIds): self.currentLeftIndex = 0            
        
        print(self.isOnLeft, self.isOnRight, self.currentRightIndex, self.currentLeftIndex, self.counter)

        if self.counter == 10:            
            self.counter = 0 
            if self.currentLeftIndex == -1 and self.currentRightIndex == -1: pass                           
            elif self.isLeftNotChanged == True or self.isRightNotChanged == True:     
                if self.isOnLeft == True: 
                    self.sentence = self.left[self.currentLeftIndex]
                    playsound.playsound('l'+str(self.currentLeftIndex)+'.mp3', False)
                    print(self.currentLeftIndex)
                if self.isOnRight == True: 
                    self.sentence = self.right[self.currentRightIndex]   
                    playsound.playsound('r'+str(self.currentRightIndex)+'.mp3', False)     
                    print(self.currentRightIndex)   

                # tts = gTTS(text=self.sentence, lang=self.language, slow=False)
                # mp3 = str(uuid.uuid4()) + ".mp3"
                # tts.save(mp3)
                # playsound.playsound(mp3, True)
                # os.remove(mp3)


        if self.isOnLeft == True:  
            for index in range(len(self.rightIds)):
                id = self.rightIds[index]
                # self.root.ids[id].background_color=(232,232,232,1)
                self.root.ids[id].background_normal = 'icontext.png'
                self.root.ids[id].color  = (212, 184, 22, 1) 
            if self.currentLeftIndex == -1: pass                       
            for index in range(len(self.leftIds)):
                id = self.leftIds[index]                
                # if self.currentLeftIndex == index: self.root.ids[id].background_color=(0, 179, 241, 1)
                # else: self.root.ids[id].background_color=(232,232,232,1)       

                if self.currentLeftIndex == index: 
                    self.root.ids[id].background_normal = 'icontext1.png'
                    self.root.ids[id].color  = (1,1,1, 1)
                else: 
                    self.root.ids[id].background_normal = 'icontext.png'    
                    self.root.ids[id].color  = (212, 184, 22, 1)        
        if self.isOnRight == True:
            for index in range(len(self.leftIds)):
                id = self.leftIds[index]
                # self.root.ids[id].background_color=(232,232,232,1)
                self.root.ids[id].background_normal = 'icontext.png'
                self.root.ids[id].color  = (212, 184, 22, 1) 
            if self.currentRightIndex == -1: pass    
            for index in range(len(self.rightIds)):
                id = self.rightIds[index]
                # if self.currentRightIndex == index: self.root.ids[id].background_color=(0, 179, 241, 1)
                # else: self.root.ids[id].background_color=(232,232,232,1)

                if self.currentRightIndex == index: 
                    self.root.ids[id].color  = (1,1,1, 1)
                    self.root.ids[id].background_normal = 'icontext1.png'
                else: 
                    self.root.ids[id].background_normal = 'icontext.png'  
                    self.root.ids[id].color  = (212, 184, 22, 1)        


        self.root.ids.sentence.text = self.sentence
        self.root.ids.sentence.color = (1, 1, 1, 1)
        self.root.ids.sentence.background_normal = 'icontext2.png'
        self.root.ids.sentence.font_name = 'FrancoisOne-Regular.ttf'
        # self.root.ids.background_color=(232,232,232,1)
        # self.counter += 1
        # print(self.leftIds)
        # print(self.rightIds)
        if self.prevLeftIndex == self.currentLeftIndex: 
            self.isLeftNotChanged = True
        else:
            self.prevLeftIndex = self.currentLeftIndex
            self.isLeftNotChanged = False
        
        if self.prevRightIndex == self.currentRightIndex: 
            self.isRightNotChanged = True
        else:
            self.prevRightIndex = self.currentRightIndex
            self.isRightNotChanged = False

        # print('check: ', text)
        Clock.schedule_once(self.get_frame, 0.3)

if __name__ == "__main__":
    MyApp().run()