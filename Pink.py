from pico2d import load_image

class Pink:
    #핑킹 속성 초기화
    def __init__(self):
        self.Idle_image=load_image('Pink/Pink_Idle.png')
        self.Run_image=load_image('Pink/Pink_Run.png')
        self.Attack_image=load_image('Pink/Pink_Attack2.png')
        self.Jump_image=load_image('Pink/Pink_Jump.png')
        
        self.x=35
        self.y=35

        self.frame=0
        self.speed=0
        self.dir=1

        #점프 관리 변수  
        self.ground_y=35 #착지 바닥 높이
        self.vy=0 #캐릭터 수직 속도
        self.gravity=0.5
        self.jump_power=10

        self.is_attack=False

        # 애니메이션 시간 초기화
        self.animation_time = 0
    
    #핑킹 그리기
    def draw(self):

        if self.is_attack:
            self.image=self.Attack_image
        elif self.speed == 0:
            self.image = self.Idle_image   
        else:
            self.image = self.Run_image

        if self.dir<0:
            self.image.clip_composite_draw(self.frame*32,0,32,32,
        0,'h',self.x,self.y,70,70)
        else:
            self.image.clip_draw(self.frame*32,0,32,32,
        self.x,self.y,70,70)

    #핑킹 애니메이션 관리
    def update(self):

        self.x += self.dir * self.speed
        self.animation_time += 0.01

        #점프/중력 처리
        self.y += self.vy
        self.vy -= self.gravity

        #바닥 착지 설정
        if self.y <= self.ground_y:
           self.y = self.ground_y
           self.vy = 0

    #각 상태 애니메이션 관리(delay랑 프레임 수 입력)   
        if self.is_attack:
            frame_count = 6
            frame_delay = 0.06

        elif self.speed == 0:
            frame_count = 4
            frame_delay = 0.15

        else:
            frame_count = 6
            frame_delay = 0.08 

        if self.animation_time >= frame_delay:
            self.frame += 1
            self.animation_time = 0

        if self.is_attack and self.frame >= 6:
            self.is_attack = False
            self.frame = 0
        elif not self.is_attack:
            self.frame %= frame_count

    #공격
    def attack(self):
        if not self.is_attack:
            self.is_attack=True
            self.frame=0
            self.animation_time=0

    #점프
    def jump(self):     
        if self.y<=self.ground_y: #먼저 캐릭터가 바닥에 있는지 확인
            self.vy=self.jump_power #수직 속도 이용해서 점프
        pass

   