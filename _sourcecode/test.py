import pygame
import random

# 초기화
pygame.init()

# 화면 크기 및 색상 정의
WIDTH, HEIGHT = 300, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 블록 크기 정의
BLOCK_SIZE = 30

# 플레이어 블록 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# 게임 초기화
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Tetris")

clock = pygame.time.Clock()

# 블록 생성 함수
def create_block():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    color = random.choice(colors)
    block = Block(color, BLOCK_SIZE, BLOCK_SIZE)
    return block

# 플레이어 블록 초기화
player_block = create_block()
player_block.rect.x = WIDTH // 2 - BLOCK_SIZE
player_block.rect.y = 0

# 중력 변수
gravity = 1

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 블록 이동 및 중력 적용
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_block.rect.x > 0:
        player_block.rect.x -= BLOCK_SIZE
    if keys[pygame.K_RIGHT] and player_block.rect.x < WIDTH - BLOCK_SIZE:
        player_block.rect.x += BLOCK_SIZE

    # 중력 적용
    if player_block.rect.y < HEIGHT - BLOCK_SIZE:
        player_block.rect.y += gravity

    # 새로운 블록 생성
    if player_block.rect.y >= HEIGHT - BLOCK_SIZE:
        player_block = create_block()
        player_block.rect.x = WIDTH // 2 - BLOCK_SIZE
        player_block.rect.y = 0

    # 화면 업데이트
    screen.fill(BLACK)
    screen.blit(player_block.image, player_block.rect)
    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(30)

# 게임 종료
pygame.quit()
