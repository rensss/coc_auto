import os
import sys
import time
import psutil
import random
import platform
import pyautogui
import subprocess
import pywinctl as pwc
from pywinbox import Box, Size, Point, Rect, pointInBox
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

def get_window_rect(window_name):
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in window_list:
        # print(f'---- {window.get("kCGWindowOwnerName", "")}')
        owner_name = window.get("kCGWindowOwnerName", "")
        if owner_name == window_name:
            rect = window.get("kCGWindowBounds", {})
            x, y, width, height = rect["X"], rect["Y"], rect["Width"], rect["Height"]
            rect = x, y, width, height
            return window, rect
    return None

def get_platform():
    return platform.system()

def clear_console():
    current_platform = platform.system()
    
    if current_platform == "Windows":
        os.system("cls")
    elif current_platform == "Darwin" or current_platform == "Linux":
        os.system("clear")
    else:
        print("Unsupported platform. Unable to clear console.")

def get_app_window_by_name(app_name):
    try:
        # windows = pwc.getAllWindows()
        # for window in windows:
        #     print(f"---- {window}")
        app_window = pwc.getWindowsWithTitle(app_name)[0]
        return app_window
    except Exception as e:
        print(f"Error finding {app_name} window: {e}")

def get_position_with_picture_name(name, confidence = 0.9):
    # 使用PyAutoGUI库查找应用程序窗口位置
    try:
        position = pyautogui.locateOnScreen(name, grayscale=True, confidence=confidence)
        return position
    except Exception as e:
        print(f"Error finding rect: {name}: -- {e}")
        return None

def get_app_window_position(rect):
    # 获取应用程序窗口的屏幕区域
    x, y = rect.left, rect.top
    width, height = rect.right-rect.left, rect.bottom-rect.top  # 替换为你想要截取的宽度和高度
    screen_capture_command = ["screencapture", "-R", f"{x},{y},{x+width},{y+height}", "screenshot.png"]

    # 使用命令行工具"screencapture"获取屏幕截图
    subprocess.run(screen_capture_command)

    # 使用PyAutoGUI库查找应用程序窗口位置
    try:
        app_position = pyautogui.locateOnScreen("screenshot.png", grayscale=True, confidence=0.9)
        return app_position
    except Exception as e:
        print(f"Error finding rect: {rect}: -- {e}")
        return None

def cd_to_script_directory():
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)

    # 获取当前脚本所在的目录
    script_directory = os.path.dirname(script_path)

    # 切换到脚本所在的目录
    os.chdir(script_directory)

    # 在目录切换后输出当前工作目录
    print(f"Current working directory: {os.getcwd()}")

def simulate_click(x, y):
    print(f'---- x:{x} y:{y}')
    # 模拟点击屏幕上的坐标
    pyautogui.click(x, y)

if __name__ == "__main__":
    # 清空
    clear_console()

    # 切换到工作路径
    cd_to_script_directory()

    # 获取当前操作系统平台
    current_platform = get_platform()

    sourceImagePath = './SourceImage'

    if current_platform == "Darwin":
        print(f"Running on macOS")
    elif current_platform == "Windows":
        print(f"Running on Windows")
    else:
        print(f"Running on {current_platform}")

    app_name = "安卓"  # 替换为目标应用的名称
    # app_position = get_app_window_position(app_name)
    # print(f"---- app_position: {app_position}")

    window_name = "MuMu安卓设备"
    mumu_window, window_rect = get_window_rect(window_name)

    if window_rect:
        print(f"{window_name} window rect: {window_rect}")
    else:
        print(f"{window_name} window not found.")

    mumu_name = "MuMu安卓设备"
    window = get_app_window_by_name(app_name)
    print(f"---- window: {window}")
    window.activate()
    print(f'---- window.isActive {window.isActive}')

    # print(f'---- mumu_window:{mumu_window}')
    fixRect = Rect(window_rect[0], window_rect[1], window_rect[0]+window_rect[2], window_rect[1]+window_rect[3])
    print(f'---- mumu_window:{fixRect}')
    position = get_app_window_position(fixRect)
    print(f'---- position {position}')


    # rect = window.getClientFrame()
    # print(f'---- rect {rect}')

    # # rect = rect.right, rect.top + 10, rect.left - 58, rect.bottom - 86 

    # fixRect = Rect(rect.left*2, rect.top*2, rect.right*2, rect.bottom*2)

    # position = get_app_window_position(rect)
    # print(f'---- position {position}')
    # # pyautogui.click(0, 0)

    # main_app_name = 'app.png'
    # main_app_image_path = sourceImagePath + '/' + main_app_name
    # app_position = get_position_with_picture_name(main_app_image_path)
    # print(f'---- app_position {app_position}')

    # if app_position:
    #     # 模拟点击窗口中的某个位置，替换为你想要点击的坐标
    #     target_x, target_y = app_position[0]/2.0 + 30, app_position[1]/2.0 + 50
    #     simulate_click(target_x, target_y)
    # else:
    #     print(f"{app_position} not found.")
