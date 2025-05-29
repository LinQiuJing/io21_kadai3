#!/usr/bin/env python3
import cgi
import RPi.GPIO as GPIO

# GPIOポート設定
ports = {
    "GR": 13,
    "YL": 19,
    "RD": 26
}

# GPIO初期化
GPIO.setmode(GPIO.BCM)
for p in ports.values():
    GPIO.setup(p, GPIO.OUT)

# 全部消灯
for p in ports.values():
    GPIO.output(p, GPIO.LOW)

# パラメータ取得
form = cgi.FieldStorage()
led = form.getvalue("led")

# 指定されたLEDだけ点灯
if led in ports:
    GPIO.output(ports[led], GPIO.HIGH)

# CGIの戻りページ
print("Content-Type: text/html\n")
print("<html><body>")
print(f"<h1>{led} を点灯しました</h1>")
print('<a href="/index.html">戻る</a>')
print("</body></html>")
