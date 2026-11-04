from pico2d import load_image

class Pink:
    #핑킹 속성 초기화
    def __init__(self):
        self.image('Pink/Pink_Idle')
        self.x=400
        self.y=300
        pass
    
    #핑킹 그리기
    def draw(self):
        self.image.draw(self.x,self.y)
        pass

    #핑킹 애니메이션 관리
    def update(self):
        pass