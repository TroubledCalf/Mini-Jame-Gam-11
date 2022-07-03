#character ATL
transform enter_l:
    subpixel True
    alpha 1.0
    yalign 1.0
    xalign -1.0
    ease 0.8 xalign 0.25

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform enter_m:
    subpixel True
    alpha 1.0
    yalign 1.0
    xalign -1.0
    ease 0.8 xalign 0.5

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform enter_r:
    subpixel True
    alpha 1.0
    yalign 1.0
    xalign -1.0
    ease 0.8 xalign 0.75

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform exp:
    subpixel True
    yoffset 0
    linear 0.1 yoffset 58
    linear 0.1 yoffset 0

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0
