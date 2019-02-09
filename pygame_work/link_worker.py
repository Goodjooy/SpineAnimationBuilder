import os
import sys

import pygame
import threading

from mod_act.classes import mod_load


class LinkWorker(threading.Thread):
    def __init__(self, mod: mod_load.SubModel, linked: mod_load.SubModel):
        super(LinkWorker, self).__init__()
        self.linked_mod = linked
        self.mod = mod

        pygame.init()

        self.size = (512, 512)

        self.bg_color = (255, 255, 255)

        self.screen: pygame.Surface = pygame.display.set_mode(self.size)

        pygame.display.set_caption("link_worker")

        self.exit = False

        self.type = 0
        # type==0 ->被连接点坐标点
        # type==1 ->连接坐标点

        self.linked = [-1, -1]
        self.link = [-1, -1]

    def run(self):

        while not self.exit:
            # 事件判断
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONUP:
                if self.type == 0 and event.button == 1:
                    self.linked = event.pos
                if self.type == 1 and event.button == 1:
                    self.link = event.pos

            # 绘制
            self.screen.fill(self.bg_color)
            pygame.mouse.set_visible(False)

            if self.type == 1:

                self.screen.blit(self.mod.pic, (0, 0))
            else:

                self.screen.blit(self.linked_mod.pic, (0, 0))
                self.mod.move(*pygame.mouse.get_pos())
                # print(self.mod.bilt_rect)
                self.screen.blit(self.mod.pic, (self.mod.bilt_rect.x, self.mod.bilt_rect.y))

            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pygame.mouse.get_pos(), (2, 2)), 1)

            pygame.display.flip()
        pygame.quit()

    def change_type(self, type_val):
        self.type = type_val


if __name__ == '__main__':
    a = LinkWorker(None, None)
    a.run()
