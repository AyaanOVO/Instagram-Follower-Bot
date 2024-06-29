from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()

email = "You_email@gmail"
password = "Your_password"

driver.get("https://www.instagram.com/")
time.sleep(3)

email_sign_up = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
email_sign_up.send_keys(email)

password_sign_up = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password_sign_up.send_keys(password)

log_in = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
log_in.send_keys(Keys.ENTER)
time.sleep(10)

not_now = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
not_now.click()

notification_not_now = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notification_not_now.click()
time.sleep(2)

search_bar = driver.find_element(By.LINK_TEXT,"Search")
search_bar.click()
time.sleep(3)

input_search = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/ul/a/div[1]/div/div/div[2]/div/div/div/span')
input_search.click()
time.sleep(5)

follower = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a')
follower.click()
time.sleep(5)

pop_up_window = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a/div/div")))

# Set a flag to track the end of the list
end_of_list = False

while not end_of_list:
    # Find all "Follow" buttons that are currently visible in the pop-up window
    follow_buttons = pop_up_window.find_elements(By.XPATH, "//button[text()='Follow']")

    # Click each "Follow" button
    for button in follow_buttons:
        try:
            button.click()
            time.sleep(1)  # Add a small delay to avoid being flagged as a bot
        except Exception as e:
            print(f"Error clicking follow button: {e}")

    # Scroll the pop-up window to load more followers
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)

    # Wait for the new set of followers to load
    time.sleep(2)

    # Check if we have reached the end of the list
    new_follow_buttons = pop_up_window.find_elements(By.XPATH, "//button[text()='Follow']")
    if len(new_follow_buttons) == len(follow_buttons):
        end_of_list = True

time.sleep(200)