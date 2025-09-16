# ===========================================
# - Title:  Solar System Simulation
# - Author: @zerot69 (Updated)
# - Date:   16 Sep 2025
# - Feature: Middle Mouse Drag Zoom
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
pygame.display.set_caption("Solar System Simulation")


class Planet:
    AU = 149.6e6 * 1000  # Astronomical unit
    G = 6.67428e-11  # Gravitational constant
    TIMESTEP = 60 * 60 * 24 * 2  # Seconds in 2 days
    SCALE = 200 / AU

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, window, show, move_x, move_y, draw_line, rotation_angle=0.0):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        # Apply rotation around the sun
        if rotation_angle != 0.0 and not self.sun:
            sx = WIDTH / 2 + move_x
            sy = HEIGHT / 2 + move_y
            dx = x + move_x - sx
            dy = y + move_y - sy
            r = math.hypot(dx, dy)
            theta = math.atan2(dy, dx) + rotation_angle
            x = sx + r * math.cos(theta)
            y = sy + r * math.sin(theta)
        else:
            x = x + move_x
            y = y + move_y
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px, py = point
                px = px * self.SCALE + WIDTH / 2
                py = py * self.SCALE + HEIGHT / 2
                # Apply rotation to orbit points
                if rotation_angle != 0.0 and not self.sun:
                    sx = WIDTH / 2 + move_x
                    sy = HEIGHT / 2 + move_y
                    dx = px + move_x - sx
                    dy = py + move_y - sy
                    r = math.hypot(dx, dy)
                    theta = math.atan2(dy, dx) + rotation_angle
                    px = sx + r * math.cos(theta)
                    py = sy + r * math.sin(theta)
                else:
                    px = px + move_x
                    py = py + move_y
                updated_points.append((px, py))
            if draw_line:
                pygame.draw.lines(window, self.color, False, updated_points, 1)
        pygame.draw.circle(window, self.color, (int(x), int(y)), self.radius)
        if not self.sun:
            distance_text = FONT_2.render(
                f"{round(self.distance_to_sun * 1.057 * 10 ** -16, 8)} light years", True, COLOR_WHITE
            )
            if show:
                window.blit(
                    distance_text,
                    (x - distance_text.get_width() / 2,
                     y - distance_text.get_height() / 2 - 20)
                )

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

    def update_scale(self, scale):
        self.radius *= scale


def main():
    # View rotation variables
    middle_mouse_held = False
    last_mouse_x = 0
    rotation_angle = 0.0
    rotation_speed = 0.005

    # Right mouse drag zoom variables
    right_mouse_held = False
    last_mouse_y = 0
    zoom_speed = 0.005

    run = True
    pause = False
    show_distance = False
    clock = pygame.time.Clock()
    move_x = 0
    move_y = 0
    draw_line = True

    # Metric from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
    sun = Planet(0, 0, 30 * Planet.SCALE * 10 ** 9, COLOR_SUN, 1.98892 * 10 ** 30)
    sun.sun = True

    mercury = Planet(-0.387 * Planet.AU, 0, 5 * Planet.SCALE * 10 ** 9, COLOR_MERCURY, 3.30 * 10 ** 23)
    mercury.y_vel = 47.4 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 9 * Planet.SCALE * 10 ** 9, COLOR_VENUS, 4.8685 * 10 ** 24)
    venus.y_vel = 35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 10 * Planet.SCALE * 10 ** 9, COLOR_EARTH, 5.9722 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 5 * Planet.SCALE * 10 ** 9, COLOR_MARS, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    jupiter = Planet(-5.204 * Planet.AU, 0, 20 * Planet.SCALE * 10 ** 9, COLOR_JUPITER, 1.898 * 10 ** 27)
    jupiter.y_vel = 13.06 * 1000

    saturn = Planet(-9.573 * Planet.AU, 0, 18 * Planet.SCALE * 10 ** 9, COLOR_SATURN, 5.683 * 10 ** 26)
    saturn.y_vel = 9.68 * 1000

    uranus = Planet(-19.165 * Planet.AU, 0, 14 * Planet.SCALE * 10 ** 9, COLOR_URANUS, 8.681 * 10 ** 25)
    uranus.y_vel = 6.80 * 1000

    neptune = Planet(-30.178 * Planet.AU, 0, 12 * Planet.SCALE * 10 ** 9, COLOR_NEPTUNE, 1.024 * 10 ** 26)
    neptune.y_vel = 5.43 * 1000

    planets = [neptune, uranus, saturn, jupiter, mars, earth, venus, mercury, sun]

    while run:
        clock.tick(60)
        WINDOW.fill(COLOR_UNIVERSE)

        for event in pygame.event.get():
            # Middle mouse button pressed/released for rotation
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                middle_mouse_held = True
                last_mouse_x = event.pos[0]
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                middle_mouse_held = False
            # Quit and key events
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                             (event.key == pygame.K_x or event.key == pygame.K_ESCAPE)):
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                show_distance = not show_distance
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                move_x, move_y = -sun.x * sun.SCALE, -sun.y * sun.SCALE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_CAPSLOCK:
                draw_line = not draw_line
            # Right mouse button pressed/released for zoom
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                right_mouse_held = True
                last_mouse_y = event.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                right_mouse_held = False
        # Rotate view while dragging middle mouse
        if middle_mouse_held:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - last_mouse_x
            rotation_angle += dx * rotation_speed
            last_mouse_x = mouse_x

        # Zoom while dragging right mouse
        if 'right_mouse_held' in locals() and right_mouse_held:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dy = mouse_y - last_mouse_y
            zoom_factor = 1 - dy * zoom_speed
            if zoom_factor > 0:
                Planet.SCALE *= zoom_factor
                for planet in planets:
                    planet.update_scale(zoom_factor)
            last_mouse_y = mouse_y

        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        window_w, window_h = pygame.display.get_surface().get_size()
        distance = 10
        if keys[pygame.K_a] or mouse_x == 0:
            move_x += distance
        if keys[pygame.K_d] or mouse_x == window_w - 1:
            move_x -= distance
        if keys[pygame.K_w] or mouse_y == 0:
            move_y += distance
        if keys[pygame.K_s] or mouse_y == window_h - 1:
            move_y -= distance

        for planet in planets:
            if not pause:
                planet.update_position(planets)
            planet.draw(WINDOW, show_distance, move_x, move_y, draw_line, rotation_angle)

        # HUD
        fps_text = FONT_1.render("FPS: " + str(int(clock.get_fps())), True, COLOR_WHITE)
        WINDOW.blit(fps_text, (15, 15))
        instructions = [
            "Press X or ESC to exit",
            "Press TAB to turn on/off distance",
            "Press CAPS LOCK to turn on/off drawing orbit lines",
            "Use mouse or WASD keys to move around",
            "Press C to center",
            "Press Space to pause/unpause",
            "Use right mouse drag (up/down) to zoom",
            "Use middle mouse drag (left/right) to rotate view"
        ]
        y_offset = 45
        for instr in instructions:
            WINDOW.blit(FONT_1.render(instr, True, COLOR_WHITE), (15, y_offset))
            y_offset += 30

        # Planet legends
        legend = [
            ("- Sun", COLOR_SUN),
            ("- Mercury", COLOR_MERCURY),
            ("- Venus", COLOR_VENUS),
            ("- Earth", COLOR_EARTH),
            ("- Mars", COLOR_MARS),
            ("- Jupiter", COLOR_JUPITER),
            ("- Saturn", COLOR_SATURN),
            ("- Uranus", COLOR_URANUS),
            ("- Neptune", COLOR_NEPTUNE),
        ]
        y_offset += 20
        for name, color in legend:
            WINDOW.blit(FONT_1.render(name, True, color), (15, y_offset))
            y_offset += 30

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
