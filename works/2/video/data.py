import ffmpeg
import numpy as np

class Data:
    _ImgArray = []
    _width = 0
    _height = 0
    _fps = 0
    _FrameAmount:int = 0
    _Lenth:int = 0          # sec
    _audioArray = []
    _audioFrequency = 0

    def IsOk(self) -> bool:
        flag:bool = False
        if(not (self._width and self._height)):
            flag = False
        if(not (self._fps and self._FrameAmount)):
            flag = False
        if(not (self._audioArray and self._audioFrequency)):
            flag = False
        if(not (self._Lenth and self._ImgArray)):
            flag = False
        return flag


# class setData:
    def setVideoFrame(self,vidoeImg):
        self._ImgArray.append(vidoeImg)


    def setVidoefps(self,fps:int):
        self._fps = fps


    def setVidoeSize(self,width:int,height:int):
        self._width = width
        self._height = height


    def setFrameAmount(self,FrameAmount:int):
        self._FrameAmount = FrameAmount


    def setAudioArray(self,audio):
        self._audioArray.append(audio)


    def setAudioFrequency(self,Hz:int):
        self._audioFrequency = Hz

# class getData:
    def getLenth(self) -> int: # sec
        return self._Lenth


    def getVideoFrame(self,index:int):
        return self._ImgArray[index]


    def getFps(self) -> int:
        return self._fps






