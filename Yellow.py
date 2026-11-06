from pico2d import load_image

class Yellow:
    def __init__(self):
        self.Idle_image=load_image('Yellow/Yellow_Idle.png')
        self.Run_image=load_image('Yellow/Yellow_Run.png')
        self.Jump_image=load_image('Yellow/Yellow_Jump.png')
        self.Attack_image=load_image('Yellow/Yellow_Attack2.png')
        pass

    def draw(self):
        pass

    def update(self):
        pass