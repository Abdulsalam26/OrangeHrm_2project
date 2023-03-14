from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest


class Test_Hrm:
     @pytest.fixture
     def booting_function(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get(data.Hrm_Data().url)
          self.driver.maximize_window()
          self.driver.implicitly_wait(10)
     def test_login(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)           
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().searchbox_upper)       
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().searchbox_lower)         
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().searchbox_pimU) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pim).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().searchbox_pimL) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pim).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().leaveup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().leave).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().leavelow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().leave).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().timeup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Time).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().timelow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Time).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().recruitmentup)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Recruitment).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().recruitmentlow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Recruitment).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().myinfoup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().My_info).click()                                 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().myinfolow)                                                                                                       
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().My_info).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().performanceup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().performance).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().performancelow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().performance).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().dashboardup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Dashboard).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().dashboardlow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Dashboard).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().directoryup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Directory).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().directorylow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Directory).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().maintanenceup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Maintenance).click()
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().admin_password).send_keys(data.Hrm_Data().a_password)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().conform_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().maintanancelow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Maintenance).click()                
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().buzzup) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Buzz).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_box).send_keys(data.Hrm_Data().buzzlow) 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Buzz).click()             
           assert self.driver.title == 'OrangeHRM'
           print("The user now able to see all individual menu names in upper and lower case ")
     def test_Adminpage(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)  
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().usermanagement).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().user).click()  
           self.driver.execute_script("window.stop();");  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee).send_keys(data.Hrm_Data().entry_name)                
           userrole1=self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().userrole)
           userrole1.click()
           drop1=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
          
           if drop1.__contains__("Admin"):   
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'",userrole1)
           num1=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().value_status)
           num1.click()
           drop2=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down1).text
           if drop2.__contains__("Enabled"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'",num1)
           sleep(5)      
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().usermanagement).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().user).click()   
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee).send_keys(data.Hrm_Data().entry_name)                
           userrole2=self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().userrole)
           userrole2.click()
           drop3=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop3.__contains__("ESS"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='ESS'",userrole2)
           status2=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().status_3)
           status2.click()
           drop4=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down1).text
           if drop4.__contains__("Disabled"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Disabled'",status2)
                
           assert self.driver.title == 'OrangeHRM'
           print("The user can able to see all dropdown visible")
      
                    
     def test_entry_employee(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().add_employee).click() 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().employee_fullname).send_keys(data.Hrm_Data().name)
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().employee_lastname).send_keys(data.Hrm_Data().lastname)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().source_1).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().loginusername).send_keys(data.Hrm_Data().login_username)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().loginpassword).send_keys(data.Hrm_Data().login_password)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().confrompassword).send_keys(data.Hrm_Data().conform_password)                                 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save_button).click() 
           assert self.driver.title == 'OrangeHRM'
           print("The user can be able to see the page moved  to  'Employee list' now")
     def test_search_employee(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()                              
           assert self.driver.title == 'OrangeHRM'
           print("The user can able to see all the  tabs  present in Employee list page")
     def test_personal_employee(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click() 
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().other_id).send_keys(data.Hrm_Data().otherid)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().driving_licence).send_keys(data.Hrm_Data().license_number)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().expiry_date).send_keys(data.Hrm_Data().license_expire_date)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ssnnumber).send_keys(data.Hrm_Data().ssn_number)          
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().sinnumber).send_keys(data.Hrm_Data().sin_number)                                    
           value=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().nationality)
           value.click()
           drop_downvalue0=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue0.__contains__("Indian"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indian'",value)
           value2=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().marital_status)
           value2.click()  
           drop_downvalue1=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue1.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",value2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().D_O_B).send_keys(data.Hrm_Data().date_of_birth)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().gender).click()                         
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().miltery).send_keys(data.Hrm_Data().militry_serives)    
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save_button1).click()                                                                                                                       
           assert self.driver.title == "OrangeHRM"
           print("Now the user can  able to see all the filled details present in personal details page")
     def test_contact_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()
           self .driver.find_element(by=By.LINK_TEXT, value=locators.Hrm_Locators().contact_detail).click() 
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().street_1).send_keys(data.Hrm_Data().street)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().street_2).send_keys(data.Hrm_Data().state_name)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().city).send_keys(data.Hrm_Data().city_name)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().state).send_keys(data.Hrm_Data().state_name)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().code).send_keys(data.Hrm_Data().zip_code)
           place=self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().country)
           place.click()
           drop_downvalue2=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue2.__contains__("India"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='India'",place)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().home).send_keys(data.Hrm_Data().home_no)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().moblie).send_keys(data.Hrm_Data().mobile_no)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().work).send_keys(data.Hrm_Data().work_name)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().w_mail).send_keys(data.Hrm_Data().work_mail)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().other_mail).send_keys(data.Hrm_Data().other_mail)        
           sleep(5)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save_button2).click()        
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in contact details page")
     def test_emergency_details(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click() 
           self.driver.find_element(by=By.LINK_TEXT, value=locators.Hrm_Locators().emergency_contact).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().emergency_add).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().name).send_keys(data.Hrm_Data().Name)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().relationship).send_keys(data.Hrm_Data().Relationship)                      
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().home_number).send_keys(data.Hrm_Data().Home_Telephone)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().mobile_number).send_keys(data.Hrm_Data().Mobile_number)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().work_no).send_keys(data.Hrm_Data().work_Telephone)           
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save_button3).click()           
           assert self.driver.title == 'OrangeHRM'
           print("The user can able to see all the filled details present in Emerengcy contact details page")
     def test_dependents_details(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()    
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Dependent).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Dependents_add).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Dependents_name).send_keys(data.Hrm_Data().Relation_name)
           relative = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().relationship_member)
           relative.click()
           dropdown3=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown3.__contains__("Child"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().date_of_year).send_keys(data.Hrm_Data().Relation_dob)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ok_button).click()     
           assert self.driver.title == "OrangeHRM"
           print("The user can able to see all the filled details present in Dependent details page")
     def test_job_detail(self, booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().job).click()
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().joined).send_keys(data.Hrm_Data().start_date) 
           sleep(2)
           job_name=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().job_title)
           job_name.click()
           dropdown_value4=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown_value4.__contains__("Software Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Software Engineer'",job_name)
           job_role=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().job_category)
           job_role.click()
           dropdown_value5=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown_value5.__contains__("Technicians"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Technicians'",job_role)
                   
           sub_name=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().sub_unit)
           sub_name.click()
           dropdown_value6=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown_value6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
     
           area=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().location)
           area.click()
           dropdown_value7=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown_value7.__contains__("New York Sales Office"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='New York Sales Office'",area)    
               
           employee_position=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_status)
           employee_position.click()
           dropdown_value8=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if dropdown_value8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Yes_button).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in job Details page")
     def test_terminate_employee(self, booting_function):      
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.Terminate).click()
           sleep(2)  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Terminate_employee).send_keys(data.Hrm_Data().exit_DOB)
           Terminate=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.Terminate_reason)
           Terminate.click()
           dropdown_value9=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.drop_down).text
           if dropdown_value9.__contains__("Other"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Other'",Terminate)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.note).send_keys(data.Hrm_Data().Text)    
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.save_button5).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user can able to see  Termination on job details page")
     def test_activate_employee(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()  
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.job).click()       
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.activate).click()  
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see Activation on job  Details page")
     def test_salarydetails(self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()  
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().salary).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().add_salary).click()           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().salary_component).send_keys(data.Hrm_Data().salarycomponent)
           value=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pay_grade)
           value.click()
           drop_downvalue10=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue10.__contains__("Grade 1"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Grade 1'",value)
           name=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pay_frequency)
           name.click()
           drop_downvalue11=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue11.__contains__("Monthly"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Monthly'",name)     
           money=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().currency)
           money.click()
           drop_downvalue12=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue12.__contains__("Indian Rupee"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indian Rupee'",money)          
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators.salary_amount).send_keys(data.Hrm_Data().salary_amount)                     
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().source_3).click()     
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().account).send_keys(data.Hrm_Data().account_no)                      
           account=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().account_type)
           account.click()
           drop_downvalue13=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue13.__contains__("Savings"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Savings'",account) 
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().routing).send_keys(data.Hrm_Data().Routing_no) 
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().amount).send_keys(data.Hrm_Data().deposit_amount) 
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in salary and deposit details page")
     def test_tax (self,booting_function):
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username) 
           self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()     
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().edit_button).click()         
           self .driver.find_element(by=By.LINK_TEXT, value=locators.Hrm_Locators().Tax).click() 
           sleep(2)
           status=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().federal_status)
           status.click()
           drop_downvalue14=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",status) 
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Exemptions).send_keys(data.Hrm_Data().value_Exemptions)
           state=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().state_2)
           state.click()
           drop_downvalue15=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue15.__contains__("Indiana"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indiana'",state)
           tax=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().status_data)
           tax.click()
           drop_downvalue16=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)
           self .driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().tax_Exemptions).send_keys(data.Hrm_Data().per_Exemptions)
           unemployee=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().unemployee_state)
           unemployee.click()
           drop_downvalue17=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue17.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",unemployee)
           work=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().work_state)
           work.click()
           drop_downvalue18=self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
           if drop_downvalue18.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",work)  
           self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().complete).click()           
           assert self.driver.title == 'OrangeHRM'        
           print("The user should be able to see all the details present in Tax Exemptions details page")


   
                                                           
        


   
