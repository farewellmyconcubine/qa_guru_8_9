import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_find_issue_with_dynamic_allure():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'farewellmyconcubine')
    allure.dynamic.feature('Issues tab')
    allure.dynamic.story('Поиск Issues')
    allure.dynamic.link('https://github.com/', 'tested_site')

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys('farewellmyconcubine/qa_guru_8_9').press_enter()

    with allure.step('Заходим в репозиторий'):
        browser.element(by.link_text('farewellmyconcubine/qa_guru_8_9')).click()

    with allure.step('Открываем табу Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие нужной issue'):
        browser.element(by.partial_text('another test issue')).should(be.visible)