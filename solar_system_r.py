from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import *

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlim3d([-25000000/90, 25000000/90])
ax.set_xlabel('X')

ax.set_ylim3d([-25000000/90, 25000000/90])
ax.set_ylabel('Y')

ax.set_zlim3d([-25000000/90, 25000000/90])
ax.set_zlabel('Z')

days_mercury = 88
days_venus = 225
days_earth = 365
days_mars = 687
days_jupiter = 4332
days_saturn = 10760
days_uranus = 30684
days_neptune = 60188

def Sun():
    # draw sphere
    u, v = mgrid[0:2*pi:50j, 0:pi:50j]
    x = cos(u)*sin(v)*696.34
    y = sin(u)*sin(v)*696.34
    z = cos(v)*696.34
    # alpha controls opacity
    ax.plot_surface(x, y, z, color="y", alpha=1)



def Mercury_orbit():
    L = 9.11*10**38     #L = angular momentum
    m = 3.28*10**23     #m = mass of mercury
    M = 1.99*10**30     #M = mass of sun
    a = 5.8*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.2056        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_mercury)
    radius = zeros([days_mercury])
    theta = zeros([days_mercury])
    x = zeros([days_mercury])
    y = zeros([days_mercury])
    z = zeros([days_mercury])
    
    for i in range(0,days_mercury):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_mercury):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/6.
        
    # alpha controls opacity
    ax.plot(x, y, z, color="blue", alpha=0.5)
    


def Venus_orbit():
    L = 1.8*10**40     #L = angular momentum
    m = 4.87*10**24     #m = mass of venus
    M = 1.99*10**30     #M = mass of sun
    a = 10.8*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.007        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_venus)
    radius = zeros([days_venus])
    theta = zeros([days_venus])
    x = zeros([days_venus])
    y = zeros([days_venus])
    z = zeros([days_venus])
    
    for i in range(0,days_venus):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_venus):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/13.274336283185841
        
    # alpha controls opacity
    ax.plot(x, y, z, color="g", alpha=0.5)



def Earth_orbit():
    L = 2.7*10**40     #L = angular momentum
    m = 5.972*10**24     #m = mass of earth
    M = 1.99*10**30     #M = mass of sun
    a = 14.9*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.017        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_earth)
    radius = zeros([days_earth])
    theta = zeros([days_earth])
    x = zeros([days_earth])
    y = zeros([days_earth])
    z = zeros([days_earth])
    
    for i in range(0,days_earth):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_earth):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= 0
         
    # alpha controls opacity
    ax.plot(x, y, z, color="w", alpha=0.5)



def Mars_orbit():
    L = 3.5*10**39     #L = angular momentum
    m = 6.42*10**23     #m = mass of mars
    M = 1.99*10**30     #M = mass of sun
    a = 22.8*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.0934        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_mars)
    radius = zeros([days_mars])
    theta = zeros([days_mars])
    x = zeros([days_mars])
    y = zeros([days_mars])
    z = zeros([days_mars])
    
    for i in range(0,days_mars):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_mars):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/24.324324324324323
         
    # alpha controls opacity
    ax.plot(x, y, z, color="y", alpha=0.5)



def Jupiter_orbit():
    L = 1.9*10**43     #L = angular momentum
    m = 1.9*10**27     #m = mass of jupiter
    M = 1.99*10**30     #M = mass of sun
    a = 77.8*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.049        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_jupiter)
    radius = zeros([days_jupiter])
    theta = zeros([days_jupiter])
    x = zeros([days_jupiter])
    y = zeros([days_jupiter])
    z = zeros([days_jupiter])
    
    for i in range(0,days_jupiter):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_jupiter):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/34.61538461538461
        
    # alpha controls opacity
    ax.plot(x, y, z, color="orange", alpha=0.5)



def Saturn_orbit():
    L = 7.8*10**42     #L = angular momentum
    m = 5.68*10**26     #m = mass of Saturn
    M = 1.99*10**30     #M = mass of sun
    a = 143.2*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.057        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_saturn)
    radius = zeros([days_saturn])
    theta = zeros([days_saturn])
    x = zeros([days_saturn])
    y = zeros([days_saturn])
    z = zeros([days_saturn])
    
    for i in range(0,days_saturn):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_saturn):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/18.072289156626503
    
    # alpha controls opacity
    ax.plot(x, y, z, color="blue", alpha=0.5)



def Uranus_orbit():
    L = 1.7*10**42     #L = angular momentum
    m = 8.68*10**25     #m = mass of Uranus
    M = 1.99*10**30     #M = mass of sun
    a = 286.7*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.046        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_uranus)
    radius = zeros([days_uranus])
    theta = zeros([days_uranus])
    x = zeros([days_uranus])
    y = zeros([days_uranus])
    z = zeros([days_uranus])
    
    for i in range(0,days_uranus):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_uranus):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/58.44155844155844
    
    # alpha controls opacity
    ax.plot(x, y, z, color="w", alpha=0.5)



def Neptune_orbit():
    L = 2.5*10**42     #L = angular momentum
    m = 1.02*10**26     #m = mass of Neptune
    M = 1.99*10**30     #M = mass of sun
    a = 451.5*10**10      #a = semi-major axis
    G = 6.674*10**-11   #G = Gravitational constant
    k = G*M*m        
    E = -k/(2*a)        #E = energy
    p = L**2/(m*k)   
    c = 1 + (2*E*L**2)/(m*k**2)
    e = 0.011        #e = eccentricity
    
    def fx(x):
        r = p/(1 + e*cos(x))
        return r
    
    phi =linspace(0,2*pi,days_neptune)
    radius = zeros([days_neptune])
    theta = zeros([days_neptune])
    x = zeros([days_neptune])
    y = zeros([days_neptune])
    z = zeros([days_neptune])
    
    for i in range(0,days_neptune):
        radius[i] = fx(phi[i])
        theta[i] = 180*phi[i]/pi
    
    for i in range(0,days_neptune):
        x[i] = radius[i]*cos(phi[i])/10000000
        y[i] = radius[i]*sin(phi[i])/10000000
        z[i]= x[i]/25.423728813559322
         
    # alpha controls opacity
    ax.plot(x, y, z, color="g", alpha=0.5)



def Finishing_touch():
    ax.set_title('Solar System')
    ax.set_facecolor('xkcd:black')
    ax.set_facecolor((0, 0, 0))
    
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['right'].set_linewidth(3)
    ax.spines['left'].set_color('white')
    ax.spines['left'].set_lw(3)
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.zaxis.label.set_color('white')
    ax.tick_params(colors='white', which='both')
    ax.title.set_color('white')




Sun()
Mercury_orbit()
Venus_orbit()
Earth_orbit()
Mars_orbit()
Jupiter_orbit()
Saturn_orbit()
Uranus_orbit()
Neptune_orbit()
Finishing_touch()
plt.show()