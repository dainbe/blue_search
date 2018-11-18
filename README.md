# blue_search

## Bluetoothを使った存在検知
### search.py
ペアリング状態のデバイスのBDアドレスをdev_list.jsonの保存します。
user_nameはunknownで書き込まれるので変更してください。

```python:search.py
[
  {
    'user_name': 'unknown',
    'addr': AB:CD:EF:01:23:45'
  }
]
```
の形で保存されます。

### scan.py
search.pyで得たBDアドレスから存在を検知します。
ループ1回につき差分をとることで入室と退出の判断をしています。
POSTすることを考えいろいろしてあります。
