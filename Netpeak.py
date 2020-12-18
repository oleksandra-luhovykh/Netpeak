import unittest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\acer\\PycharmProjects\\chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.get("https://netpeak.ua/")
        button_career_xpath = "//li[@class = 'blog']"
        button_career = self.driver.find_element_by_xpath(button_career_xpath)
        try:
            button_career.click()
        except:
            print("Button 'Карьера' is not clickable.")
        button_want_work_xpath = "//*[@class ='btn green-btn']"
        button_want_work = self.driver.find_element_by_xpath(button_want_work_xpath)
        try:
            button_want_work.click()
        except:
            print("Button with text 'Я хочу работать в Netpeak' is not clickable.")

    def test_display_FormatFileMessage(self):
    # Testing the message, about incorrect format of downloaded file, has to be successfully displayed.
        filePath = "C:\\Users\\acer\\Desktop\\mine\\picture.jpg"
        button_downloadFile = self.driver.find_element_by_css_selector("input[type=file]").send_keys(filePath)
        time.sleep(5)
        try:
            formatFile_message = self.driver.find_element_by_id("up_file_name").text
        except NoSuchElementException:
            print("Couldn't find text message of invalid format downloaded file.")
            return False
        assert formatFile_message == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).", \
            "Message of invalid format downloaded file hasn't displayed."
        return True

    def test_TextColor_RequiredFieldsMessage(self):
    # Filling with random data block "3. Personal data".
        field_name = self.driver.find_element_by_id("inputName").send_keys("Роман")
        field_surname = self.driver.find_element_by_id("inputLastname").send_keys("Иванов")
        field_email = self.driver.find_element_by_id("inputEmail").send_keys("RomanIvanov@gmail.com")
        field_phone = self.driver.find_element_by_id("inputPhone").send_keys("+380675849213")
        dropdown_list_year = Select(self.driver.find_element_by_name("by"))
        dropdown_list_year.select_by_value("1999")
        dropdown_list_month = Select(self.driver.find_element_by_name("bm"))
        dropdown_list_month.select_by_value("07")
        dropdown_list_day = Select(self.driver.find_element_by_name("bd"))
        dropdown_list_day.select_by_value("11")
    #Testing that the message text "Все поля являются обязательными для заполнения" is highlighted in red color.
        button_sendCV = self.driver.find_element_by_id("submit")
        try:
            button_sendCV.click()
        except:
            print("Button 'Отправить анкету' is not clickable.")
        error_redMessage_xpath = "//*[@class = 'warning-fields help-block']"
        error_redMessage = self.driver.find_element_by_xpath(error_redMessage_xpath).value_of_css_property("color")
        assert error_redMessage == 'rgba(255, 0, 0, 1)', "Color of error message text is not red."

    def test_load_WebPageCourses(self):
    # Testing the loading of the expected WebPage by clicking button "Курсы"
        button_courses = self.driver.find_element_by_class_name("blog").click()
        assert button_courses == self.driver.get("https://school.netpeak.ua/"), "Expected WebPage hasn't loaded."



    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
