import xbmc
import xbmcgui
import xbmcaddon
import os
import threading

# Function to play music using Kodi's player
def play_music(music_folder):
    player = xbmc.Player()
    for music_file in os.listdir(music_folder):
        if music_file.endswith('.mp3'):
            music_path = os.path.join(music_folder, music_file)
            player.play(music_path)
            # Wait for the song to finish
            while player.isPlaying():
                xbmc.sleep(1000)  # Kodi's way of sleeping (milliseconds)

# Simplified slideshow function using Kodi's GUI components
def show_slideshow(image_folder):
    win = xbmcgui.WindowDialog()
    img_control = xbmcgui.ControlImage(0, 0, 1280, 720, '')
    win.addControl(img_control)
    
    for image_file in os.listdir(image_folder):
        if image_file.endswith('.jpg'):
            img_control.setImage(os.path.join(image_folder, image_file))
            xbmc.sleep(5000)  # Display each image for 5 seconds
    
    win.close()

# Example of starting the music and slideshow (adjust paths as needed)
music_folder = '/path/to/your/music'
image_folder = '/path/to/your/images'
threading.Thread(target=play_music, args=(music_folder,)).start()
threading.Thread(target=show_slideshow, args=(image_folder,)).start()
