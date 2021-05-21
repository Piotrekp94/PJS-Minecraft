def on_on_chat():
    global sizeX, sizeY, dist2
    sizeX = 30
    sizeY = 30
    i = 0
    while i <= sizeX:
        j = 0
        while j <= sizeY:
            dist2 = Math.floor(abs(Math.sqrt((i - sizeX / 2) * (i - sizeX / 2) + (j - sizeY / 2) * (j - sizeY / 2))))
            if dist2 % 2 == 0:
                blocks.place(WOOL, builder.position())
            else:
                blocks.place(BLACK_WOOL, builder.position())
            builder.move(FORWARD, 1)
            j += 1
        builder.turn(LEFT_TURN)
        builder.turn(LEFT_TURN)
        builder.move(FORWARD, sizeX + 1)
        builder.turn(LEFT_TURN)
        builder.turn(LEFT_TURN)
        builder.move(UP, 1)
        i += 1
player.on_chat("circle", on_on_chat)

dist2 = 0
sizeY = 0
sizeX = 0
dist = 0