def screenshot(url,c_name,extrasleep=False):

    from selenium import webdriver
    from PIL import Image
    from selenium.webdriver.chrome.options import Options
    import time
    from pathlib import Path

    #run first time to get scrollHeight
    driver = webdriver.Chrome()
    driver.get(url)

    #pause 3 second to let page load
    time.sleep(3)
    
    #get scroll Height
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
   
   # if internet connection is too slow, then add more seconds
    if extrasleep:
        time.sleep(extrasleep)

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

    #print window size
    print(driver.get_window_size())

    # save to output folder using relative path. "python/output" should exist
    data_folder =  Path(Path.cwd(),"python/output")
    filename = 'sshot_{}.png'.format(c_name)
    savepath = '{}\{}'.format(data_folder,filename)
    driver.save_screenshot(savepath)
    
    # close web browser
    driver.close()

    # print confirmation
    print('done')


url = 'http://www.medium.com'    
screenshot(url,c_name='medium2')

