#Special thanks to Bilibili 未来小说家

#特别鸣谢Bilibili未来小说家
# How to display my Bilibili coin count on Runcat Neo
# Part of the code is checked for errors and modified by AI
#Please refer to the content to modify the file

How to obtain your SESSDATA

1. Login to Bilibili: Open and log in to your Bilibili account in the browser.
2. Open developer tools: right-click anywhere on the page and select "Inspect", or press the F12 key directly on the keyboard.
3. Find the "Application" panel:
4. In the menu bar at the top of the developer tool, find and click on the Application tab.
If using Firefox browser, this tag may be called Storage.
6. Find Cookies:
7. In the left menu of the Application panel, expand the Cookies option and click under it https://www.bilibili.com .
8. Copy the value of SESSDATA:
9. In the list on the right, find the row named SESSDATA.
10. Double click the Value column corresponding to the SESSDATA row, select and copy it (a string of characters similar to xxxx% 2Cxxxx).

How to enable scripts to automatically update and synchronize

Open cron task editing: Enter crontab - e in the terminal and press enter. If it is the first time using it, you will be prompted to select the editor, choose Nano (simple) or Vim.
Add a timed command: Enter a line of content in the following format in the editor:
*/20 * * * * /usr/bin/python3 /Users/sunhuiwen/bilibili_coins.py
#*/20 * * * * means it is executed every 20 minutes (you can change it to */10 means it is executed every 10 minutes, but to avoid triggering Bilibili traffic restrictions, it is recommended to run for more than 20 minutes).
#/The URL/bin/python3 is the complete path in Python (you can use the 'which python3' command to view your actual path).
#/Users/sunhuiwen/bilibili_coms.py is the complete path of your script.
Save and exit:
If using nano: press Ctrl+O, enter to confirm, and then press Ctrl+X.
If using Vim: press Esc, enter: wq, enter.
Verify if the addition was successful: Execute crontab - l, and if you see the line just added, it means the task has taken effect.




如何获取你的 SESSDATA

1.登录B站：在浏览器中打开并登录你的 B 站账号。
2.打开开发者工具：在页面任意位置右键点击，选择“检查”(Inspect)，或者直接按键盘上的 F12 键。
3.找到“应用程序” (Application) 面板
4.在开发者工具顶部的菜单栏中，找到并点击 Application (应用程序) 标签。
5.如果使用的是 Firefox 浏览器，这个标签可能叫 Storage (存储)。
6.找到 Cookies
7.在 Application 面板的左侧菜单中，展开 Cookies 选项,然后点击其下的 https://www.bilibili.com。
8.复制 SESSDATA 的值
9.在右侧的列表中，找到名为 SESSDATA 的那一行。
10.双击 SESSDATA 这一行对应的 Value (值) 列，选中并复制它（一串类似 xxxx%2Cxxxx 的字符）。

如何让脚本能够自动更新并同步

打开 cron 任务编辑：在终端输入 crontab -e 并按回车。如果是第一次使用，会提示选择编辑器，选 nano（简单）或 vim 即可。
添加一行定时指令：在编辑器中输入以下格式的一行内容：
*/20 * * * * /usr/bin/python3 /Users/sunhuiwen/bilibili_coins.py
#*/20 * * * * 表示每 20 分钟执行一次（你可以改成 */10 表示每10分钟，但为避免触发B站限流，推荐20分钟以上）。
#/usr/bin/python3 是 Python 的完整路径（可以用 which python3 命令查看你的实际路径）。
#/Users/sunhuiwen/bilibili_coins.py 是你的脚本完整路径。
保存并退出：
如果用 nano：按 Ctrl+O，回车确认，再按 Ctrl+X。
如果用 vim：按 Esc，输入 :wq，回车。
验证是否添加成功：执行 crontab -l，如果看到刚才添加的那一行，说明任务已生效。

