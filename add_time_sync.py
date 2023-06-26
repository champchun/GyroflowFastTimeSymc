# %%
import json
import glob
filenames = glob.glob("*.gyroflow")

with open(f'./YourTimeSync.json', 'r') as f:
    # 讀取 JSON 檔案內容
    your_time_sync = json.load(f)

for fn in filenames:
    # 開啟 JSON 檔案
    with open(f'{fn}', 'r') as f:
        # 讀取 JSON 檔案內容
        data = json.load(f)

    # 輸出 JSON 檔案內容
    print(f'{fn}')
    data["offsets"] = {"100": your_time_sync["your_time_sync"]}
    
    with open(f'{fn[0:-9]}_add_time_sync.gyroflow', 'w') as f:
        json.dump(data, f)


# %%
