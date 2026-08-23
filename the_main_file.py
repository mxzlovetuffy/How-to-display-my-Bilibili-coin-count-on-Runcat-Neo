#you have to change two things,one is the SESSDATA and the other is the UI
#some thing is run with deepseek
#edit by mxz
import os
import requests
import sys
SESSDATA = "you must to change it"
UID = "you must to change it"
OUTPUT_FILE = os.path.expanduser("~/bilibili_coins.json")

if SESSDATA == "you must to change it":
    print("你还没有修改这个脚本的 sessdata 值")
    sys.exit(1)

if UID == "you must to change it":
    print("你还没有修改这个文件的 UID 值，在修改这个文件的UID值时记得去掉双引号！")
    sys.exit(1)

def get_coins():
    url = f"https://api.bilibili.com/x/space/acc/info?mid={UID}"
    headers = {
        "Cookie": f"SESSDATA={SESSDATA}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            data = resp.json()
            if data.get("code") == 0:
                coins = data.get("data", {}).get("coins", 0)

                return float(coins) if coins else 0.0
            else:
                msg = data.get("message", "未知错误")
                if "频繁" in msg:
                    print(f"⚠️ 请求过于频繁，等待5秒... (尝试 {attempt+1}/3)")
                    time.sleep(5)
                    continue
                else:
                    raise Exception(f"API错误: {msg}")
        except Exception as e:
            print(f"⚠️ 请求失败: {e}，等待5秒... (尝试 {attempt+1}/3)")
            time.sleep(5)
            continue
    raise Exception("重试3次均失败")

def main():
    print("🔄 正在获取硬币数...")
    try:
        coins = get_coins()
    except Exception as e:
        print(f"❌ 错误: {e}")
        return

    data = {
        "title": "B站硬币",
        "symbol": "bitcoinsign.circle.fill",
        "metricsBarValue": f"{coins:.1f} 枚",
        "metrics": [
            {
                "title": "当前硬币",
                "formattedValue": f"{coins:.1f} 枚"
            }
        ],
        "lastUpdatedDate": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 更新成功：{coins:.1f} 枚 → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()