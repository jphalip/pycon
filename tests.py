from needle.cases import NeedleTestCase


base_url = 'http://0.0.0.0:8000'


class PyconTests(NeedleTestCase):

    def test_banner(self):
        self.set_viewport_size(1200, 768)
        self.driver.get(base_url)
        self.assertScreenshot('.banner', 'banner')

    def test_banner_responsive(self):
        for w, h in [(1200, 768), (600, 400)]:
            self.set_viewport_size(w, h)
            self.driver.get(base_url)
            self.assertScreenshot('.banner', 'banner-%s-%s' % (w, h))

    def test_menu_desktop(self):
        self.set_viewport_size(1200, 768)
        self.driver.get(base_url)
        self.assertScreenshot('header.main', 'desktop-menu')

        about = self.driver.find_element_by_css_selector('header.main ul.nav li:first-child a')
        about.click()

        self.assertScreenshot('header.main', 'desktop-menu-click')
        self.assertScreenshot('header.main ul.nav li:first-child ul', 'desktop-submenu')

    def test_menu_mobile(self):
        self.set_viewport_size(600, 400)
        self.driver.get(base_url)
        self.assertScreenshot('header.main', 'mobile-menu')

        button = self.driver.find_element_by_css_selector('header.main a.btn-navbar')
        button.click()

        self.assertScreenshot('header.main', 'mobile-submenu')