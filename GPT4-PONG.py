import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    paddle_width, paddle_height = 15, 80
    ball_size = 15
    paddle_speed = 2
    ball_speed = 1

    paddle1 = pygame.Rect(0, (600 - paddle_height) / 2, paddle_width, paddle_height)
    paddle2 = pygame.Rect(800 - paddle_width, (600 - paddle_height) / 2, paddle_width, paddle_height)
    ball = pygame.Rect((800 - ball_size) / 2, (600 - ball_size) / 2, ball_size, ball_size)

    ball_dx = ball_speed
    ball_dy = ball_speed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_ip(0, -paddle_speed)
        if keys[pygame.K_s]:
            paddle1.move_ip(0, paddle_speed)
        if keys[pygame.K_UP]:
            paddle2.move_ip(0, -paddle_speed)
        if keys[pygame.K_DOWN]:
            paddle2.move_ip(0, paddle_speed)

        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > 600:
            paddle1.bottom = 600
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > 600:
            paddle2.bottom = 600

        ball.move_ip(ball_dx, ball_dy)
        if ball.left < 0 or ball.right > 800:
            ball_dx *= -1
        if ball.top < 0 or ball.bottom > 600:
            ball_dy *= -1

        if paddle1.colliderect(ball):
            ball_dx *= -1
        if paddle2.colliderect(ball):
            ball_dx *= -1

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), paddle1)
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.aaline(screen, (255, 255, 255), (400, 0), (400, 600))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
