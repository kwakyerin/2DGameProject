from pico2d import load_image

class Blue:
    def __init__(self):
        self.Idle_image=load_image('Blue/Blue_Idle.png')
        self.Run_image=load_image('Blue/Blue_Run.png')
        self.Jump_image=load_image('Blue/Blue_Jump.png')
        self.Attack_image=load_image('Blue/Blue_Attack2.png')
        pass

    def draw(self):
        pass

    def update(self):
        pass
