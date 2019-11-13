from PIL import Image, ImageDraw


def picture(guesses):
    
    width = 500
    height = 500

    img = Image.new('RGB', (width, height))

    draw = ImageDraw.Draw(img)

    draw.rectangle(((0, 0), (width, height)), fill="white")
    color = (139, 92, 74)  # brown
    if guesses == 9:
        draw.line((100, 440, 400, 440),fill= color, width= 8) # bottom of gallow
    elif guesses == 8:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8) # gallows upright 
    elif guesses == 7:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8) #overhead
    elif guesses == 6:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope

    elif guesses == 5:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')

    elif guesses == 4:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
        draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 

    elif guesses == 3:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
        draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 
        draw.line((200, 230, 250, 230),fill='purple', width= 5) #arms1

    elif guesses == 2:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
        draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 
        draw.line((200, 230, 250, 230),fill='purple', width= 5) #arms1
        draw.line((250, 230, 300, 230),fill='purple', width= 5) #arms2

    elif guesses == 1:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
        draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 
        draw.line((200, 230, 250, 230),fill='purple', width= 5) #arms1
        draw.line((250, 230, 300, 230),fill='purple', width= 5) #arms2
        draw.line((250, 310, 290, 400), fill='purple', width= 8)#legs1

    elif guesses == 0:
        draw.line((100, 440, 400, 440),fill= color, width= 8)
        draw.line((340, 440, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 340, 50),fill= color, width= 8)
        draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
        circle_x = width/2
        circle_y = height/3    #head
        circle_radius = 30
        draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
        draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 
        draw.line((200, 230, 250, 230),fill='purple', width= 5) #arms1
        draw.line((250, 230, 300, 230),fill='purple', width= 5) #arms2
        draw.line((250, 310, 290, 400), fill='purple', width= 8)#legs1
        draw.line((250, 310, 210, 400), fill='purple', width= 8)#legs2
      

    img.show()  


# width = 500
# height = 500
# img = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(img)
# draw.rectangle(((0, 0), (width, height)), fill="white")
# color = (139, 92, 74)  # brown




# draw.line((100, 440, 400, 440),fill= color, width= 8)
# draw.line((340, 440, 340, 50),fill= color, width= 8)
# draw.line((250, 50, 340, 50),fill= color, width= 8)
# draw.line((250, 50, 250, 150),fill='yellow', width= 8) # rope
# circle_x = width/2
# circle_y = height/3    #head
# circle_radius = 30
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
# draw.line((250, 195, 250, 310), fill='purple', width= 10) #body 
# draw.line((200, 230, 250, 230),fill='purple', width= 5) #arms1
# draw.line((250, 230, 300, 230),fill='purple', width= 5) #arms2
# draw.line((250, 310, 290, 400), fill='purple', width= 8)#legs1
# draw.line((250, 310, 210, 400), fill='purple', width= 8)#legs2

# img.show()