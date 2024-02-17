import pygame 
import sys 
import random 
 
pygame.init() 
 
width, height = 800, 600 
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Моя Гра") 
 
background_color = (0, 0, 0)  # Чорний фон 
player_color = (0, 128, 255) 
enemy_color = (255, 0, 0) 
 
player_radius = 20 
enemy_radius = 15 
 
player_x, player_y = width // 2, height // 2 
player_speed = 7 
 
enemy_speed = 3 
base_enemy_speed = enemy_speed 
 
level_duration = 4 
level_timer = level_duration 
current_level = 1 
 
font = pygame.font.Font(None, 36) 
 
enemies = [] 
 
running = True 
clock = pygame.time.Clock() 
 
def create_enemy(): 
    enemy_x = random.randint(enemy_radius, width - enemy_radius) 
    enemy_y = 0 - enemy_radius 
    return enemy_x, enemy_y 
 
def draw_player(x, y): 
    pygame.draw.circle(screen, player_color, (x, y), player_radius) 
 
def draw_enemy(x, y): 
    pygame.draw.circle(screen, enemy_color, (x, y), enemy_radius) 
 
def show_end_screen(level): 
    screen.fill(background_color) 
    end_text = font.render("Гра завершена", True, (255, 0, 0)) 
    level_text = font.render("Завершено на рівні: {}".format(level), True, (255, 255, 255)) 
    screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - end_text.get_height() // 2)) 
    screen.blit(level_text, (width // 2 - level_text.get_width() // 2, height // 2 + 50)) 
    pygame.display.flip() 
    pygame.time.delay(3000) 
 
def animate_game_over(): 
    for i in range(0, 255, 5): 
        screen.fill((i, i, i)) 
        pygame.display.flip() 
        pygame.time.delay(20) 
 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and player_x > player_radius: 
        player_x -= player_speed 
    if keys[pygame.K_RIGHT] and player_x < width - player_radius: 
        player_x += player_speed 
    if keys[pygame.K_UP] and player_y > player_radius: 
        player_y -= player_speed 
    if keys[pygame.K_DOWN] and player_y < height - player_radius: 
        player_y += player_speed 
 
    for i in range(len(enemies)): 
        enemy_x, enemy_y = enemies[i] 
        enemy_y += enemy_speed 
        enemies[i] = (enemy_x, enemy_y) 
 
    if random.random() < 0.02: 
        enemies.append(create_enemy()) 
 
    for enemy in enemies: 
        enemy_x, enemy_y = enemy 
        distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5 
        if distance < player_radius + enemy_radius: 
            print("Гра завершена!") 
            animate_game_over() 
            show_end_screen(current_level) 
            running = False 
 
    screen.fill(background_color) 
    draw_player(player_x, player_y) 
    for enemy in enemies: 
        draw_enemy(enemy[0], enemy[1]) 
 
    # Виведення поточного рівня на екран 
    level_text = font.render("Рівень: {}".format(current_level), True, (255, 255, 255)) 
    screen.blit(level_text, (10, 10)) 
 
    pygame.display.flip() 
 
    # Зменшуємо лічильник часу рівня 
    level_timer -= 1 / 30 
 
    # Перевіряємо, чи закінчився час рівня 
    if level_timer <= 0: 
        # Збільшуємо рівень 
        current_level += 1 
        # Збільшуємо швидкість ворожих об'єктів для наступного рівня 
        enemy_speed *= 1.15 
        # Перезапускаємо лічильник часу рівня 
        level_timer = level_duration 
 
    clock.tick(30) 
 
pygame.quit() 
sys.exit()