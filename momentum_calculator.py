def calculate_work(cart_data:tuple) -> str:
    number,list1,cart = cart_data
    mass,vi,vf = list1
    ke_cart_i = (1/2)*mass*(vi)**2
    ke_cart_f = (1/2)*mass*(vf)**2
    return f"{number} {cart} cart : {ke_cart_i:.2f} v_i (J) | {ke_cart_f:.2f} v_f (J)"

def calculate_momentum(cart_data:tuple) -> str:
    number,list1,cart = cart_data
    mass,vi,vf = list1
    delta_p_i = mass*vi
    delta_p_f = mass*vf
    impulse = delta_p_i-delta_p_f
    return f"{number} {cart} cart : {delta_p_i:.2f} kg*m/s (i) | {delta_p_f:.2f} kg*m/s (f)\nImpulse : {impulse:.2f} kg*m/s"

data = [
    (1,(0.4,0,-0.46),'green'),
    (2,(0.4,0,-0.39),'green'),
    (3,(0.4,0,-0.35),'green'),
    (1,(0.3,-0.6,0.15),'gray'),
    (2,(0.3,-0.5,0.13),'gray'),
    (3,(0.3,-0.4,0.12),'gray'),
]
for cart_data in data:
    print(calculate_momentum(cart_data))
    print(calculate_work(cart_data))