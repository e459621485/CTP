from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import base64

class ScreenShot:
    def __init__(self, url, save_path, device_name=None):
        self.url = url
        self.save_path = save_path
        self.device_name = device_name
        self.driver = None

    def __enter__(self):
        options = Options()
        options.add_argument("--headless")
        if self.device_name:
            options.add_experimental_option('mobileEmulation', {'deviceName': self.device_name})
        self.driver = webdriver.Chrome(options=options)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def capture(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        page_width = self.driver.execute_script("return document.body.scrollWidth")
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        # 直接开启设备模拟，不要再手动开devtools了，否则截图截的是devtools的界面！
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',
                               {'mobile': True, 'width': page_width, 'height': page_height, 'deviceScaleFactor': 1})
        time.sleep(1)
        # 执行截图
        res = self.driver.execute_cdp_cmd('Page.captureScreenshot', {'fromSurface': True})
        time.sleep(0.5)
        # 返回的base64内容写入PNG文件
        with open(self.save_path, 'wb') as f:
            img = base64.b64decode(res['data'])
            f.write(img)