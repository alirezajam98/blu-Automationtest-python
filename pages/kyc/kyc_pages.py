import time
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from conftest import driver
from pages.base_page import BasePage


class NotificationPermissionPage(BasePage):
    """کلاس مربوط به اجازه دسترسی به نوتیفیکیشن"""

    def allow_notification_permission(self):
        """اجازه دسترسی به نوتیفیکیشن (اگر مجوز درخواست شد)"""
        try:
            allow_button = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id"
                                                             "/permission_allow_button"))
            )
            allow_button.click()
        except TimeoutException:
            # اگر صفحه مجوز نمایش داده نشود، ادامه دهید
            pass

    def allow_camera_permission(self):
        """اجازه دسترسی به دوربین (اگر مجوز درخواست شد)"""
        try:
            allow_button = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id"
                                                             "/permission_allow_foreground_only_button"))
            )
            allow_button.click()
        except TimeoutException:
            # اگر صفحه مجوز نمایش داده نشود، ادامه دهید
            pass


class CreateAccountPage(BasePage):
    """کلاس مربوط به صفحه ایجاد حساب کاربری"""

    def click_create_account(self):
        """کلیک روی دکمه ایجاد حساب کاربری"""
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
        )
        create_account_button.click()
        create_account_button.get_attribute("text")


class OpenAccountPage(BasePage):
    """کلاس مربوط به صفحه باز کردن حساب"""

    def click_open_account(self):
        """کلیک روی دکمه باز کردن حساب"""
        open_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openAccountButton"))
        )
        open_account_button.click()

    def get_open_account_text(self):
        """کلیک روی دکمه باز کردن حساب"""
        open_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openAccountButton"))
        )
        return open_account_button.get_attribute("text")


class SelectServerPage(BasePage):
    """کلاس مربوط به صفحه انتخاب سرور"""

    def select_uat_server(self):
        """انتخاب سرور 'UAT'"""
        uat_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className('
                                                                          '"android.view.ViewGroup").instance(3)'))
        )
        uat_button.click()


class CreateAccountInfoPage(BasePage):
    """کلاس مربوط به صفحه اطلاعات حساب کاربری"""

    def click_start(self):
        """کلیک روی دکمه شروع"""
        start_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        start_button.click()

    def get_account_info_page_title(self):
        info_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("در فرایند بازکردن حساب در بلو به '
                                               'موارد زیر نیاز خواهید داشت:")'))
        )
        return info_page_title.get_attribute("text")

    def get_clock_text_title(self):
        clock_text_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("۷ دقیقه زمان!")'))
        )
        return clock_text_title.get_attribute("text")

    def get_clock_text_subtitle(self):
        clock_text_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("کمتر از ۷ دقیقه زمان نیاز دارید")'))
        )
        return clock_text_subtitle.get_attribute("text")

    def get_sim_text_title(self):
        sim_text_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("سیم‌کارت به‌نام")'))
        )
        return sim_text_title.get_attribute("text")

    def get_sim_text_subtitle(self):
        sim_text_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("فعال و به نام خودتان باشد")'))
        )
        return sim_text_subtitle.get_attribute("text")

    def get_identification_documents_text_title(self):
        identification_documents_text_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اصل مدرک هویتی")'))
        )
        return identification_documents_text_title.get_attribute("text")

    def get_identification_documents_text_subtitle(self):
        get_identification_documents_text_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("[ کارت ملی هوشمند ] یا [ کد رهگیری + شناسنامه ]")'))
        )
        return get_identification_documents_text_subtitle.get_attribute("text")

    def get_video_text_title(self):
        video_text_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ویدیو سلفی")'))
        )
        return video_text_title.get_attribute("text")

    def get_video_text_subtitle(self):
        video_text_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("کوتاه و با متن مشخص‌شده از شما ضبط خواهد شد")'))
        )
        return video_text_title.get_attribute("text")

    def get_start_button_text(self):
        start_button_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        return start_button_text.get_attribute("text")


class AcceptRulesAndRegulationsPage(BasePage):
    """کلاس مربوط به قبول قوانین و مقررات"""

    def get_accept_rule_page_title(self):
        title_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بازکردن حساب در بلو")'))
        )
        return title_text.get_attribute("text")

    def get_accept_rule_page_subtitle(self):
        subtitle_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("تکمیل مراحل زیر، فقط چند دقیقه زمان نیاز دارد")'))
        )
        return subtitle_text.get_attribute("text")

    def get_create_account_step_title(self):
        create_account_step_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ساخت حساب کاربری")'))
        )
        return create_account_step_title.get_attribute("text")

    def get_create_account_step_subtitle(self):
        create_account_step_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("در این مرحله اطلاعات خودتان را وارد می‌کنید و '
                    'رمز عبور انتخاب می‌کنید.")'))
        )
        return create_account_step_subtitle.get_attribute("text")

    def get_documents_scan_step_title(self):
        documents_scan_step_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("اسکن مدارک شما")'))
        )
        return documents_scan_step_title.get_attribute("text")

    def get_identification_step_title(self):
        identification_step_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("شناسایی هویت شما")'))
        )
        return identification_step_title.get_attribute("text")

    def get_identification_step_subtitle(self):
        identification_step_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("این مرحله شامل انتخاب شغل و ارسال ویدیو از خودتان می‌باشد.")'))
        )
        return identification_step_subtitle.get_attribute("text")

    def get_check_information_step_title(self):
        check_information_step_titl = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("بررسی اطلاعات شما توسط بلو")'))
        )
        return check_information_step_titl.get_attribute("text")

    def get_card_order_step_title(self):
        card_order_step_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("سفارش رایگان بلوکارت")'))
        )
        return card_order_step_title.get_attribute("text")

    def get_rules_and_regulations_title(self):
        rules_and_regulations_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("قوانین و شرایط را خواندم و قبول می‌کنم")'))
        )
        return rules_and_regulations_title.get_attribute("text")

    def get_confirm_button_title(self):
        confirm_button_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.samanpr.blu.dev:id/confirm")'))
        )
        return confirm_button_title.get_attribute("text")

    def click_rules_and_regulations(self):
        """کلیک روی سوییچ قوانین و مقررات"""
        accept_switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.Switch'))
        )
        accept_switch.click()

    def click_confirm_button(self):
        """کلیک روی دکمه تایید"""
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        confirm_button.click()
        return EnterPhoneNumberPage(self.driver)

    def is_switch_on(self):
        """بررسی اینکه سوییچ قوانین روشن است یا خاموش"""
        accept_switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.Switch'))
        )
        switch_status = accept_switch.get_attribute("checked")
        return switch_status == "true"  # اگر true باشد یعنی سوییچ روشن است

    def toggle_switch(self):
        """تغییر وضعیت سوییچ قوانین و مقررات"""
        current_status = self.is_switch_on()
        self.click_rules_and_regulations()  # تغییر وضعیت سوییچ
        new_status = not current_status  # وضعیت جدید باید معکوس شود
        return new_status


class EnterPhoneNumberPage(BasePage):
    """کلاس مربوط به وارد کردن شماره تلفن"""

    def enter_phone_number(self, phone_number):
        """وارد کردن شماره تلفن"""
        phone_number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/phoneInputEditText"))
        )
        phone_number_field.send_keys(phone_number)

    def get_phone_number_page_header(self):
        phone_number_page_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("ساخت حساب کاربری")'))
        )
        return phone_number_page_header.get_attribute("text")

    def get_phone_number_page_title(self):
        phone_number_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.samanpr.blu.dev:id/titleTextView")'))
        )
        return phone_number_page_title.get_attribute("text")

    def get_phone_number_field_text(self):
        phone_number_field_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.samanpr.blu.dev:id/phoneInputEditText")'))
        )
        return phone_number_field_text.get_attribute("text")

    def get_phone_number_page_subtitle(self):
        phone_number_page_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.samanpr.blu.dev:id/guideTextView")'))
        )
        return phone_number_page_subtitle.get_attribute("text")

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class ReferralPage(BasePage):
    """کلاس مربوط به صفحه وارد کردن کد ریفرال"""

    def get_referral_page_title(self):
        """دریافت متن فیلد ریفرال"""
        referral_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))
        )
        return referral_page_title.get_attribute("text")

    def get_referral_field_text(self):
        """دریافت متن فیلد ریفرال"""
        referral_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/referralInputEditText"))
        )
        return referral_field.get_attribute("text")

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class NationalCodePage(BasePage):
    """کلاس مربوط به وارد کردن کد ملی"""

    def enter_national_code(self, national_code):
        """وارد کردن کد ملی"""
        national_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        national_code_field.send_keys(national_code)

    def get_national_code_text(self):
        """دریافت متن فیلد کد ملی"""
        national_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nationalCodeInputEditText"))
        )
        return national_code_field.get_attribute("text")

    def get_national_code_title(self):
        """دریافت متن فیلد کد ملی"""
        national_code_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/titleTextView")'))
        )
        return national_code_title.get_attribute("text")

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class BirthDatePage(BasePage):
    """کلاس مربوط به تنظیم تاریخ تولد"""

    def get_birth_day_page_title(self):
        """دریافت متن فیلد کد ملی"""
        birth_day_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/pageTitle")'))
        )
        return birth_day_page_title.get_attribute("text")

    def get_birth_day_empty_field_text(self):
        """دریافت متن فیلد کد ملی"""
        birth_day_empty_field_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/birthdateInputEditText")'))
        )
        return birth_day_empty_field_text.get_attribute("text")

    def scroll_year(self):
        """اسکرول کردن سال با استفاده از ActionChains با مختصات نسبی"""
        window_size = self.driver.get_window_size()  # دریافت اندازه صفحه
        start_x = window_size['width'] * 0.5  # 50% عرض صفحه
        start_y = window_size['height'] * 0.7  # 80% ارتفاع صفحه (مختصات شروع)
        end_y = window_size['height'] * 0.8  # 20% ارتفاع صفحه (مختصات پایان)

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)  # حرکت به مختصات شروع
        actions.w3c_actions.pointer_action.pointer_down()  # کلیک و نگه‌داشتن
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)  # حرکت به مختصات پایان
        actions.w3c_actions.pointer_action.release()  # رها کردن کلیک
        actions.perform()

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class UserNamePage(BasePage):
    """کلاس مربوط به وارد کردن نام کاربری"""

    def get_username_page_title(self):
        username_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/titleTextView")'))
        )
        return username_page_title.get_attribute("text")

    def get_username_field_text(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().resourceId('
                                            '"com.samanpr.blu.dev:id/usernameInputEditText")'
                                            ))
        )
        return username_field.get_attribute("text")

    def enter_username(self, username):
        """وارد کردن نام کاربری"""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/usernameInputEditText"))
        )
        username_field.send_keys(username)
        return username_field.get_attribute("text")

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class PasswordPage(BasePage):
    """کلاس مربوط به وارد کردن رمز عبور"""

    def get_password_page_title(self):
        password_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/titleTextView")'))
        )
        return password_page_title.get_attribute("text")

    def get_password_page_field_text(self):
        password_page_field_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/textInputEditText")'))
        )
        return password_page_field_text.get_attribute("text")

    def get_password_condition_lowercase_and_uppercase(self):
        password_condition_lowercase_and_uppercase = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شامل حروف کوچک و بزرگ انگلیسی")'))
        )
        return password_condition_lowercase_and_uppercase.get_attribute("text")

    def get_password_condition_minimum_characters(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شامل حداقل ۸ کاراکتر")'))
        )
        return username_field.get_attribute("text")

    def get_password_condition_number(self):
        password_condition_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شامل عدد")'))
        )
        return password_condition_number.get_attribute("text")

    def get_password_page_subtitle(self):
        password_page_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                                          '"com.samanpr.blu.dev:id/guideTextView")'))
        )
        return password_page_subtitle.get_attribute("text")

    def enter_password(self, password):
        """وارد کردن رمز عبور"""
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/textInputEditText"))
        )
        password_field.send_keys(password)

    def click_next_button(self):
        """کلیک روی دکمه بعدی"""
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class CreateAccountInBluStatePage(BasePage):
    """کلاس مربوط به تایید ایجاد حساب در بلو استیت"""

    def get_documents_scan_step_subtitle(self):
        documents_scan_step_subtitle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("در این مرحله به '
                                                                          'کارت ملی یا کد رهگیری و شناسنامه نیاز '
                                                                          'دارید.")'))
        )
        return documents_scan_step_subtitle.get_attribute("text")

    def click_confirm_button(self):
        """کلیک روی دکمه تایید"""
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        confirm_button.click()


class SelectNationalCardOrTrackerIdPage(BasePage):
    """کلاس مربوط به انتخاب کارت ملی یا شناسه پیگیری"""

    def get_select_document_method_title(self):
        select_document_method_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.samanpr.blu.dev:id/titleTextView")'))
        )
        return select_document_method_title.get_attribute("text")

    def get_i_have_national_card(self):
        select_document_method_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("com.samanpr.blu.dev:id/nationalCardButton")'))
        )
        return select_document_method_title.get_attribute("text")

    def get_i_have_birth_certificate(self):
        select_document_method_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.samanpr.blu.dev:id/trackerIdButton")'))
        )
        return select_document_method_title.get_attribute("text")

    def click_select_national_card(self):
        """کلیک روی گزینه انتخاب کارت ملی"""
        national_card = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nationalCardButton"))
        )
        national_card.click()

    def click_birth_certificate(self):
        """کلیک روی گزینه انتخاب شناسه پیگیری"""
        tracker_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/trackerIdButton"))
        )
        tracker_id.click()


class TrakingCodePage(BasePage):
    """صفحه کدپیگیری شناسنامه"""

    def enter_tracing_code(self, national_code):
        tracing_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        tracing_code_field.send_keys(national_code)

    def get_tracing_code_text(self):
        tracing_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nationalCodeInputEditText"))
        )
        return tracing_code_field.get_attribute("text")

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()
class SelectTypeBirthCertificatePage(BasePage):
    """کلاس مربوط به انتخاب کارت ملی یا شناسه پیگیری"""
    def click_birth_certificate_new(self):
        """کلیک روی گزینه انتخاب کارت ملی"""
        birth_certificate_new = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nationalCardButton"))
        )
        birth_certificate_new.click()

    def click_birth_certificate_old(self):
        """کلیک روی گزینه انتخاب شناسه پیگیری"""
        birth_certificate_old = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/trackerIdButton"))
        )
        birth_certificate_old.click()

class TakePhotoPage(BasePage):
    """کلاس مربوط به گرفتن عکس"""

    def get_edit_photo_button_text(self):
        edit_photo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("com.samanpr.blu.dev:id/pageTitleTextView")'))
        )
        return edit_photo.get_attribute("text")

    def get_select_from_gallery(self):
        select_from_gallery = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/normalGalleryButton"))
        )
        select_from_gallery.get_attribute("text")

    def click_select_from_gallery(self):
        select_from_gallery = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/normalGalleryButton"))
        )
        select_from_gallery.click()

    def click_select_from_gallery_circle_button(self):
        select_from_gallery = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/circleGalleryButton"))
        )
        select_from_gallery.click()

    def click_take_photo(self):
        """کلیک روی دکمه عکس گرفتن"""
        take_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/takePhotoButton"))
        )
        take_photo.click()


class GalleryPage(BasePage):
    def click_first_photo(self):
        """کلیک روی دکمه عکس گرفتن"""
        first_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'))
        )
        first_photo.click()

    def click_second_photo(self):
        """کلیک روی دکمه عکس گرفتن"""
        first_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(1)'))
        )
        first_photo.click()

    def click_third_photo(self):
        """کلیک روی دکمه عکس گرفتن"""
        first_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(2)'))
        )
        first_photo.click()

    def click_fourth_photo(self):
        """کلیک روی دکمه عکس گرفتن"""
        first_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(3)'))
        )
        first_photo.click()

    def click_album_button(self):
        """کلیک روی دکمه عکس گرفتن"""
        album_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Albums")'))
        )
        album_button.click()

    def click_favorite_album(self):
        """کلیک روی دکمه عکس گرفتن"""
        favorite_album = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.LinearLayout").instance(3)'))
        )
        favorite_album.click()


class EditPhotoPage(BasePage):
    def click_confirm_button(self):
        """کلیک روی دکمه عکس گرفتن"""
        confirm_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().resourceId("com.samanpr.blu.dev:id/continueButton")'))
        )
        confirm_button.click()


class ConfirmPhotoPage(BasePage):
    """کلاس مربوط به تایید عکس"""

    def click_confirm_photo(self):
        """کلیک روی دکمه تایید عکس"""
        confirm_photo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmSendButton"))
        )
        confirm_photo.click()
        return ConfirmPhotoModal

    def click_edit_again_photo(self):
        edit_again_photo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmSendButton"))
        )
        edit_again_photo.click()


class ConfirmPhotoModal(BasePage):
    """کلاس مربوط به تایید عکس در مودال"""

    def click_confirm_photo(self):
        """کلیک روی دکمه تایید در مودال"""
        confirm_photo_modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmAndSendBtn"))
        )
        confirm_photo_modal.click()


class UploadPhotoModal(BasePage):
    """کلاس مربوط به آپلود عکس"""

    def click_upload_photo(self):
        """کلیک روی دکمه آپلود عکس"""
        upload_photo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmAndSendBtn"))
        )
        upload_photo.click()


class SelectJobPage(BasePage):
    """کلاس مربوط به انتخاب شغل"""

    def select_job(self):
        """انتخاب اولین شغل از لیست"""
        select_job = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("‏طراح و تحلیلگر علمی / فنی / پژوهشگر")'))
        )
        select_job.click()

    def click_confirm_job(self):
        """کلیک روی دکمه تایید شغل"""
        confirm_job = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))
        )
        confirm_job.click()


class VideoDemoPage(BasePage):
    """کلاس مربوط به نمایش ویدیو آموزشی"""

    def click_confirm_video_demo(self):
        """کلیک روی دکمه تایید ویدیو"""
        button_locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/continueButton")
        WebDriverWait(self.driver, 30).until(
            lambda driver: self.driver.find_element(*button_locator).is_enabled()
        )
        self.driver.find_element(*button_locator).click()


class VideoRecordingPage(BasePage):
    """کلاس مربوط به ضبط ویدیو"""

    def click_video_recording(self):
        """کلیک روی دکمه ضبط ویدیو"""
        record_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/recordButton"))
        )
        record_button.click()

    def click_stop_recording_button(self):
        """کلیک روی دکمه توقف ضبط"""
        stop_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/recordButton"))
        )
        stop_button.click()

    def click_upload_video(self):
        """کلیک روی دکمه آپلود ویدیو"""
        upload_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/uploadButton"))
        )
        upload_button.click()


class ConfirmVideoModal(BasePage):
    """کلاس مربوط به تایید آپلود ویدیو"""

    def click_confirm_video(self):
        """کلیک روی دکمه تایید آپلود ویدیو"""
        confirm_video = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmAndSendBtn"))
        )
        confirm_video.click()


class FinalPage(BasePage):
    """کلاس مربوط به تایید نهایی"""

    def click_final_confirm(self):
        """کلیک روی دکمه تایید نهایی"""
        confirm_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))
        )
        confirm_button.click()


class CreateAccountConfirmPage(BasePage):
    def enter_to_blu_button(self):
        """کلیک روی دکمه تایید نهایی"""
        click_enter_to_blu_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
        )
        click_enter_to_blu_button.click()
