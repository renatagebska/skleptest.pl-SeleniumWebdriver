class LoginLocator:

    # locating and navigating to the Account link
    account_xpath = '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a'
    # username
    username_css_selector = 'input#username'
    # password
    password_css_selector = 'input#password'
    # login button
    login_button_xpath = '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]'
    # log_out
    logout_xpath = '//*[@id="post-8"]/div[2]/div/p[1]/a'
    # error message
    error_xpath = '//*[@id="post-8"]/div[2]/ul/li'