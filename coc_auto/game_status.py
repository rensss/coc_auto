# 定义操作类
class SimulatorHomeAction:
    def perform_action(self):
        print("Perform action for simulator home.")

class GameHomeAction:
    def perform_action(self):
        print("Perform action for game home.")

class SplashAdAction:
    def perform_action(self):
        print("Handle splash ad.")

class PlayerInfoAction:
    def perform_action(self):
        print("View player information.")

class MailboxAction:
    def perform_action(self):
        print("Check mailbox.")

class GroupChatAction:
    def perform_action(self):
        print("Participate in group chat.")

class NewMessagesAction:
    def perform_action(self):
        print("Read new messages.")

class DonationRequestsAction:
    def perform_action(self):
        print("Handle donation requests.")

class GameStatus:
    def __init__(self):
        self.simulator_home = False
        self.game_home = False
        self.splash_ad = False
        self.player_info = False
        self.mailbox = False
        self.group_chat_open = False
        self.new_messages = False
        self.donation_requests = False

    def set_simulator_home(self, value):
        self.simulator_home = value
        self.handle_state_change()

    def set_game_home(self, value):
        self.game_home = value
        self.handle_state_change()

    def set_splash_ad(self, value):
        self.splash_ad = value
        self.handle_state_change()

    def set_player_info(self, value):
        self.player_info = value
        self.handle_state_change()

    def set_mailbox(self, value):
        self.mailbox = value
        self.handle_state_change()

    def set_group_chat_open(self, value):
        self.group_chat_open = value
        self.handle_state_change()

    def set_new_messages(self, value):
        self.new_messages = value
        self.handle_state_change()

    def set_donation_requests(self, value):
        self.donation_requests = value
        self.handle_state_change()

    def handle_state_change(self):
        # 在这里根据状态的改变创建相应的操作类对象并执行
        if self.simulator_home:
            action = SimulatorHomeAction()
            action.perform_action()

        if self.game_home:
            action = GameHomeAction()
            action.perform_action()

        if self.splash_ad:
            action = SplashAdAction()
            action.perform_action()

        if self.player_info:
            action = PlayerInfoAction()
            action.perform_action()

        if self.mailbox:
            action = MailboxAction()
            action.perform_action()

        if self.group_chat_open:
            action = GroupChatAction()
            action.perform_action()

        if self.new_messages:
            action = NewMessagesAction()
            action.perform_action()

        if self.donation_requests:
            action = DonationRequestsAction()
            action.perform_action()

# 创建游戏状态对象
current_game_status = GameStatus()

# 改变状态并触发对应操作
current_game_status.set_simulator_home(True)
current_game_status.set_game_home(True)
current_game_status.set_splash_ad(True)
current_game_status.set_player_info(True)
current_game_status.set_mailbox(True)
current_game_status.set_group_chat_open(False)
current_game_status.set_new_messages(True)
current_game_status.set_donation_requests(True)
