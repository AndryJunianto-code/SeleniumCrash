from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='IDR')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2021-10-23', check_out_date='2021-10-25')
        bot.select_adults(10)
        bot.click_search()
        #bot.apply_filtration()
        bot.report_results()
except Exception as e:
    if 'in PATH' in str(e):
        print('got problem running this from CLI')
    else:
        raise
