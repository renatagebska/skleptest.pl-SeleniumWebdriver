class Registration:

    # locating and navigating to the Account link
    account_xpath = '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a'

    # registration email
    reg_email_css_selector = 'input#reg_email'

    # registration password
    reg_password_css_selector = 'input#reg_password'

    # registration button
    reg_button_xpath = '//*[@id="customer_login"]/div[2]/form/p[3]/input[3]'
