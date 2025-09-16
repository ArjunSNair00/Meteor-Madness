# ===========================================
# - Title:  3D Solar System Simulation
# - Author: @zerot69 (Updated)
# - Date:   16 Sep 2025
# - Features: 3D Camera, Left/Right/Middle Drag, WASD Movement
# ============================================

import pygame
import math

pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
COLOR_WHITE = (255, 255, 255)
COLOR_UNIVERSE = (36, 36, 36)
COLOR_SUN = (252, 150, 1)
COLOR_MERCURY = (173, 168, 165)
COLOR_VENUS = (227, 158, 28)
COLOR_EARTH = (107, 147, 214)
COLOR_MARS = (193, 68, 14)
COLOR_JUPITER = (216, 202, 157)
COLOR_SATURN = (191, 189, 175)
COLOR_URANUS = (209, 231, 231)
COLOR_NEPTUNE = (63, 84, 186)
FONT_1 = pygame.font.SysFont("Trebuchet MS", 21)
FONT_2 = pygame.font.SysFont("Trebuchet MS", 16)
pygame.display.set_caption("3D Solar System Simulation")

# ----------------- Camera -----------------
cam_pos = [0.0, 50.0, 200.0]      # Camera position
look_at = [0.0, 0.0, 0.0]         # Camera target
up_vector = [0.0, 1.0, 0.0]
focal_length = 500.0

yaw = 0.0     # rotation around Y axis
pitch = 0.0   # rotation around X axis
rotation_speed = 0.005
pan_speed = 0.3
zoom_speed = 0.5
move_speed = 5.0

# ----------------- Planet Class -----------------
class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    TIMESTEP = 60 * 60 * 24 * 2
    SCALE = 200 / AU

    def __init__(self, x, y, z, radius, color, mass):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def draw(self, window, show_distance, draw_line):
      proj = project((self.x, self.y, self.z))
      if proj is None:
          return  # skip if planet is behind camera
      sx, sy = proj
      # Draw orbit
      if len(self.orbit) > 2 and draw_line:
          projected_orbit = []
          for p in self.orbit:
              pr = project(p)
              if pr is not None:
                  projected_orbit.append(pr)
          if len(projected_orbit) > 1:
              pygame.draw.lines(window, self.color, False, projected_orbit, 1)
      # Draw planet
      pygame.draw.circle(window, self.color, (int(sx), int(sy)), max(int(self.radius), 1))
      # Draw distance
      if show_distance and not self.sun:
          dist_text = FONT_2.render(
              f"{round(self.distance_to_sun * 1.057 * 10**-16, 8)} ly", True, COLOR_WHITE
          )
          window.blit(dist_text, (sx - dist_text.get_width()/2, sy - 20))


    def attraction(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dz = other.z - self.z
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance**2
        fx = force * dx / distance
        fy = force * dy / distance
        fz = force * dz / distance
        return fx, fy, fz

    def update_position(self, planets):
        total_fx = total_fy = total_fz = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy, fz = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            total_fz += fz
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.z_vel += total_fz / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.z += self.z_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y, self.z))

    def update_scale(self, scale):
        self.radius *= scale

# ----------------- Projection -----------------
def project(point3d):
    x, y, z = point3d
    dx = x - cam_pos[0]
    dy = y - cam_pos[1]
    dz = z - cam_pos[2]
    if dz <= 0:
        return None  # behind camera
    sx = WIDTH/2 + dx * focal_length / dz
    sy = HEIGHT/2 - dy * focal_length / dz
    return sx, sy

# ----------------- Main -----------------
def main():
    global cam_pos, look_at, yaw, pitch

    run = True
    pause = False
    show_distance = False
    draw_line = True
    clock = pygame.time.Clock()

    # Mouse states
    left_drag = False
    middle_drag = False
    right_drag = False
    last_mouse = [0, 0]

    # Planets
    sun = Planet(0, 0, 0, 20, COLOR_SUN, 1.98892e30); sun.sun = True
    mercury = Planet(-0.387*Planet.AU, 0, 0, 5, COLOR_MERCURY, 3.30e23); mercury.y_vel = 47.4e3
    venus = Planet(-0.723*Planet.AU, 0, 0, 9, COLOR_VENUS, 4.8685e24); venus.y_vel = 35.02e3
    earth = Planet(-1*Planet.AU, 0, 0, 10, COLOR_EARTH, 5.9722e24); earth.y_vel = 29.783e3
    mars = Planet(-1.524*Planet.AU, 0, 0, 5, COLOR_MARS, 6.39e23); mars.y_vel = 24.077e3
    jupiter = Planet(-5.204*Planet.AU, 0, 0, 20, COLOR_JUPITER, 1.898e27); jupiter.y_vel = 13.06e3
    saturn = Planet(-9.573*Planet.AU, 0, 0, 18, COLOR_SATURN, 5.683e26); saturn.y_vel = 9.68e3
    uranus = Planet(-19.165*Planet.AU, 0, 0, 14, COLOR_URANUS, 8.681e25); uranus.y_vel = 6.80e3
    neptune = Planet(-30.178*Planet.AU, 0, 0, 12, COLOR_NEPTUNE, 1.024e26); neptune.y_vel = 5.43e3

    planets = [neptune, uranus, saturn, jupiter, mars, earth, venus, mercury, sun]

    while run:
        clock.tick(60)
        WINDOW.fill(COLOR_UNIVERSE)

        # ----------------- Events -----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_x or event.key == pygame.K_ESCAPE)):
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: pause = not pause
                elif event.key == pygame.K_TAB: show_distance = not show_distance
                elif event.key == pygame.K_CAPSLOCK: draw_line = not draw_line
            elif event.type == pygame.MOUSEBUTTONDOWN:
                last_mouse = list(event.pos)
                if event.button == 1: left_drag = True
                elif event.button == 2: middle_drag = True
                elif event.button == 3: right_drag = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: left_drag = False
                elif event.button == 2: middle_drag = False
                elif event.button == 3: right_drag = False

        mx, my = pygame.mouse.get_pos()
        dx = mx - last_mouse[0]
        dy = my - last_mouse[1]

        # ----------------- Mouse Control -----------------
        if left_drag:
            yaw += dx * rotation_speed
            pitch += dy * rotation_speed
        if middle_drag:
            cam_pos[0] -= dx * pan_speed
            cam_pos[1] += dy * pan_speed
            look_at[0] -= dx * pan_speed
            look_at[1] += dy * pan_speed
        if right_drag:
            cam_pos[2] += dy * zoom_speed

        last_mouse = [mx, my]

        # ----------------- WASD Movement -----------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: cam_pos[1] += move_speed
        if keys[pygame.K_s]: cam_pos[1] -= move_speed
        if keys[pygame.K_a]: cam_pos[0] -= move_speed
        if keys[pygame.K_d]: cam_pos[0] += move_speed

        # ----------------- Update Planets -----------------
        for planet in planets:
            if not pause: planet.update_position(planets)
            planet.draw(WINDOW, show_distance, draw_line)

        # ----------------- HUD -----------------
        fps_text = FONT_1.render(f"FPS: {int(clock.get_fps())}", True, COLOR_WHITE)
        WINDOW.blit(fps_text, (15, 15))
        instructions = [
            "Press X or ESC to exit",
            "Press TAB to toggle distance",
            "Press CAPS LOCK to toggle orbit lines",
            "Use mouse or WASD to move camera",
            "Left drag to rotate",
            "Middle drag to pan",
            "Right drag to zoom",
        ]
        y_off = 45
        for instr in instructions:
            WINDOW.blit(FONT_1.render(instr, True, COLOR_WHITE), (15, y_off))
            y_off += 30

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
