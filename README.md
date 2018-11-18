<h1>blue_search</h1>
  
Bluetoothを使った存在検知
<h3>search.py</h3>
ペアリング状態のデバイスのBDアドレスをdev_list.jsonの保存します。
user_nameはunknownで書き込まれるので変更してください。

```
[
  {
    'user_name': 'unknown',
    'addr': AB:CD:EF:01:23:45'
  }
]
```
の形で保存されます。

<h3>scan.py</h3>
search.pyで得たBDアドレスから存在を検知します。
ループ1回につき差分をとることで入室と退出の判断をしています。
POSTすることを考えいろいろしてあります。
