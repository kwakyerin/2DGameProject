from pico2d import load_image

class Pink:
    #핑킹 속성 초기화
    def __init__(self):
        self.image=load_image('Pink/Pink_Idle.png')
        self.x=400
        self.y=300
        pass
    
    #핑킹 그리기
    def draw(self):
        self.image.clip_draw(0,0,32,32,self.x,self.y,70,70)
        pass

    #핑킹 애니메이션 관리
    def update(self):
        pass