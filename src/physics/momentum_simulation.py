from blessed import Terminal
import pymunk
import random
import time

# Initialize terminal and physics space
term = Terminal()
space = pymunk.Space()

# Set parameters
space.gravity = 0,-900
x_cord = random.randint(0,101)
y_cord = random.randint(0,51)
mass = random.randint(1,1000)
radius = random.randint(10,50)
moment = pymunk.moment_for_circle(mass,0,radius)
body = pymunk.Body(mass,moment)
body.position=x_cord,y_cord
circle = pymunk.Circle(body,radius)
circle.elasticity = 0.8
space.add(body,circle)

# Set terminal dimensions
floor_body = space.static_body
floor_shape = pymunk.Segment(floor_body,(0,5),(term.width,5),1)
floor_shape.elasticity = 0.9
space.add(floor_shape)

# Write the simulation
with term.hidden_cursor(),term.cbreak():
    print(term.clear)
    for _ in range(300):
        space.step(1/30)
        x = int(body.position.x)
        y = int(term.height-body.position.y)
        print(term.clear)
        with term.location(0,term.height-5):
            print('-'*term.width)
        if 0<=y<term.height and 0<=x<term.width:
            with term.location(x,y):
                print(term.bold_red('O'))
        with term.location(0,0):
            momentum = body.mass * body.velocity.length
            print(f'Momentum: {momentum:.2f} kg·m/s | Position: ({body.position.x:.2f}, {body.position.y:.2f}) | Velocity: ({body.velocity.x:.2f}, {body.velocity.y:.2f})')
        time.sleep(1/30)