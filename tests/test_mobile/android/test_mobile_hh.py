from selene import be
from selene.support.shared import browser
from allure import step as title


def test_login():
    with title('Type search'):
        browser.element('#fragment_intentions_onboarding_choose_direction_button_new_user').tap()
        browser.element('«По телефону или почте»').tap()
        browser.element('#view_line_input_edit_text').type('email@test.ru')
        browser.element('«Войти по паролю»').tap()
        browser.element('«email@test.ru»').should(be.visible)


def test_check_category():
    with title('Type search'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()
        browser.element('«Избранное»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Избранное"]').should(be.visible)
        browser.element('«Отклики»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Отклики"]').should(be.visible)
        browser.element('«Сообщения»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Сообщения"]').should(be.visible)
        browser.element('«Профиль»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Профиль"]').should(be.visible)


def test_check_notifications():
    with title('Type search'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()
        browser.element('«Профиль»').tap()
        browser.element('//android.widget.ImageView').tap()
        browser.element('«Уведомления»').tap()
        browser.element('«Нет уведомлений»').should(be.visible)


def test_check_vacancies():
    with title('Type search'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()
        browser.element('«Вакансии рядом с вами»').tap()
        browser.element('#permission_deny_and_dont_ask_again_button').tap()
        browser.element('#custom_text_layout_container_item').type('QA')
        browser.element('«QA engineer»').should(be.visible)