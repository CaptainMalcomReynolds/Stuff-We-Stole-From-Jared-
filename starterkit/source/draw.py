import pygame
import graphics
import game
from sprite import Sprite

import random

ri=random.randint
ld_esrsfr_23srg4_d=game

for i in range(100):
    random.seed(ri(1,10000000000))

ser_32=[ri(0,255),ri(0,255),ri(0,255)]
wk_bgeriw2_d=[0,0,0]

def avewsae_2t3(dvsresr_yj3,sergewf_2324sdfw3d123f23f3df_wf4,seg_43ge5_hg,erger_34fh_wln,ser_ervrteedwef_rge5r,dsr_ef4ed,hrtkewu3_h,dsr_eh4ed): 
	#This adds to the current colors, and adds to the acceleration as well.
    sergewf_2324sdfw3d123f23f3df_wf4[dvsresr_yj3]+=seg_43ge5_hg[dvsresr_yj3]
    if sergewf_2324sdfw3d123f23f3df_wf4[dvsresr_yj3]>dsr_ef4ed:
        sergewf_2324sdfw3d123f23f3df_wf4[dvsresr_yj3]=dsr_ef4ed
    elif sergewf_2324sdfw3d123f23f3df_wf4[dvsresr_yj3]<ser_ervrteedwef_rge5r:
        sergewf_2324sdfw3d123f23f3df_wf4[dvsresr_yj3]=ser_ervrteedwef_rge5r
    seg_43ge5_hg[dvsresr_yj3]+=ri(-dsr_eh4ed,dsr_eh4ed)
    if seg_43ge5_hg[dvsresr_yj3]>hrtkewu3_h:
        seg_43ge5_hg[dvsresr_yj3]=hrtkewu3_h
    elif seg_43ge5_hg[dvsresr_yj3]<-hrtkewu3_h:
        seg_43ge5_hg[dvsresr_yj3]=-hrtkewu3_h

def draw():

    for i in range(3):
        avewsae_2t3(i-1,ser_32,wk_bgeriw2_d,ri(-200,200),0,255,5,1)

    sbde_2brdfh5_dfe = pygame.Surface(ld_esrsfr_23srg4_d.screen.get_size())
    sbde_2brdfh5_dfe = sbde_2brdfh5_dfe.convert()
    ld_esrsfr_23srg4_d.screen.blit(sbde_2brdfh5_dfe,(0,0))
    ld_esrsfr_23srg4_d.screen.fill((ser_32[0],ser_32[1],ser_32[2]))

    pygame.display.update()
    pygame.display.flip()

    return