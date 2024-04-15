class SortProducts:

    results_name = 'orderby'
    default_sorting_xpath = '//*[@id="page"]/div/div/div[2]/div/form/select/option[1]'
    sort_by_popularity_xpath = '//*[@id="page"]/div/div/div[2]/div/form/select/option[2]'
    sort_by_rating_xpath = '//*[@id="page"]/div/div/div[2]/div/form/select/option[3]'
    sort_by_newness_xpath = '//*[@id="page"]/div/div/div[2]/div/form/select/option[4]'
    sort_by_price_low_xpath = '//*[@id="page"]/div/div/div[2]/div/form/select/option[5]'
    sort_by_price_high_xpath = 'xpath', '//*[@id="page"]/div/div/div[2]/div/form/select/option[6]'
