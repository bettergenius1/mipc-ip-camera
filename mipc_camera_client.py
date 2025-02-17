camera_ip = "192.168.1.197"
camera_user = "1jfiegbqo356a"
camera_password = "turbo54"

from mipc_camera_client import MipcCameraClient

c = MipcCameraClient(camera_ip)
c.login(camera_user, camera_password)
jpeg_data = c.get_image()
with open("hello.jpg", mode="wb") as file:
    file.write(jpeg_data)