#character ATL
transform enter_l:
    subpixel True
    alpha 0.0
    xpos -200
    parallel:
        ease 1.0 xpos 100
        ease 0.1 alpha 1.0

transform leave:
    subpixel True
    alpha 1.0
    parallel:
        ease 0.5 xpos -400
        ease 0.1 alpha 0.0

transform exp:
    subpixel True
    ease 0.1 ypos +20
    ease 0.1 ypos -20
