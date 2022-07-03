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
    ypos 370
    linear 0.1 ypos 390
    linear 0.1 ypos 370

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform train_halt:
    subpixel True
    yoffset 0
    parallel:
        ease 0.1 zoom 2.0
    parallel:
        ease 0.1 yalign 0.5

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform train_halt2:
    subpixel True
    yoffset 0
    parallel:
        ease 0.8 zoom 1.0
    parallel:
        ease 0.8 yoffset 30

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform zoomin:
    subpixel True
    yoffset 0
    parallel:
        ease 0.3 zoom 1.25
    parallel:
        ease 0.1 yalign 0.5

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0

transform zoomout:
    subpixel True
    yoffset 0
    parallel:
        ease 0.3 zoom 1.0
    parallel:
        ease 0.8 yoffset 30

    on hide:
        parallel:
            ease 0.8 xalign -1.0
        parallel:
            linear 1.0 alpha 0.0
#BG ATL
transform blurry:
    blur 10

transform stab_ef:
    alpha 0.0
    pause(0.5)
    linear 0.1 alpha 1.0
    linear 0.3 alpha 0.6
    linear 0.2 alpha 0.8
    linear 0.4 alpha 0.5
    linear 1.0 alpha 0.0
