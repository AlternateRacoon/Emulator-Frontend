import glob
import os

import pygame
from pygame.locals import *

#Initializing Pygame
pygame.init()

#Setting The Display
screen = pygame.display.set_mode((1280,720))

#Setting The Paths
path_roms = "/home/ayaan/Python Projects/Emulator-Frontend/Roms/"
path_assets = "/home/ayaan/Python Projects/Emulator-Frontend/Assets/"
path_thumb = "/home/ayaan/Python Projects/Emulator-Frontend/Thumbnails/"
path_dir = "/home/ayaan/Python Projects/Emulator-Frontend/"

#Variable Contains all the assets filenames
os.chdir(path_assets)
cfiles = glob.glob('*.png')

#Getting the filenames of roms
os.chdir(path_roms + "/Gamecube")
gc_roms = glob.glob('*.iso')
os.chdir(path_roms + "/PS2")
ps2_roms = glob.glob('*.iso')
os.chdir(path_roms + "/Arcade")
arcade_roms = glob.glob('*.zip')
os.chdir(path_roms + "/Wii-U")
wiiu_roms = glob.glob('*.wud')
os.chdir(path_roms + "/Snes")
snes_roms = glob.glob('*.sfc')
os.chdir(path_roms + "/Nes")
nes_roms = glob.glob('*.sfc')

#Defining all the System's Menu

def gamecube_menu(gamecube_width, gamecube_hieght):
    gc_controller = pygame.image.load(path_assets + "controller_gc.png").convert_alpha()
    gc_controller = pygame.transform.scale(gc_controller, (80, 50)).convert_alpha()
    font = pygame.font.SysFont('GAMECUBEN', 50)
    gamecube = font.render("Gamecube", False, (255, 255, 255))
    rect_outline = pygame.draw.rect(screen, [153,50,204], (gamecube_width,gamecube_hieght,500,100))
    screen.blit(gc_controller.convert_alpha(), (gamecube_width + 380, gamecube_hieght + 20))
    screen.blit(gamecube, (gamecube_width + 5, gamecube_hieght + 15))

def ps2_menu(ps2_width, ps2_hieght):
    ps2_controller = pygame.image.load(path_assets + "controller_ps2.png").convert_alpha()
    ps2_controller = pygame.transform.scale(ps2_controller, (80, 80)).convert_alpha()
    font = pygame.font.SysFont('Blue Players', 50)
    ps2 = font.render("PS 2", False, (255, 255, 255))
    rect_outline = pygame.draw.rect(screen, [211,211,211], (ps2_width,ps2_hieght,500,100))
    screen.blit(ps2_controller.convert_alpha(), (ps2_width + 380, ps2_hieght + 10))
    screen.blit(ps2, (ps2_width + 5, ps2_hieght + 30))

def arcade_menu(arcade_width, arcade_hieght):
    arcade_controller = pygame.image.load(path_assets + "controller_stick.png").convert_alpha()
    arcade_controller = pygame.transform.scale(arcade_controller, (80, 90)).convert_alpha()
    font = pygame.font.SysFont('Arcade Normal', 50)
    arcade = font.render("Arcade", False, (255, 255, 255))
    rect_outline = pygame.draw.rect(screen, [255,0,0], (arcade_width,arcade_hieght,500,100))
    screen.blit(arcade_controller.convert_alpha(), (arcade_width + 380, arcade_hieght + 5))
    screen.blit(arcade, (arcade_width + 5, arcade_hieght + 30))

def wiiu_menu(wiiu_width, wiiu_hieght):
    wiiu_controller = pygame.image.load(path_assets + "controller_wiiu.png").convert_alpha()
    wiiu_controller = pygame.transform.scale(wiiu_controller, (100, 50)).convert_alpha()
    font = pygame.font.SysFont('Continuum Bold', 80)
    wiiu = font.render("Wii U", False, (255,255,255))
    rect_outline = pygame.draw.rect(screen, [63, 255, 238], (wiiu_width,wiiu_hieght,500,100))
    screen.blit(wiiu_controller.convert_alpha(), (wiiu_width + 370, wiiu_hieght + 20))
    screen.blit(wiiu, (wiiu_width + 5, wiiu_hieght + 10))

def snes_menu(snes_width, snes_hieght):
    snes_controller = pygame.image.load(path_assets + "controller_snes.png").convert_alpha()
    snes_controller = pygame.transform.scale(snes_controller, (100, 50)).convert_alpha()
    font = pygame.font.SysFont('SNES', 80)
    snes = font.render("SNES", False, (255,255,255))
    rect_outline = pygame.draw.rect(screen, [211,211,211], (snes_width,snes_hieght,500,100))
    screen.blit(snes_controller.convert_alpha(), (snes_width + 370, snes_hieght + 20))
    screen.blit(snes, (snes_width + 5, snes_hieght + 20))

def nes_menu(nes_width, nes_hieght):
    nes_controller = pygame.image.load(path_assets + "controller_nes.png").convert_alpha()
    nes_controller = pygame.transform.scale(nes_controller, (100, 50)).convert_alpha()
    font = pygame.font.SysFont('SNES', 80)
    nes = font.render("NES", False, (255,255,255))
    rect_outline = pygame.draw.rect(screen, [211,211,211], (nes_width,nes_hieght,500,100))
    screen.blit(nes_controller.convert_alpha(), (nes_width + 370, nes_hieght + 20))
    screen.blit(nes, (nes_width + 5, nes_hieght + 20))

#This Function Checks The Roms Folder And If It Finds A Rom It Adds the Menu for that system
def check_roms_menu(menu_w=0,menu_h=0):
    global menu_hieght
    global first_gc, first_ps2, first_arcade, first_wiiu
    first_gc = 0
    first_ps2 = 0
    first_arcade = 0
    first_wiiu = 0
    if gc_roms:
        gamecube_menu(menu_w, menu_h)
        first_gc = 1
        menu_h += 200
    if ps2_roms:
        ps2_menu(menu_w,menu_h)
        if first_gc == 1:
            first_ps2 = 2
        else:
            first_ps2 = 1
        menu_h += 200
    if arcade_roms:
        arcade_menu(menu_w, menu_h)
        if first_ps2:
            first_arcade += first_ps2 + 1
        elif first_gc == 1:
            first_arcade += first_gc + 1
        else:
            first_arcade == 1
        menu_h += 200
    if wiiu_roms:
        wiiu_menu(menu_w, menu_h)
        if first_arcade:
            first_wiiu += first_arcade + 1
        elif first_gc == 1:
            first_wiiu += first_gc + 1
        elif first_ps2:
            first_wiiu += first_ps2 + 1
        else:
            first_wiiu == 1
        menu_h += 200
    menu_hieght = menu_h
#This Is the same function as before but now it does it for the second page
def check_roms_menu_second(menu_w=0,menu_h=0):
    global menu_hieght
    global first_snes, first_nes
    first_snes = 0
    first_nes = 0
    if snes_roms:
        snes_menu(menu_w, menu_h)
        first_snes = 1
        menu_h += 200
    if nes_roms:
        nes_menu(menu_w, menu_h)
        if snes_roms:
            first_snes = first_snes + 1
        else:
            first_snes = 1
    menu_hieght = menu_h

#Initializing Joystick
pygame.joystick.init()

#Getting The Joystick Count
joystick_count = pygame.joystick.get_count()

#Loads Asset
image_not_found = pygame.image.load(path_assets + "image_not_found.png").convert_alpha()
image_not_found = pygame.transform.scale(image_not_found, (80, 90)).convert_alpha()

#The Input Box Which Asks For Path When "C" Is Pressed
font = pygame.font.SysFont('Bebas Neue', 20)
font_larger = pygame.font.SysFont('Bebas Neue', 50)
font1 = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(570,400, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
popup_menu = pygame.Surface((300, 300))
popup_menu.set_alpha(128)
popup_menu.fill((70, 70, 70))

#Going to the main directory
os.chdir(path_dir)

#Opening the paths.ini file and reading it
text = open("paths.ini", "r").read()


#Setting all the paths in the syntax they are in the .ini file
mame_path = text.splitlines()[2].replace("MamePath=","")
dolphin_path = text.splitlines()[0].replace("DolphinPath=","")
ps2_path = text.splitlines()[1].replace("PCSX2Path=","")
cemu_path = text.splitlines()[3].replace("CemuPath=","")
snes_path = text.splitlines()[4].replace("SnesPath=","")
nes_path = text.splitlines()[5].replace("NesPath=","")

#setting variables
text = text.splitlines()
check = True
done = True
menu_enabled = 0
allow_c = 0
allow_down = 0
second_page_enabled = False
color = color_inactive
active = True

systems = ["gc", "ps2", "arcade", "wiiu", "snes", "nes"]

pygame.init()

while done:
    #Checking If There Is A Joystick Connected
    if joystick_count == 1:
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        axis0 = joystick.get_axis(1)
        axis0 = int(round(axis0))
    else:
        axis0 = 0
   #Variable to Determine How many system menu's have been defined
    menu_width = 0
    menu_hieght = 0
    #checks if it is the first page of systems or second
    if second_page_enabled:
        check_roms_menu_second()
    else:
        check_roms_menu()
    #The Selection Outline around the system menu (only executed once)
    if check:
        rect = pygame.Rect(0, 0, 500,100)
        rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
        pygame.display.flip()
        pygame.display.update()
        check = False
    #if there are joysticks connected get thier input data
    event = pygame.event.wait()
    if pygame.joystick.get_count() == 1:
        buttons = joystick.get_numbuttons()
        button_1 = []
        for i in range(buttons):
            button = joystick.get_button(i)
            button_1.append(button)
    else:
        button_1 = [0,0]
    #If the cross button is pressed it closses the program
    if event.type == pygame.QUIT:
        done = False
    #Check If An Key Is Pressed
    if menu_enabled == 1:
        screen.fill((0, 0, 0))
        check_roms_menu()
        check = True
        if check:
            rect = pygame.Rect(0, rect.y, 500, 100)
            rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
            check = False
        if first == "gc":
            path = font_larger.render("Dolphin Path", False, (255, 255, 255))
            text_blit = text.replace("DolphinPath=", "")
        elif first == "ps2":
            path = font_larger.render("PCSX2 Path", False, (255, 255, 255))
            text_blit = text.replace("PCSX2Path=", "")
        elif first == "arcade":
            path = font_larger.render("M.A.M.E Path", False, (255, 255, 255))
            text_blit = text.replace("MamePath=", "")
        elif first == "wiiu":
            path = font_larger.render("CEMU Path", False, (255, 255, 255))
            text_blit = text.replace("CemuPath=", "")
        elif first == "snes":
            path = font_larger.render("SNES Path", False, (255, 255, 255))
            text_blit = text.replace("SnesPath=", "")
        elif first == "nes":
            path = font_larger.render("NES Path", False, (255, 255, 255))
            text_blit = text.replace("NesPath=", "")
        screen.blit(popup_menu, [520, 250])
        screen.blit(path, [560, 260])
        txt_surface = font.render(text_blit, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.update()
        pygame.display.flip()
    if event.type == KEYDOWN or (axis0 == 1) or (axis0 == -1) or (button_1[0] == 1) or (button_1[1] == 1):
        #Check if its the first page or second then set a variable which will contain which system menu the outline rectangle is on
        if second_page_enabled:
            first_systems = [first_snes, first_nes]
            for row in range(len(first_systems)):
                if row == 0:
                    first_s = "snes"
                    first_s = "nes"
                if first_systems[row] == 1 and rect.y == 600:
                    first = first_s
                if first_systems[row] == 2 and rect.y == 800:
                    first = first_s
        else:
            first_systems = [first_gc, first_ps2, first_arcade, first_wiiu]
            for row in range(len(first_systems)):
                if row == 0:
                    first_s = "gc"
                if row == 1:
                    first_s = "ps2"
                if row == 2:
                    first_s = "arcade"
                if row == 3:
                    first_s = "wiiu"
                if first_systems[row] == 1 and rect.y == 0:
                    first = first_s
                if first_systems[row] == 2 and rect.y == 200:
                    first = first_s
                    print(first)
                if first_systems[row] == 3 and rect.y == 400:
                    first = first_s
                if first_systems[row] == 4 and rect.y == 600:
                    first = first_s
            first_rect = rect.y
        #checks if the popup menu is active or not
        if type(text) == list:
            for position, row in enumerate(systems):
                if row == first:
                        text = text[position]

        if menu_enabled == 1:
            if event.key == pygame.K_RETURN:
                os.chdir(path_dir)
                #It Edits the ini file that got opened earlier and writes it back
                for position,row in enumerate(systems):
                    lines = ["DolphinPath=" + dolphin_path, "\nPCSX2Path="+ ps2_path,"\nMamePath=" + mame_path, "\nCemuPath=" + cemu_path, "\nSnesPath=" + snes_path, "\nNesPath=" + nes_path]
                    lines[position] = text[position]
                os.system("rm paths.ini")
                with open("paths.ini", "w") as file_new:
                    for line in lines:
                        file_new.write(line)
                file_new.close()
            # It Creats A Textbox and it edits the text then updates the text on the screen
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_c:
                if allow_c == 0:
                    pass
                if allow_c >= 1:
                    text += event.unicode
                allow_c += 1
            elif event.key == pygame.K_ESCAPE:
                pass
            else:
                text += event.unicode
        if event.type == KEYDOWN:
            pass
        else:
            event.key = ""
        # if  key on the joystick is pressed it closses the program
        if (button_1[1] == 1):
            pygame.quit()
        # Enables the menu when "C" is pressed
        elif event.key == K_c:
            if menu_enabled == 0:
                menu_enabled = 1
        # If Pressed Escape When Menu Is Active Closes the Menu Window
        if (event.key == K_ESCAPE):
            if menu_enabled == 1:
                screen.fill((0,0,0))
                check_roms_menu()
                check = True
                if check:
                    rect = pygame.Rect(0, rect.y, 500, 100)
                    rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                    pygame.display.flip()
                    pygame.display.update()
                    menu_enabled -= 1
                    check = False
                allow_c = 0
        #Checks If The Menu Is Enabled or not if not Enters the Submenu For the System The White Box is On
        if menu_enabled >= 1:
            pass
        elif (event.key == K_RETURN) or (button_1[0] == 1):
            # Creats an entirely new display
            screen = pygame.display.set_mode((1280, 720))
            keymap = {}
            thumbnails = []
            game_name = []
            # Checks The System that Was Clicked on
            if first == "arcade":
                os.chdir(path_roms + "Arcade/")
                files = glob.glob("*.zip")
                os.chdir(path_thumb + "Arcade/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".zip", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "Arcade"
            if first == "gc":
                os.chdir(path_roms + "Gamecube/")
                files = glob.glob("*.iso")
                os.chdir(path_thumb +"GameCube/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".iso", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "GameCube"
            if first == "ps2":
                os.chdir(path_roms + "PS2/")
                files = glob.glob("*.iso")
                os.chdir(path_thumb + "PS2/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".iso", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "PS2"
            if first == "wiiu":
                os.chdir(path_roms + "Wii-U/")
                files = glob.glob("*.wud")
                os.chdir(path_thumb + "Wii-U/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".wud", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "Wii U"
            if first == "snes":
                os.chdir(path_roms + "Snes/")
                files = glob.glob("*.sfc")
                os.chdir(path_thumb + "Snes/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".sfc", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "Snes"
            if first == "nes":
                os.chdir(path_roms + "Nes/")
                files = glob.glob("*.sfc")
                os.chdir(path_thumb + "Nes/")
                thumbnails_unfiltered = glob.glob("*.png")
                for row in files:
                    row = row.replace(".sfc", "")
                    game_name.append(row)
                    for r in thumbnails_unfiltered:
                        if row in r:
                            thumbnails.append(r)
                system = "Nes"
            game_select = 1
            loaded_images = []
            images = 0
            # Loading Thumbnails
            for row in thumbnails:
                image = pygame.image.load(path_thumb+ "/"+ system +"/" + row)
                image = pygame.transform.scale(image, (200, 200))
                images += 1
                loaded_images.append(image)
            no_image = 0
            running = True
            allow = True
            allow_blit = True
            rect_x = 0
            rect_y = 0
            while running:
                # Checks If A Joystick is connected or not
                if pygame.joystick.get_count() == 1:
                    axis1 = joystick.get_axis(1)
                    axis1 = int(round(axis1))
                    axis0 = joystick.get_axis(2)
                    axis0 = int(round(axis0))
                else:
                    axis0 = 0
                    axis1 = 1
                width = 0
                hieght = 0
                # Uses Blit To Show The Thubmnails On Screen If There isnt a thumbnail it Shows Nothing
                if allow_blit:
                    if loaded_images:
                        for row in range(len(loaded_images)):
                            screen.blit(loaded_images[row], (width, hieght))
                            if allow:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                            allow = False
                            width += 200
                    if int(len(files)) > len(thumbnails):
                        no_image = len(files) - images
                        for row in range(no_image):
                            rect = pygame.Rect(width, hieght, 200, 200)
                            rect_outline = pygame.draw.rect(screen, [169,169,169], rect, 0)
                            screen.blit(image_not_found, (width + 60, hieght))
                            if allow:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                            allow = False
                            width += 200
                    allow_blit = False
                pygame.display.flip()
                pygame.display.update()
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    running = False
                if pygame.joystick.get_count() == 1:
                    buttons = joystick.get_numbuttons()
                    button_1 = []
                    for i in range(buttons):
                        button = joystick.get_button(i)
                        button_1.append(button)
                else:
                    button_1 = [0,0]

                if event.type == KEYDOWN or (axis0 == 1) or (axis0 == -1) or (button_1[0] == 1) or (button_1[1] == 1):
                    if event.type == KEYDOWN:
                        keymap[event.scancode] = event.unicode
                    else:
                        event.key = ""
                    if (event.key == K_RETURN) or (button_1[0] == 1):
                        if first == "gc":
                            os.chdir(path_dir)
                            file = open("paths.ini","r").read()
                            if file:
                                if first == "gc":
                                    file = file.splitlines()[0].replace("DolphinPath=","")
                                elif first == "ps2":
                                    if first_rect == 0:
                                        file = file.splitlines()[0].replace("PCSX2Path=", "")
                                    elif first_rect == 200:
                                        file = file.splitlines()[1].replace("PCSX2Path=", "")
                                os.chdir(path_roms+ "Gamecube")
                                os.system(file + '"' +files[game_select - 1] + '"')
                        elif first == "ps2":
                            os.chdir(path_dir)
                            file = open("paths.ini","r").read()
                            if file:
                                file = file.splitlines()[0].replace("PCSX2Path=","")
                                os.chdir(path_roms +"\PS2")
                                os.system(file + '"' +files[game_select - 1] + '"')
                        elif first == "Arcade":
                            os.chdir(path_dir)
                            file = open("paths.ini","r").read()
                            if file:
                                file = file.splitlines()[0].replace("MamePath=","")
                                os.chdir(path_roms + "\Arcade")
                                os.system(file + '"' +files[game_select - 1] + '"')
                    if (event.key == K_BACKSPACE):
                        break
                    # Moves The White Square Everytime Left Or Right Is Pressed
                    if (event.key == K_RIGHT) or (axis0 == 1):
                        screen.fill((0, 0, 0))
                        width = 0
                        hieght = 0
                        if loaded_images:
                            for row in loaded_images:
                                screen.blit(row, (width, hieght))
                                width += 200
                        if int(len(files)) > len(thumbnails):
                            no_image = len(files) - images
                            for row in range(no_image):
                                rect = pygame.Rect(width, hieght, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [169, 169, 169], rect, 0)
                                screen.blit(image_not_found, (width + 60, hieght))
                                if allow:
                                    rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                    rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                allow = False
                                width += 200
                        allow_blit = False
                        if len(loaded_images) == 1:
                            if rect_x > 200:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                            elif rect_x == 0:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                        elif len(loaded_images) == 0:
                            if no_image == 1:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                            else:
                                limit = (no_image - 1) * 200
                                if rect_x == limit:
                                    rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                    rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                    pygame.display.flip()
                                    pygame.display.update()
                                else:
                                    rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                    rect_x += 200
                                    rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                    pygame.display.flip()
                                    pygame.display.update()
                        if len(loaded_images) >= 1 and no_image >= 1:
                            limit = (len(files) - 1) * 200
                            if rect_x == limit:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                            else:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_x += 200
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                        else:
                            if rect_x < width - 200:
                                rect_x += 200
                                game_select += 1
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                            elif rect_x == width - 200:
                                rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                pygame.display.flip()
                                pygame.display.update()
                    if (event.key == K_LEFT) or (axis0 == -1):
                        screen.fill((0, 0, 0))
                        width = 0
                        hieght = 0
                        if loaded_images:
                            for row in loaded_images:
                                screen.blit(row, (width, hieght))
                                width += 200
                                if int(len(files)) > len(thumbnails):
                                    no_image = len(files) - images
                                    for row in range(no_image):
                                        rect = pygame.Rect(width, hieght, 200, 200)
                                        rect_outline = pygame.draw.rect(screen, [169, 169, 169], rect, 0)
                                        screen.blit(image_not_found, (width + 60, hieght))
                                        if allow:
                                            rect = pygame.Rect(rect_x, rect_y, 200, 200)
                                            rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                                        allow = False
                                        width += 200

                        if rect_x <= 0:
                            rect = pygame.Rect(rect_x, rect_y, 200, 200)
                            rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                            pygame.display.flip()
                            pygame.display.update()
                        else:
                            rect_x -= 200
                            game_select -= 1
                            rect = pygame.Rect(rect_x, rect_y, 200, 200)
                            rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                            pygame.display.flip()
                            pygame.display.update()
            screen = pygame.display.set_mode((1280, 720))
            screen.fill((0, 0, 0))
            if second_page_enabled:
                check_roms_menu_second()
            else:
                check_roms_menu()
            check = True
            if check:
                if second_page_enabled:
                    first_rect -= 600
                    rect = pygame.Rect(0, first_rect, 500, 100)
                    first_rect += 600
                else:
                    rect = pygame.Rect(0, first_rect, 500, 100)
                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                pygame.display.flip()
                pygame.display.update()
                check = False

        if (event.key == K_DOWN) or (axis0 == 1):
            rect_y = rect.y + 200
            if rect_y > menu_hieght - 200:
                pass
            if second_page_enabled or rect.y >= 600:
                if rect_y > menu_hieght:
                    pass
                else:
                    screen.fill((0,0,0))
                    second_page_enabled = True
                    check_roms_menu_second()
                    if allow_down == 0:
                        rect.y = 0
                        rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                    else:
                        rect.y += 200
                        rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                    pygame.display.update()
                    pygame.display.flip()
                    allow_down = 1
            else:
                rect.y += 200
                screen.fill((0,0,0))
                check_roms_menu()
                rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                pygame.display.update()
                pygame.display.flip()
        if (event.key == K_UP) or (axis0 == -1):
            if rect.y == 0 and second_page_enabled == False:
                pass
            else:
                if second_page_enabled:
                    screen.fill((0,0,0))
                    if rect.y == 0:
                        check_roms_menu()
                        rect.y = 600
                        rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                        pygame.display.update()
                        pygame.display.flip()
                        second_page_enabled = False
                    elif rect.y == 200:
                        check_roms_menu_second()
                        rect.y -= 200
                        rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                        pygame.display.update()
                        pygame.display.flip()
                else:
                    screen.fill((0,0,0))
                    check_roms_menu()
                    rect.y -= 200
                    rect_outline = pygame.draw.rect(screen, [255, 255, 255], rect, 5)
                    pygame.display.update()
                    pygame.display.flip()
                    second_page_enabled = False
