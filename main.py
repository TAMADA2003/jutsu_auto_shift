from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



txt_file_path = 'finde.txt'

# Открываем текстовый файл в режиме чтения
with open(txt_file_path, mode='r', encoding='utf-8') as file:
    # Читаем содержимое файла
    file_contents = file.read()
# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()


# Открываем веб-страницу
driver.get(file_contents)

try:
    while True:
        try:
            # Проверяем, есть ли элемент кнопки на странице
            element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="Нажмите, если лень смотреть опенинг"]'))
            )
            element.click()
        except Exception as e:
            print("1")

        try:
            # Проверяем, есть ли элемент для перехода к следующему эпизоду
            element_last = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="Перейти к следующему эпизоду"][2]'))
            )
            element_last.click()
        except Exception as e:
            print("2")

        try:
            # Проверяем, есть ли элемент для перехода к следующему эпизоду
            element_play = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="Воспроизвести видео"]'))
            )
            element_play.click()
        except Exception as e:
            print("3")

        try:
            # Проверяем, есть ли элемент для перехода к следующему эпизоду
            element_play = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="На весь экран"]'))
            )
            element_play.click()
        except Exception as e:
            print("4")


except KeyboardInterrupt:
    # Если вы прервете выполнение скрипта (например, с помощью Ctrl+C), закроем браузер
    driver.quit()
