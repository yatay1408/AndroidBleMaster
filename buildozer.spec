[app]
title = BleApp
package.name = bleapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,bleak
orientation = all
fullscreen = 1
android.arch = arm64-v8a, armeabi-v7a, x86_64
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, BLUETOOTH, BLUETOOTH_ADMIN
android.minapi = 21
android.sdk = 30
android.ndk = 21b
