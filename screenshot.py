def screenshot(url,c_name,extrasleep=False):

    from selenium import webdriver
    from PIL import Image
    from selenium.webdriver.chrome.options import Options
    import time

    #run first time to get scrollHeight
    driver = webdriver.Chrome()
    driver.get(url)
    #pause 3 second to let page load
    time.sleep(3)
    #get scroll Height
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    #     print(height)
    if extrasleep:
        time.sleep(extrasleep)
    #     print(f'height: {height}')
    #close browser
    driver.close()

    #Open another headless browser with height extracted above
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1200,{}".format(height))
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    #pause 3 second to let page loads
    time.sleep(3)
    #save screenshot
    print(driver.get_window_size())
    driver.save_screenshot('sshot_{}.png'.format(c_name))
    driver.close()
    print('done')


url = 'http://www.medium.com'    
screenshot(url,c_name='medium')

