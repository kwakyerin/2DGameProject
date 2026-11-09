from pico2d import load_image

class Character:
    def __init__(self):

        self.character_type=1

        #핑킁
        self.Pink_Idle=load_image('Pink/Pink_Idle.png')
        self.Pink_Run=load_image('Pink/Pink_Run.png')
        self.Pink_Jump=load_image('Pink/Pink_Jump.png')
        self.Pink_Attack=load_image('Pink/Pink_Attack2.png')

        #블룽
        self.Blue_Idle=load_image('Blue/Blue_Idle.png')
        self.Blue_Run=load_image('Blue/Blue_Run.png')
        self.Blue_Jump=load_image('Blue/Blue_Jump.png')
        self.Blue_Attack=load_image('Blue/Blue_Attack.png')

        #옐로웅
        self.Yellow_Idle=load_image('Yellow/Yellow_Idle.png')
        self.Yellow_Run=load_image('Yellow/Yellow_Run.png')
        self.Yellow_Jump=load_image('Yellow/Yellow_Jump.png')
        self.Yellow_Attack=load_image('Yellow/Yellow_Attack.png')
        pass

    def transform(self):
        pass
