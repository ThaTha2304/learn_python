'''
    Membuat game sederhana dengan pygame
'''

import pygame

# A. Initialize
pygame.init()

# Variable cek game running ato tidak
isRun = True

# B. Membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# C. Object Game
## C.1. Posisi
x = 250
y = 250

## C.2. Ukuran
panjang = 20
lebar = 20

## C.3. Kecepatan Gerak
speed = 10

# Main Program:
while isRun:
    pygame.time.delay(20)

    # D. User Input --> bisa dari keyboard, mouse, database
    for event in pygame.event.get():
        ## D.1. Cek, kalo kita menutup aplikasi, maka program stop
        if event.type == pygame.QUIT:
            isRun = False

    ## D.2. Ambil Semua Keyboard Press
    keys = pygame.key.get_pressed()
    ### D.2.1. Ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    ### D.2.2. Ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    ### D.2.3. Ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    ### D.2.3. Ke bawah
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

    # Game Dynamic
    # E. Update Asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,120,0), (x,y,lebar,panjang))

    # F. Render ke Display
    pygame.display.update()

pygame.quit()
