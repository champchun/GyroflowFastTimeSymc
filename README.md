# GyroflowFastTimeSymc
Applicable for GyroFlow version: `1.5.0`
# 使用方式
If you are using the same device for gyro calibration, the time difference should be the same. Therefore, after performing the initial calibration, record the current time difference and fill it in the `YourTimeSync.json` file.

![](./Figure/Screenshot_8.png)
After exporting the `.gyroflow file`, run `add_time_sync.py`.

![](./Figure/Screenshot_1.png)

Drag and drop the output `*._add_time_sync.gyroflow` file into GyroFlow.
![](./Figure/Screenshot_2.png)