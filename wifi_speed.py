#To display the downloading and uploading speed
import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())
