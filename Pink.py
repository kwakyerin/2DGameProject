from pico2d import load_image

class Pink:
    #핑킹 속성 초기화
    def __init__(self):
        self.Idle_image=load_image('Pink/Pink_Idle.png')
        self.Run_image=load_image('Pink/Pink_Run.png')
        self.x=35
        self.y=35

        self.frame=0
        self.speed=3
        self.dir=0

        # 애니메이션 시간 초기화
        self.animation_time = 0
    
    #핑킹 그리기
    def draw(self):

        if self.dir==0:
            self.image=self.Idle_image
        else:
            self.image=self.Run_image

        self.image.clip_draw(self.frame*32,0,32,32,self.x,self.y,70,70)
    
    #핑킹 애니메이션 관리
    def update(self):

        self.x += self.dir * self.speed

        self.animation_time += 0.01

        if self.dir == 0:
            frame_count = 4
            frame_delay = 0.15
        else:
            frame_count = 6
            frame_delay = 0.08

        # 일정 시간이 지나면 프레임 변경
        if self.animation_time >= frame_delay:
            self.frame = (self.frame + 1) % frame_count
            self.animation_time = 0    
   