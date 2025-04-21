import pygame
import os

MUSIC_DIR = r"C:\Users\Мадина\PyGame Uni\music"

songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]

if not songs:
    print("Ошибка: В папке 'music' нет mp3-файлов!")
    exit()

# Индекс текущей песни
song_index = 0
is_paused = False  

# Инициализация Pygame и аудиомикшера
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))  

# Загружаем первую песню и автоматически запускаем
pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[song_index]))
pygame.mixer.music.set_volume(1.0) 
pygame.mixer.music.play()

print(f" Музыкальный плеер запущен! Сейчас играет: {songs[song_index]}")
print("Управление: [SPACE] - Play/Pause, [S] - Stop, [→] - Next, [←] - Previous")

# Функции управления музыкой
def play_pause():
    global is_paused
    if pygame.mixer.music.get_busy():  # Если музыка играет, ставим на паузу
        pygame.mixer.music.pause()
        is_paused = True
        print("⏸ Музыка на паузе")
    elif is_paused:  # Если музыка на паузе, продолжаем с того же места
        pygame.mixer.music.unpause()
        is_paused = False
        print("▶ Музыка продолжена")

def stop():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False
    print("⏹ Музыка остановлена")

def next_song():
    global song_index, is_paused
    song_index = (song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[song_index]))
    pygame.mixer.music.play()
    is_paused = False
    print(f"▶ Следующая песня: {songs[song_index]}")

def previous_song():
    global song_index, is_paused
    song_index = (song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[song_index]))
    pygame.mixer.music.play()
    is_paused = False
    print(f"◀ Предыдущая песня: {songs[song_index]}")

# Запускаем игровой цикл
running = True
while running:
    screen.fill((30, 30, 30))  # Фон окна, чтобы видеть, что оно активно
    pygame.display.flip()  # Обновляем экран

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause()  #  Пауза / Продолжение
            elif event.key == pygame.K_s:
                stop()  #  Остановить
            elif event.key == pygame.K_RIGHT:
                next_song()  #  Следующий трек
            elif event.key == pygame.K_LEFT:
                previous_song()  #  Предыдущий трек

pygame.quit()
