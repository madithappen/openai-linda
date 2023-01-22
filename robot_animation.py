import pyglet

animation = pyglet.image.load_animation('docs/robot.gif')
animSprite = pyglet.sprite.Sprite(animation)

gifWidth, gifHeight = 800, 600

win = pyglet.window.Window(width=gifWidth, height=gifHeight)

@win.event
def on_draw():
    win.clear()
    animSprite.draw()

# Start the pyglet event loop
pyglet.app.run()

# Do other stuff here
while True:
    # Update the window
    pyglet.clock.tick()
    # Do other stuff here