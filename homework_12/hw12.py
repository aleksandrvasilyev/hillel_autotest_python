"""
https://rozetka.com.ua/ua/ (юзер не залогинен)

! некоторые элементы появляются в DOM дереве после открытия всплывающих окон, которые открываются после клика по ссылкам

XPATH:
1. //rz-mobile-user-menu/button
2. //a[@class="header__logo"]
3. //button[@id="fat-menu"]
4. //input[@name="search"]
5. //button[contains(@class, 'search-form__microphone')]
6. //button[contains(@class, 'search-form__submit')]
7. //a[@id="rz-banner"]
8. //a[@id="rz-banner"]/span
9. //rz-goods-sections/section[1]//li[2]
10. //h2[text()=" Акционные предложения "]//ancestor::section//li[1]//a[1]
11. //h2[text()=" Горячие новинки "]//ancestor::section//li[2]
12. //*[@class="main-videos"]/li[1]//p
13. //rz-youtube-videos/section/div/a
14. //h2[text()=" Акционные предложения "]//ancestor::section//li[1]//a[1]//parent::div
15. //a[contains(@class, 'main-categories__link')]//parent::li//parent::ul
16. //div[contains(@class, "top-wrap")]/rz-top-slider/ul//a
17. //button[contains(@class, "main-slider__control--next")]
18. //span[@class="main-categories__link-text"]//parent::a//parent::li
19. //button[contains(@class, "form__toggle-password")]
20. //label[@for="remember_me"]
21. //label[@for="remember_me"]//ancestor::div[last()]
22. //button/@_ngcontent-rz-client-c46
23. //h3[text()="Вход"]
24. //*[@class="auth-modal ng-star-inserted"]//child::input[contains(@id, "email")]
25. //button[@class="auth-modal__register-link button button--link ng-star-inserted"]//parent::div
26. //h4[text()="Корзина пуста"]
27. //*[@id="fat-menu"]
28. //*[@id="fat-menu"]//ancestor::rz-header-fat-menu
29. //a[@role='button' and @class='main-categories__link ng-star-inserted']//ancestor::ul
30. //script[@gtm="GTM-N4LDSTX"][1]

CSS:
1. button[id="fat-menu"]
2. rz-cart > button
3. input[name="search"]
4. button[class~="search-form__submit"]
5. rz-user button
6. button[aria-label="Відкрити меню"]
7. rz-sidebar-fat-menu li:nth-child(5) > a
8. rz-main-page-sidebar > a:last-of-type
9. a[class=~"main-slider__link"]
10. img[alt="MasterCard Secure"]
11. div[class~="side-menu__body"] a[class~="socials__link--telegram"]
12. a[class="main-slider__pagination-link"]
13. a[class^="help-zsu"]
14. a[class^="lang__link"]
15. img[class^="top-information__picture"]
"""
