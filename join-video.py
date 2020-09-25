# Import everything needed to edit video clips 
from moviepy.editor import *
  
# loading video
clip = VideoFileClip("video1.mp4") 
  
# getting subclip as video is large 
clip1 = clip.subclip(0, 5) 
  
  
# loading video  
clipx = VideoFileClip("video2.mp4") 
  
# getting subclip  
clip2 = clipx.subclip(0, 5) 
  
# clip list 
clips = [clip1, clip2] 
  
# concatinating both the clips 
final = concatenate_videoclips(clips) 
  
# showing final clip 
final.ipython_display(width = 480) 
