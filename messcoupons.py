from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from datetime import date, timedelta

# Ask for user input **before** launching Chrome
print("Choose your mess:")
print("1. Vindhya\n2. Nilgiri\n3. K-star\n4. Neelkesh\n5. Shakthi")
choice = input("Enter choice: ")
print("\n")

print("1/2/3\n")
print("Breakfast/Lunch/Dinner\n")
print("Choose your Meal:")
print("1. Breakfast\n2. Lunch\n3. Dinner\n")
choice_meal = input("Enter choice: ")
print("\n")


# Set up Selenium WebDriver (Chrome)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

# Initialize WebDriver **after** taking input
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def loginfunc(username, password):
    driver.get("https://ikollege.iitm.ac.in/iitmhostel/login.do?method=userlogin&loginType=student")  # Replace with your login page URL
    time.sleep(1)
    # Locate login fields and button
    username_field = driver.find_element(By.XPATH, '//*[@id="loginid"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="passwordid"]')
    login_button = driver.find_element(By.XPATH, "/html/body/form/input[3]")

    # Enter login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
# Function to log in
def login(choice, choice_meal):
    
    # Navigate through purchase pages
    driver.get('https://ikollege.iitm.ac.in/iitmhostel/guestCouponOnline.do?method=displayCouponPaymentAdvice')

    time.sleep(1)
    # Select Veg option
    driver.find_element(By.XPATH, '//*[@id="guestCouponFormId"]/div[4]/div[1]/div/div[1]/label').click()

    # Select mess from dropdown
    dropdown = Select(driver.find_element(By.XPATH, '//*[@id="messId"]'))
    
    mess_options = {
        '1': "104",  # Vindhya
        '2': "95",   # Nilgiri
        '3': "102",  # K-star
        '4': "72",   # Neelkesh
        '5': "41"    # Shakthi
    }

    if choice in mess_options:
        dropdown.select_by_value(mess_options[choice])
    else:
        print("Stop being retarded just enter a number from the list.")
        driver.quit()
        return

    # Select next day's date
    next_day = (date.today() + timedelta(days=1)).strftime("%d-%b-%Y")
    print(f"Selecting date: {next_day}")

    date_input = driver.find_element(By.ID, "diningFromCouponId")
    driver.execute_script("arguments[0].value = arguments[1];", date_input, next_day)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)

    
    date_input = driver.find_element(By.ID, "diningToCouponId")
    driver.execute_script("arguments[0].value = arguments[1];", date_input, next_day)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)
    
    



    breakfast = driver.find_element(By.XPATH, '//*[@id="breakfast_0"]')

    lunch = driver.find_element(By.XPATH, '//*[@id="lunch_0"]')
    dinner = driver.find_element(By.XPATH, '//*[@id="dinner_0"]')

    if (choice_meal == '1'):
        breakfast.click()
    elif (choice_meal == '2'):
        lunch.click()
    elif (choice_meal == '3'):
        dinner.click()
    else:
        print("Chutiya ho braindead?")

    #click save
    
    driver.find_element(By.XPATH, '//*[@id="saveId"]').click()
   



# Main execution flow
if __name__ == "__main__":
    # Replace with your credentials
    username = "roll number"
    password = "password ldap"

    # Log in and proceed with the selection
    loginfunc(username, password)
    login(choice, choice_meal)
    # Close the browser
    driver.quit()