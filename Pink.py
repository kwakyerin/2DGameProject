from pico2d import load_image

class Pink:
    #핑킹 속성 초기화
    def __init__(self):
        self.Idle_image=load_image('Pink/Pink_Idle.png')
        self.Run_image=load_image('Pink/Pink_Run.png')
        self.x=400
        self.y=300

        self.frame=0
        self.dir=0
        pass
    
    #핑킹 그리기
    def draw(self):
        self.image.clip_draw(self.frame*32,0,32,32,self.x,self.y,70,70)
        pass

    #핑킹 애니메이션 관리
    def update(self):
        self.frame=(self.frame+1)%4
        self.x+=self.dir
        pass