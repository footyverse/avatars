from PIL import Image
num_shirts = 10
num_shorts = 5
num_eyes = 5
num_hair = 5
body = Image.open('images/body.png')
head = Image.open('images/head.png')
# shirt = Image.open('images/shirt.png')
shorts = Image.open('images/shorts1.png')
shoes = Image.open('images/shoes.png')
eyes = Image.open('images/eyes1.png')
body_size = body.size
n = 1
# while n<6:
#     # hair = Image.open('images/hair%s.png'%n)
#     player = Image.new('RGBA',(body_size[0], body_size[1]))
#     player.paste(body,(0,0), body)
#     player.paste(hair,(20,0), hair)
#     player.paste(head,(40,20), head)
#     player.paste(shirt,(10,90), shirt)
#     player.paste(shorts,(40,170), shorts)
#     player.paste(shoes,(20,250), shoes)
#     player.save("images/players/player%s.png"%n,"PNG")
#     n+=1
#     print(n)
collage = Image.new('RGBA',(10*body_size[0], 10*body_size[1]))
for shirt_item in range(num_shirts):
    shirt = Image.open('images/shirt%s.png'%(shirt_item+1))
    for hair_item in range(num_hair):
        player = Image.new('RGBA',(body_size[0], body_size[1]))
        player.paste(body,(0,0), body)
        hair = Image.open('images/hair%s.png'%(hair_item+1))
        player.paste(hair,(20,0), hair)
        player.paste(head,(40,20), head)
        player.paste(eyes,(60,40), eyes)
        player.paste(shirt,(10,90), shirt)
        player.paste(shorts,(40,170), shorts)
        player.paste(shoes,(20,250), shoes)
        # player.save("images/players/player%s%s.png"%(shirt_item+1, hair_item+1),"PNG")
        collage.paste(player,(((n-1)%10)*body_size[0],((n-1)//10)*body_size[1]))
        print(n)
        # print(((n-1)%10)*body_size[0], (n//10)*body_size[1])

        n+=1
collage.save("images/players/collage.png","PNG")