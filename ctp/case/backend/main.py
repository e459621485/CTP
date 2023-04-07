from concurrent.futures import ThreadPoolExecutor, as_completed
from .screenShot import ScreenShot
from asgiref.sync import sync_to_async



def get_shot(device):
    with ScreenShot("https://www.moomoo.com", "./shot/{}.png".format(device.replace('/', '_')), device) as s:
        s.capture()
    return device

def run():
    devices = ['iPhone X', 'Galaxy S5', 'Pixel 2',
                        'Pixel 2 XL', 'iPhone 5/SE', 'iPhone 6/7/8',
                        'iPhone 6/7/8 Plus', 'Moto G4']
    # await get_shot(device=devices[0])
    # loop = asyncio.get_event_loop()
    # await loop.run_in_executor(None, get_shot, 'iPhone X')

    executor = ThreadPoolExecutor(max_workers=4)

    all_task = [executor.submit(get_shot, (device)) for device in devices]

    for future in as_completed(all_task):
        data = future.result()
        print("device {} success".format(data))
