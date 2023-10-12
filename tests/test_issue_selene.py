from selene import browser, by, be


def test_find_issue_with_selene():
    browser.open('https://github.com/').element('.search-input').click()
    browser.element('#query-builder-test').send_keys('farewellmyconcubine/qa_guru_8_9').press_enter()
    browser.element(by.link_text('farewellmyconcubine/qa_guru_8_9')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('another test issue')).should(be.visible)
    browser.quit()